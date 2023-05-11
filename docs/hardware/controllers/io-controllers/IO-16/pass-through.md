---
sidebar_position: 1
---


# Modbus Pass-through


# Introduction

In this example, we will be setting up a Rubix IO16 as a modbus pass-through device, turning the meter into a wireless solution.
We've chosen to use an EM115 MOD single phase modbus meter for this example, but the same principle applies to any modbus pass-through situations.

Link to energy meter manual here https://meters.co.uk/wp-content/uploads/2018/07/EM115-MOD.pdf

# Example

## Meter settings:
* Baud Rate: 9600
* Modbus Address: 1
* Parity: None


## Hardware setup - Rubix iO 16
The Modbus device's addressing is only required on the Rubix platform during modbus pass-though mode. 
The Rubix iO-16's address can be disregarded, so the dip switches on the left bank can be set all down `(but leave switch 8 up)`.
On the right bank of the Rubix iO-16, set the dip switch settings to match the meter's `baud rate (9600)` and `parity (None)`.

Also, remember to set the communication mode to pass-through mode. 

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


## add a modbus network
Network Name: (assign a network name)
* Type: RTU
* Delay between points (ms): 6000ms for IO modules in LoRa mode
* timeout: 1
* rtu parity: none
* rtu speed: 9600
* rtu stop-bits: 1
* rtu byte-size: 8
* rtu port: /data/socat/serialBridge1