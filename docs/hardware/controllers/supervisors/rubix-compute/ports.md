---
sidebar_position: 4
---
# Networking and Interfaces

![max500px](img/rc-networking.png)

# Networking

| Port Name | Linux Port Name | Type  | IP            | Subnet        | Gateway      |
|-----------|-----------------|-------|---------------|---------------|--------------|
| ETH-1     | eth0            | Fixed | 192.168.15.10 | 255.255.255.0 | 192.168.15.1 |
| ETH-2     | eth1            | DHCP  | na            | na            | na           |


# RS485 ports

| Port Name         | Serial Port Name |
|-------------------|------------------|
| 485-1             | /dev/ttyUSB0     |
| 485-2 and support | /dev/ttyAMA0     |


# LoRa for Droplet, Micro-Edge and Rubix IO

| Port Name | Serial Port Name  |
|-----------|-------------------|
| LoRa      | /data/socat/loRa1 |


# Modbus Over LoRa For the Rubix IO

| Port Name | Serial Port Name          |
|-----------|---------------------------|
| LoRa      | /data/socat/serialBridge1 |


# Summery

| **Device Type**                          | **LoRa Port selection on Rubix Platform** |
|------------------------------------------|-------------------------------------------|
| Wireless sensors - Droplets & Micro Edge | /data/socat/loRa1                         |
| Rubix IO16 in Wireless Mode             | /data/socat/serialBridge1                 |
| Rubix IO16 in 485 Mode                  | /dev/ttyAMA0                              |
