---
sidebar_position: 1
---

# Overview

# Rubix OS - Rubix Operating Stytem or ROS (open by firewall)
Rubix OS is the core runtime that runs either on the Rubix Compute or in the Nube-iO cloud.

## Performs tasks such as:
* Updating Rubix Compute apps, points, histories and/or network drivers
* Scheduling
* Connections to the Nube iO cloud
* Protocols such as LoRa, Modbus and/or BACnet

## Operates on hardware or Cloud Servers
Can operate either in the `cloud` or on a `Rubix-compute`.

## Ports

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


# Rubix Bios (open by firewall)
Rubix Edge is used to connect to the Rubix OS.

## Rubix Bios performs tasks such as:

* Updating Rubix OS.

## Operates on hardware or Cloud Servers
Operates in the `cloud` or on a `Rubix-compute`.

## Ports

Operateson port `http`
```
1659
```
Operates on port `https`
```
443
rb-YOURACCOUNT.nube-iiot.com
```

## Service Name
```
Sudo systemctl status nubeio-rubix-bios.
```

# Rubix Edge Wires - Wires (closed by firewall)
Rubix Edge Wires is a block logic Building Automation Control runtime for controlling HVAC equipment, lighting and creating function block logic programs.

## Wires Performs tasks such as

* BMS or DDC flow based programming.

## Operates on hardware or Cloud Servers
Operates in the `cloud` or on a `Rubix-compute`.

## Ports

Operates on port `http`
```
1665.
```

## Service Name
```
Sudo systemctl status nubeio-rubix-edge-wires.
```


# Other 3rd Party Services and Drivers

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
The LoRa driver is a wireless communication protocol for Nube iO LoRa sensors and other wireless devices.
Note: LoRa and LoRaWAN are not the same protocol. For 3rd Party LoRa sensors or devices, a LoRaWAN driver and gateway/reciver is required.

### Service Name
```
Sudo systemctl status driver-lora.
```

### Ports

n/a

## Rubix Compute iO Driver  (closed by firewall)
Rubix Compute iO Driver is a communication protocol for Input/Output (IO) hardware devices for Nube iO Rubix Compute iO.

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
A VPN service used for the Rubix Compute to communicate back to the `Nube iO Cloud`.

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
The MQTT broker is used for internal services.

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
The LoRaWAN driver is a wireless communication protocol for 3rd party LoRaWAN sensors and other wireless devices.
Note: LoRa and LoRaWAN are not the same protocol. For 3rd Party LoRa sensors or devices, a LoRaWAN driver and gateway/reciver is required.
Service for communication to the `LORA-CONNECT` plugged into a Rubix Compute via a `RJ12` plug and cable.

### Service Name
```
Sudo systemctl status lorawan-gateway. 
```

### Ports

Operates on port `udp`
```
tba
```

