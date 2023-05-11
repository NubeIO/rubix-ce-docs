---
sidebar_position: 3
---

# BACnet Master

## about

BACnet is a data communications protocol for Building Automation and Control Networks. It is an approved and
standard protocol by American Society of Heating, Refrigerating and Air Conditioning Engineers (ASHRAE),
American National Standards Institute (ANSI), and International Organization for Standardization (ISO). The
BACnet protocol supports communication and control of applications such as heating, ventilation, air-conditioning, lighting, access, and fire detection systems and their associated equipment.

## supported services

### whois

The BACnet: Who-Is Node allows you to broadcast a Who-Is message and await I-Am replies from BACnet-compatible devices on your network.

| Service                                | Supported |
| -------------------------------------- | --------- |
| Who-Is (Device and Object Discovery)   | yes       |
| I-Am (Device and Object Discovery)     | yes       |
| Read-Property (Data Sharing)           | yes       |
| Read-Property Multiple (Data Sharing)  | yes       |
| Write-Property (Data Sharing)          | yes       |
| Write-Property Multiple (Data Sharing) | yes       |
| Subscribe COV                          | no        |

### read properties

For example for a BACnet point

| Object             | Number | Supported For Read |
| ------------------ | ------ | ------------------ |
| Analog Input       | 0      | yes                |
| Analog Output      | 1      | yes                |
| Analog Value       | 2      | yes                |
| Binary Input       | 3      | yes                |
| Binary Output      | 4      | yes                |
| Binary Value       | 5      | yes                |
| Calendar           | 6      | no                 |
| Command            | 7      | no                 |
| Device             | 8      | no                 |
| Event Enrollment   | 9      | no                 |
| File               | 10     | no                 |
| Group              | 11     | no                 |
| Loop               | 12     | no                 |
| Multi-state Input  | 13     | yes                |
| Multi-state Output | 14     | yes                |
| Notification Class | 15     | no                 |
| Program            | 16     | no                 |
| Schedule           | 17     | no                 |
| Multi-state Value  | 19     | yes                |

### write properties

For example for a BACnet point

| Object             | Number | Supported For Write |
| ------------------ | ------ | ------------------- |
| Analog Input       | 0      | no                  |
| Analog Output      | 1      | yes                 |
| Analog Value       | 2      | yes                 |
| Binary Input       | 3      | no                  |
| Binary Output      | 4      | yes                 |
| Binary Value       | 5      | yes                 |
| Calendar           | 6      | no                  |
| Command            | 7      | no                  |
| Device             | 8      | no                  |
| Event Enrollment   | 9      | no                  |
| File               | 10     | no                  |
| Group              | 11     | no                  |
| Loop               | 12     | no                  |
| Multi-state Input  | 13     | no                  |
| Multi-state Output | 14     | yes                 |
| Notification Class | 15     | no                  |
| Program            | 16     | no                  |
| Schedule           | 17     | no                  |
| Multi-state Value  | 19     | yes                 |
