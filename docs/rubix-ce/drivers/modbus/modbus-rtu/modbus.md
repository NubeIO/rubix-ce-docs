---
sidebar_position: 1
---

# Getting Started

Modbus Network

This article explains how to configure the Modbus Network within Rubix CE (Computer Edition). This will allow us the send and receive
Modbus data from connected Modbus devices.


## Adding a Modbus RTU Network

1. **Step-1** On the controller level, under `drivers`, click the **create** ![add icon](../../../img/apps/add-button.png) to select and download and install the relevant network. 
2. **Step-2** Select the **Modbus Network** . This will download the appropriate modules and drivers.
3. **Step-3** Configure the Modbus Network. Make sure that the parameters are same with the devices you will add on the network.
4. **Step-4** Once all the settings are added click on **Create Network** button. This should now create the Modbus and network. Now open the Modbus network to add a device.

![max800px](img/modbus-network.gif)

:::info
Important things to note before proceeding:
You must have a Rubix Compute and a Modbus RTU device and know the settings required to add the device **[ports](../../../../hardware/controllers/supervisors/rubix-compute/ports.md)**
:::


* **Network name** - The network name is the name of the desired network. It is recommended you use the type of Modbus
  communications (eg. LoRa® or RS485-1 / RS485-2).
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
  RS485-1/RS485-2 ports, use `/dev/tty/RS485-1` / `/dev/tty/RS485-2` RTU ports. respectively. For wireless Modbus-Over-LoRa® Network,
  use `/data/socat/serialBridge1`.
* **Max Poll Rate** (seconds) max polling rate.

## Adding a Modbus Device in the Network
1. **Step-1** On Modbus Network, under `drivers`, click the **create new device** ![add icon](../../../img/apps/add-button.png).
2. **Step-2** Fill out the details in the pop-up window with the correct information for the device you are adding. Ensure the Address ID is unique within the network. Click `Save` to confirm.

## Adding Points to the Modbus Device
1. **Step-1** Locate the device you want to add points to from the list under the Modbus network. Right-click to open its settings.
2. **Step-2** Click the **create new point** ![add icon](../../../img/apps/add-button.png).
3. **Step-3** Provide the necessary details in the pop-up window based on the device's manufacturer documentation for Modbus registers. Click the `Save` button to finalize.
