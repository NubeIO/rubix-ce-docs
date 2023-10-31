---
sidebar_position: 1
---

# Overview

# Rubix-OS (open by firewall)
Rubix-OS is the core runtime that runs either on the Rubix-Compute or in the Nube-iO cloud


## performs tasks like:
* Updating Rubix-computes apps, points, histories and network drivers
* Scheduling
* Connections to the Nube-IO cloud
* Protocols like Lora, Modbus and BACnet


## runs on hardware
Runs in the `cloud` or on a `Rubix-compute`

## port

runs on port `http`
```
1660
```
runs on port `https`
```
ra-YOURACCOUNT.nube-iiot.com
```

## service name
```
sudo systemctl status nubeio-rubix-os
```

# Overview of ports normally opened for port-forwarding for remote access

| Driver/Service Name | Service Name      | Port |                                                   | 
|---------------------|-------------------|------|---------------------------------------------------|
| Rubix-OS            | nubeio-rubix-os   | 1660 | Mandatory                                         | 
| Rubix-Bios          | nubeio-rubix-bios | 1659 | Mandatory                                         | 
| OpenVPN             | openvpn           | 443  | Optional but mandatory when using `Nube-IO-Cloud` | 
| lorawan-dashboard   | lorawan-server    | 8080 | Optional                                          | 


# Rubix-Bios (open by firewall)
Rubix-Edge is used to connect to rubix-os

## performs tasks like

* Updating rubix-os


## runs on hardware
Runs in the `cloud` or on a `Rubix-compute`

## port

runs on port `http`
```
1659
```
runs on port  `https`
```
443
rb-YOURACCOUNT.nube-iiot.com
```

## service name
```
sudo systemctl status nubeio-rubix-bios
```

# Rubix-Edge-Wires (closed by firewall)
Rubix-Edge-Wires is a building automation control runtime for controlling HVAC equipment, lighting. Rubix-Edge-Wires uses a flow based programming runtime

## performs tasks like

* bms HVAC flow based programming


## runs on hardware
Runs in the `cloud` or on a `Rubix-compute`

## port

runs on port `http`
```
1665
```

## service name
```
sudo systemctl status nubeio-rubix-edge-wires
```


# Other 3rd party services and Drivers

## driver-bacnet (open by firewall)
Service for communication for `BACnet-master` and `BACnet-device`

### service name
```
sudo systemctl status driver-bacnet 
```

### port

runs on port `udp`
```
47808
```


## driver-lora (closed by firewall)
Service for communication for `LoRa` for Nube-iO LoRa sensors

### service name
```
sudo systemctl status driver-lora 
```

### port

na

## driver-rubix-compute-io  (closed by firewall)
Service for communication for `IO` for Nube-iO Rubix-Compute-IO

### service name
```
sudo systemctl status driver-rubix-compute-io 
```

### port

runs on port `http`
```
5001
```

## VPN (open by firewall)
VPN service used for the Rubix-Compute to communicate back to the `Nube-iO-Cloud`

### service name
```
sudo systemctl status openvpn 
```

### port

runs on port `tls`
```
443
```

## mqtt broker (closed by firewall)
The MQTT broker is used for internal services
### service name
```
sudo systemctl status mosquitto 
```

### port 

runs on port `tcp`
```
1883
```

## LoRaWAN Dashboard (open by firewall)
Dashboard used for the administration of the lorawan server

### service name
```
sudo systemctl status lorawan-server 
```

### port

runs on port `http`
```
8080
```


## LoRaWAN Gateway (closed by firewall)
Service for communication to the `LORA-CONNECT` plugged into the Rubix-Compute via the `RJ12` plug and cable

### service name
```
sudo systemctl status lorawan-gateway 
```

### port

runs on port `udp`
```
tba
```

