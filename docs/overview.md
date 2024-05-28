---
sidebar_position: 1
---

## Rubix OS - Rubix Operating System or ROS (open by firewall)
Rubix OS serves as the core runtime platform that operates on either the Rubix Compute device or within the Nube-iO cloud environment.

### Rubix OS carries out various tasks including:
* Updating Rubix Compute apps, points, histories and/or network drivers
* Scheduling operations
* Establishing connections to the Nube iO cloud
* Support protocols such as LoRa, Modbus, and/or BACnet
* Rubix OS operates on both hardware and cloud servers. It can operate either within the `cloud` or on a `Rubix-compute` device.

### Ports

Operates on port `http`
```
1660
```
Operates on port `https`
```
ra-YOURACCOUNT.nube-iiot.com
```

## Service Name
```
Sudo systemctl status nubeio-rubix-os.
```

# Overview of ports normally opened for port-forwarding for remote access:

| Driver/Service Name | Service Name      | Port |                                                   | 
|---------------------|-------------------|------|---------------------------------------------------|
| Rubix-OS            | nubeio-rubix-os   | 1660 | Mandatory                                         | 
| Rubix-Bios          | nubeio-rubix-bios | 1659 | Mandatory                                         | 
| OpenVPN             | openvpn           | 443  | Optional but mandatory when using `Nube-IO-Cloud` | 
| lorawan-dashboard   | lorawan-server    | 8080 | Optional                                          | 


## Rubix Bios (open by firewall)
Rubix Edge is used to connect to the Rubix OS.

### Rubix Bios

* Performs updating Rubix OS.
* It can operate either within the `cloud` or on a `Rubix-compute` device.

### Ports

Operates on port `http`
```
1659
```
Operates on port `https`
```
443
rb-YOURACCOUNT.nube-iiot.com
```

### Service Name
```
Sudo systemctl status nubeio-rubix-bios.
```

## Rubix Edge Wires - Wires (closed by firewall)
Rubix Edge Wires is a block logic Building Automation Control runtime designed for managing HVAC equipment, lighting, and creating function block logic programs within building automation systems.

### Wires 

* BMS (Building Management System) or DDC (Direct Digital Control) flow-based programming.
* It can operate either within the `cloud` or on a `Rubix-compute` device.

### Ports

Operates on port `http`
```
1665.
```

### Service Name
```
Sudo systemctl status nubeio-rubix-edge-wires.
```


## <u> 3RD PARTY SERVICES & DRIVERS </u>

## BACnet Driver (open by firewall)
Communication protocol for `BACnet-master` and `BACnet-device`.

### Service Name
```
Sudo systemctl status driver-bacnet.
```

### Ports

Operates on port `udp`
```
47808
```

## LoRa Driver (closed by firewall)
The LoRa driver facilitates wireless communication for Nube iO LoRa sensors and other compatible wireless devices. <br/><br/>
Note: LoRa and LoRaWAN are distinct protocols. For third-party LoRa sensors or devices, a LoRaWAN driver and a gateway/receiver are necessary for integration.

### Service Name
```
Sudo systemctl status driver-lora.
```

### Ports

n/a

## Rubix Compute iO Driver  (closed by firewall)
The Rubix Compute IO Driver is a communication protocol tailored for Input/Output (IO) hardware devices specifically designed for Nube iO Rubix Compute IO.

### Service Name
```
Sudo systemctl status driver-rubix-compute-io. 
```

### Ports

Operates on port `http`
```
5001
```

## VPN (open by firewall)
A VPN service used for the Rubix Compute to establish communication back to `Nube iO Cloud`.

### Service Name
```
Sudo systemctl status openvpn.
```

### Ports

Operates on port `tls`
```
443
```

## MQTT broker (closed by firewall)
The MQTT broker is utilized for internal services within the system.

### Service Name
```
Sudo systemctl status mosquitto.
```

### Ports 

Operates on port `tcp`
```
1883
```

## LoRaWAN Dashboard (open by firewall)
Dashboard used for the administration of the loRaWAN server.

### Service Name
```
Sudo systemctl status lorawan-server. 
```

### Ports

Operates on port `http`
```
8080
```

## LoRaWAN Gateway/Driver (closed by firewall)
The LoRaWAN driver is a wireless communication protocol designed for 3rd party LoRaWAN sensors and other compatible wireless devices. <br/><br/>
NOTE: LoRa and LoRaWAN are distinct protocols. For 3rd Party LoRa sensors or devices, a LoRaWAN driver and a gateway/receiver are necessary for integration.
Connect `LORA-CONNECT` to Rubix Compute via the `RJ12` port to establish communication.

### Service Name
```
Sudo systemctl status lorawan-gateway. 
```

### Ports

Operates on port `udp`
```
tba
```

