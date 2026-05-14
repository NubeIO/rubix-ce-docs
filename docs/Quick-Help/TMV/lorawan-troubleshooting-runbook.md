# LoRaWAN / ChirpStack Troubleshooting Runbook

Date: 2026-05-13  
Host: `10.8.1.17` (`estiahealthtmv`)

## Scope
This runbook documents the exact troubleshooting and fixes used for:
- `module-core-lorawan` showing `mqtt - unable to connect`
- `nubeio-lorawan-modbus-bridge` runtime failures (`socat` / `/data/socat`)
- `lorawan-gateway` pre-start script noise and local USB concentrator error
- external gateway traffic not being seen by ChirpStack (eventual root cause: wrong destination IP on slave gateways)

---

## 1) SSH to the host
```bash
ssh nube-io@10.8.1.17 -p 22
```

## 2) Initial platform health checks
```bash
hostname
date
systemctl list-units --type=service --all | grep -Ei 'lorawan|chirpstack|gateway|mosquitto'
ss -lunp | grep -E ':1700|:1701' || true
echo '<sudo-password>' | sudo -S docker ps --format 'table {{.Names}}\t{{.Status}}\t{{.Image}}'
```

## 3) Check ChirpStack Gateway Bridge logs and config
```bash
echo '<sudo-password>' | sudo -S docker logs --since 20m lorawan-complete-chirpstack-gateway-bridge-1 2>&1 | tail -n 120
echo '<sudo-password>' | sudo -S docker exec -i lorawan-complete-chirpstack-gateway-bridge-1 sh -c "cat /etc/chirpstack-gateway-bridge/chirpstack-gateway-bridge.toml"
```

## 4) Confirm gateways in ChirpStack DB
```bash
echo '<sudo-password>' | sudo -S docker exec -i lorawan-complete-postgresql-1 psql -U chirpstack_as -d chirpstack_as -c "\d gateway"
echo '<sudo-password>' | sudo -S docker exec -i lorawan-complete-postgresql-1 psql -U chirpstack_as -d chirpstack_as -c "select encode(mac,'hex') as gateway_id,name,first_seen_at,last_seen_at from gateway order by name;"
```

## 5) Fix MQTT listener binding (root cause of MQTT connect errors)
Observed issue: Mosquitto listener bound to `172.17.0.1:1883`, causing localhost clients / expected integrations to fail.

Update Mosquitto config so listener is on all interfaces:
- from: `listener 1883 172.17.0.1`
- to:   `listener 1883 0.0.0.0`

Then restart and validate:
```bash
echo '<sudo-password>' | sudo -S systemctl restart mosquitto
ss -ltnp | grep 1883
```

## 6) Fix `nubeio-lorawan-modbus-bridge` dependencies/runtime path
Observed issues:
- `socat` missing
- `/data/socat` directory missing

Commands used:
```bash
echo '<sudo-password>' | sudo -S apt-get update
echo '<sudo-password>' | sudo -S apt-get install -y socat
echo '<sudo-password>' | sudo -S mkdir -p /data/socat
echo '<sudo-password>' | sudo -S chown nube-io:nube-io /data/socat
echo '<sudo-password>' | sudo -S systemctl restart nubeio-lorawan-modbus-bridge
```

Validate:
```bash
journalctl -u nubeio-lorawan-modbus-bridge -n 200 --no-pager
ls -la /data/socat
```

Expected healthy signs:
- log contains: `Connected to MQTT Broker!`
- PTY symlinks exist under `/data/socat`

## 7) Remove stale `lorawan-gateway` pre-start script error
Observed noise:
- missing script `/home/pi/scripts/reset-usb-all.sh`

Create systemd override:
```bash
echo '<sudo-password>' | sudo -S mkdir -p /etc/systemd/system/lorawan-gateway.service.d
cat <<'EOF' | sudo tee /etc/systemd/system/lorawan-gateway.service.d/override.conf >/dev/null
[Service]
ExecStartPre=
ExecStartPre=/bin/sleep 2
EOF

echo '<sudo-password>' | sudo -S systemctl daemon-reload
echo '<sudo-password>' | sudo -S systemctl restart lorawan-gateway
systemctl status lorawan-gateway --no-pager -l
journalctl -u lorawan-gateway -n 60 --no-pager
```

Note:
- This removes pre-start script noise only.
- Service still fails if local concentrator device `/dev/ttyACM0` is not physically present.

## 8) Verify local USB concentrator status (separate issue)
```bash
ls -l /dev/ttyACM* /dev/ttyUSB* 2>/dev/null || true
ls -l /dev/serial/by-id 2>/dev/null || true
lsusb
```

If no `/dev/ttyACM0` exists, local packet forwarder failure is expected and unrelated to external gateways.

## 9) Verify incoming external gateway traffic (Semtech UDP)
```bash
echo '<sudo-password>' | sudo -S timeout 20 tcpdump -ni any udp port 1700 -vv -c 50
```

At fault time, captures showed no useful inbound gateway packets and DB `first_seen_at/last_seen_at` remained null.

## 10) Final root cause found
Root cause for external gateways not appearing in ChirpStack:
- slave gateways had incorrect destination IP configuration
- they were sending to the wrong server, not `10.8.1.17`

After correction on slave devices, run this verification:
```bash
ssh nube-io@10.8.1.17 -p 22
echo '<sudo-password>' | sudo -S timeout 15 tcpdump -ni any udp port 1700 -vv
echo '<sudo-password>' | sudo -S docker exec -i lorawan-complete-postgresql-1 psql -U chirpstack_as -d chirpstack_as -c "select encode(mac,'hex') as gateway_id,name,first_seen_at,last_seen_at from gateway where encode(mac,'hex') in ('0016c001f1435576','0016c001ff1f0b9e','0016c001ff1f0ba4') order by name;"
echo '<sudo-password>' | sudo -S docker logs --since 10m lorawan-complete-chirpstack-gateway-bridge-1 2>&1 | tail -n 200
```

Expected:
- UDP/1700 packets visible in capture
- `first_seen_at` and `last_seen_at` populated for the 3 gateways

---

## Quick checklist for next incident
1. Check service status and UDP/1700 listener.
2. Check gateway-bridge logs and MQTT connectivity.
3. Verify gateways in DB and `last_seen_at` timestamps.
4. Fix Mosquitto listener bind if MQTT errors occur.
5. Ensure `socat` installed and `/data/socat` exists.
6. Ignore/disable local USB gateway path if using external gateways only.
7. Run tcpdump on UDP/1700.
8. Validate slave gateway destination IP/port and gateway EUI mapping.
