---
sidebar_position: 1
---

# Overview

This IoT multi-gateway will collect data from both wired and wireless devices.
It will enable you to aggregate data from multiple sensors and send it anywhere – your cloud, a local server, or
3rd-party hardware.

![rc5.png](../../../img/rc5.png)

## One Gateway. Multiple Data Types.

Rubix Compute is a one of a kind IoT gateway that aggregates all types of building data, removing the frustration of
running multiple gateways in one solution.

* Integrate into any BMS via BACnet/IP
* Has flow-based programming environment for BMS programing
* Receive wireless signals
* LoRa® & LoRaWAN®
* Convert Modbus & BACnet to wireless
* Has onboard rest-api

## Overview of specs

* 1GB of RAM
* 8GB of onboard storage

## Overview of interfaces

![rc-overview.png](img/rc-overview.png)

* 2x ethernet ports
* 2x rs485 ports
* 2x RJ12 ports
* 1x USB port

## Overview of protocols

* BACnet-sever (Run the rubix-compute as a BACnet-Device over BACnet/IP)
* BACnet-master (Run the rubix-compute as a BACnet-Client over BACnet/IP to read and write to other BACnet devices)
* Modbus Master
* LoRaWAN Gateway and Server
* LoRa Gateway (For nube-sensors and IO-controllers)

# Mounting

The Rubix Compute 5 is designed to be mounted on electrical DIN rail. It can be mounted vertically or horizontally. The
controller should always be mounted in a location such that it will not experience very high or low temperatures,
liquids or high humidity.

![mounting.png](img/mounting.png)

# IO add on modules

Up to 4x [IO-16s](../../io-controllers/IO-16/overview.md) can be plugged into the right-side of the IO-16

To communicate with the IO-16s you have two options
1. Add a modbus-RTU network
2. Or add a BACnet-server node in [rubix-wires](../../../../rubix-ce/wires/bacnet.md)

:::danger modbus networks conflict
You cant add a modbus network and the BACnet-server node in rubix-wires, Its one or the other
:::


![rc-with-io16s.png](img/rc-with-io16s.png)