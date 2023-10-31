---
sidebar_position: 1
---

# Getting Started

## Download And Install Rubix-CE
Rubix-CE is the engineering tool used to program the Nube-iO BMS products. See the link to download [**link**](../rubix-ce/setup/download.md)


## Hardware Required
To complete the quick start we need some basic hard
- [**Rubix-Compute**](../hardware/controllers/supervisors/rubix-compute/overview.md)
- [**IO-16**](../hardware/controllers/io-controllers/IO-16/overview.md)
- Ethernet Cat-5 cable and network access or an ethernet port on your PC
- 24vdc power supply to power the rubix-compute


:::info
if you don't an ethernet port on your PC don't worry as the 2nd ethernet port on the Rubix-Compute is set to **DHCP**
:::


## Setup of hardware

1. Power the [**Rubix-Compute**](../hardware/controllers/supervisors/rubix-compute/overview.md)
2. Plugin the `IO-16` into the side of the `Rubix-Compute` (This will power the IO-16, and the `default modbus address` of the IO-16 is `address-1`)
3. Use the ethernet cable and plug it into the 2nd port of the rubix-compute for DHCP or the 1st port for a fix IP address of `192.168.15.10`

:::tip
[**Rubix-Compute Power Connection**](../hardware/controllers/supervisors/rubix-compute/power.md) <br/>
[**IO-16 Modbus Address**](../hardware/controllers/io-controllers/IO-16/parameters.md#dip-switch-configuration) 
:::

## Programming the Rubix-Compute
### Run Rubix-CE
Once the software is downloaded you can run the software (there is no install process)

### Install Rubix-OS & Adding A Supervisor

:::tip
`Rubix-OS` is the core operating system (OS) that runs on the Rubix-Compute
:::

:::tip
A `Supervisor` is a concept where Rubix-OS can manage/supervisor multiple Rubix-Computes <br/>
A `Supervisor` can either be a single Rubix-Compute or a `Nube-iO` cloud account running `Rubix-OS`
:::

1. [**Add Token**](../rubix-ce/setup/getting-started.md#add-token)
2. [**Adding A Supervisor**](../rubix-ce/setup/supervisor.md)

## Set up the Rubix-Compute as a BACnet/IP Device
This will allow any BACnet-Master device to read/write the IO on the IO-16 controller

:::info
See [**Apps for more info**](../rubix-ce/setup/apps.md) <br/>
See [**BACnet for more info**](../rubix-ce/drivers/bacnet/bacnet-server/bacnet-server.md) 
:::

1. Install App `rubix-edge-wires`
2. Install App `driver-bacnet`
3. Set the BACnet device-id and how many IO-16s you want to add. (In this demo it will be one IO-16)


:::tip
See [**Full BACnet tutorial**](bacnet-device.md)
:::