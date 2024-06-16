---
sidebar_position: 1
---
# Modbus TCP
## Getting Started

This article explains how to configure the Modbus TCP within Rubix CE. This will allow us the send and receive
Modbus data from connected Modbus devices.


## Adding a Modbus TCP Network

1. **Step-1** On the controller level, under `drivers`, click the **create** ![add icon](../../../img/apps/add-button.png) to select and download and install the relevant network. 
2. **Step-2** Select the **Modbus Network** . This will download the appropriate modules and drivers.
3. **Step-3** Configure the Modbus Network. Make sure that the parameters are same with the devices you will add on the network.
4. **Step-4** Once all the settings are added click on **Create Network** button. This should now create the Modbus and network. Now open the Modbus network to add a device.

:::info
Important things to note before proceeding:
You must have a Rubix Compute and a modbus RTU device and know the settings required to add the device
**[ports](../../../../hardware/controllers/supervisors/rubix-compute/ports.md)**
:::

There should be a Modbus Network for Modbus Devices connecting via Ethernet/Networked to this Rubix device. We recommend
naming this network based on the device that you are connecting to. See below explanation of what each of these
settings pertain to.

* **Network** name - Name related to the Modbus Device/Gateway you are connecting to.
* **Type** - TCP
* **Enable** - Ticked
* **Delay between points** (ms) - 60
* **Timeout** - 1
* **IP** - IP address of the Device/Gateway you are connecting to
* **Port** - Modbus Port of the Device/Gateway you are connecting to (this is a number)

## Adding a Modbus Device in the Network
1. **Step-1** On Modbus Network, under `drivers`, click the **create new device** ![add icon](../../../img/apps/add-button.png).
2. **Step-2** Fill out the details in the pop-up window with the correct information for the device you are adding. Ensure the Address ID is unique within the network. Click `Save` to confirm.

## Adding Points to the Modbus Device
1. **Step-1** Locate the device you want to add points to from the list under the Modbus network. Right-click to open its settings.
2. **Step-2** Click the **create new point** ![add icon](../../../img/apps/add-button.png).
3. **Step-3** Provide the necessary details in the pop-up window based on the device's manufacturer documentation for Modbus registers. Click the `Save` button to finalize.