---
sidebar_position: 1
---

# Getting Started

Modbus Network

This article explains how to configure the Modbus Network within Rubix CE. This will allow us the send and receive
Modbus data from connected Modbus devices.


## Adding a Modbus TCP Network

:::info
Important things to note before proceeding:
You must have a Rubix Compute and a modbus RTU device and know the settings required to add the device
**[ports](../../../../hardware/controllers/supervisors/rubix-compute/ports.md)**
:::

There should be a Modbus Network for Modbus Devices connecting via Ethernet/Networked to this Rubix device. We recommend
naming this network based on the device that you are connecting to. See above for an explanation of what each of these

settings pertain to.

* **Network** name - Name related to the Modbus Device/Gateway you are connecting to.
* **Type** - TCP
* **Enable** - Ticked
* **Delay between points** (ms) - 60
* **Timeout** - 1
* **IP** - IP address of the Device/Gateway you are connecting to
* **Port** - Modbus Port of the Device/Gateway you are connecting to (this is a number)
