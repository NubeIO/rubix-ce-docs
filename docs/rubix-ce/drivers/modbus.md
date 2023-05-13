---
sidebar_position: 6
---

# Modbus

Modbus Network

This article explains how to configure the Modbus Network within Rubix-CE. This will allow us the send and receive
Modbus data from connected Modbus devices.

## Adding a network

**Step-1** On the controller level, under `drivers`, click the **create** ![add icon](../img/apps/add-button.png) to
select and download and install the relevant network. Follow the wizard to continue installing the network.

**Step-2** Select the **Modbus Serial Network** or **Modbus TCP Network**. This will download the appropriate modules
and drivers.

Check the default communication settings for the sensor by ticking the 'show advanced options' checkbox.

**Step-3** Once all the settings are added click on **Submit** button

This should now create the Modbus and network. Now open the Modbus network to add a device

## Adding a Modbus RTU Network

:::info
Important things to note before proceeding:
You must have a rubix-compute and a modbus RTU device and know the settings required to add the device *
**[ports](../../hardware/controllers/supervisors/rubix-compute/ports.md)**
:::

* **Network name** - The network name is the name of the desired network. It is recommended you use the type of modbus
  communications (eg. LoRa or RS485-1 / RS485-2).
* **Enable** - Tick to enable the Modbus Network.
* **Delay between points (ms)** - This is the minimum time (in milliseconds) between the individual Modbus poll requests.
* **Serial Timeout** - This is the time (in seconds) that the Modbus Service will wait for a response from the Modbus Device before
  moving on to the next Modbus poll.
* **RTU parity** - (RTU ONLY) Parity setting must match for all devices on the Modbus Network.
* **RTU speed** - (RTU ONLY) This is the BAUD RATE setting. Baud Rate setting must match for all devices on the Modbus
  Network.
* **RTU stop-bits** - (RTU ONLY) Stop Bit setting must match for all devices on the Modbus Network.
* **RTU byte-size** - (RTU ONLY) Byte Size setting must match for all devices on the Modbus Network.
* **RTU port** - (RTU ONLY) Select from the dropdown the serial port that is used for the Modbus Network. For
  RS485-1/RS485-2 ports, use `/dev/tty/RS485-1` / `/dev/tty/RS485-2` RTU ports. respectively. For wireless Modbus-Over-LoRa Network,
  use `/data/socat/serialBridge1`.
* **Max Poll Rate** (seconds) max polling rate
