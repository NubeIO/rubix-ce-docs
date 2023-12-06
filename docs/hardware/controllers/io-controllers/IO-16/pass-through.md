---
sidebar_position: 1
---


# Modbus Pass-through


# Introduction

Pass through mode is used to connect any Modbus RS485 networks together wirelessly over LoRa. It can connect any number over wired RS485 networks together as long as there are no conflicting addresses. It can also support up to the normal amount of Modbus slave devices of 247 with just one Rubix IO.
Since the Rubix Compute and Rubix IO16 are communicating over LoRa, their baud rates are independent of one another and do not have to match. <br/>

The Rubix IO in pass-through mode should match the other devices on the RS485 network it is connected to. 

Example: A Modbus power meter is on address 2, baud rate 9600, the Rubix IO should be set to baud rate 9600. <br/>
When creating the Modbus network on the client/platform, the baud rate should be set to 38400 as this is the required setting for the Rubix Compute.


# Example

## Meter settings:

| **Attribute**  | **Setting Value** | 
|----------------|-------------------|
| Baud Rate      | 9600              | 
| Modbus Address | 1                 | 
| Parity         | None              | 


## Hardware setup - Rubix IO16

- The Modbus device's addressing is only required on the Rubix platform during modbus pass-though mode. 
- The Rubix IO16's address can be disregarded, so the dip switches on the left bank can be set all down `(but leave switch 8 up)`.
- On the right bank of the Rubix IO16, set the dip switch settings to match the meter's `baud rate (9600)` and `parity (None)`.

Also, remember to set the communication mode to pass-through mode. 

:::info
More info on Rubix IO dips switch: **[settings](parameters.md#dip-switch-configuration)**
:::

| **Left Bank Switch** | **Position** | **Function**      |
|----------------------|--------------|-------------------|
| 1                    | Down         | Modbus Addressing |
| 2                    | Down         | Modbus Addressing |
| 3                    | Down         | Modbus Addressing |
| 4                    | Down         | Modbus Addressing |
| 5                    | Down         | Modbus Addressing |
| 6                    | Down         | Modbus Addressing |
| 7                    | Down         | Modbus Addressing |
| 8                    | **Up**       | Always Up         |


| **Right Bank Switch** | **Position** | **Function**             |
|-----------------------|--------------|--------------------------|
| 1                     | Down         | Comm Mode                |
| 2                     | **Up**       | Comm Mode (pass-through) |
| 3                     | **Up**       | Baud Rate (9600)         |
| 4                     | Down         | Baud Rate                |
| 5                     | Down         | Baud Rate                |
| 6                     | Down         | Parity                   |
| 7                     | Down         | Parity                   |
| 8                     | **Up**       | Always Up                |


## Adding a Modbus network
Network Name: (assign a network name)
* Type: RTU
* Delay between points (ms): 6000ms for Rubix IO modules in LoRa mode
* timeout: 1
* rtu parity: none
* rtu speed: 38400
* rtu stop-bits: 1
* rtu byte-size: 8
* rtu port: /data/socat/serialBridge1
