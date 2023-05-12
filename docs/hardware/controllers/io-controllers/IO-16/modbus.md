---
sidebar_position: 5
---


# Modbus RS485 Wiring

Nube-iO Rubix IO Modules are a pure Modbus device; All communications with the IO Modules are via Modbus.  
This article will detail the correct wiring for the Modbus RS485 Network.  
To communicate via Modbus the Rubix IO Module must also have its Onboard DIP Switches configured correctly to set the Modbus Serial Communication Parameters.

# Connecting RS485 Network (Wired Network)
When using the wired network connection, the IO Module RS485 Modbus connection is used.  

When Networking multiple Nube-iO iO Modules on an RS485 network, each controller is
connected in a `Daisy Chain`. Controllers that are connected between 2 other controllers
will have 2 wires (one from the previous controller and one from the next controller) in the
same terminal. Ensure A/+ and B/- wires are kept consistent for all controllers on the
network.

The connector is terminated and installed as shown below.

![modbus-connection.png](img/modbus-connection.png)


| Pin       |
|-----------|
| Pin 1 (+) |
| Pin 2 (-) |
| Pin 3 (G) |


## Serial Ports On the Rubix-Compute

| Port Name         | Serial Port Name |
|-------------------|------------------|
| 485-1             | /dev/ttyUSB0     |
| 485-2 and support | /dev/ttyAMA0     |

