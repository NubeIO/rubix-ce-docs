---
sidebar_position: 1
---

# Getting Started

This page will demonstrate how to add wireless LoRa® Droplets and Micro Edges to the Rubix Compute.
The Rubix Compute is a LoRa® Gateway/Reciever. 

## Adding a LoRa® Network

:::info Important things to note before proceeding:
* Install required **[apps](../../../setup/apps.md)** **driver-LoRa®**
* Install required **[modules](../../../setup/Modules.md)** **LoRa®** 
:::

| Attribute   | Description                                       |
|-------------|---------------------------------------------------|
| Name        | Name of the network                               |
| Description | Description of the network, eg: `level 1 network` |
|Enable               |Enable the network                                                                     |
| Serial Port              | A dropdown menu to choose the port where the Lora Network is connected.    |
| Serial Baudrate | A dropdown menu to choose speed at which data is transmitted over a serial communication interface |
|History Enable     | Enable network history                                                                    |
|Tags               | Right-click the network then `tags, meta-tags` to add in query key words                    |
|Meta-Tags          | Right-click the network then `tags, meta-tags` to add in query key words                   |
|Message            | See **[Troubleshooting](../../../setup/Troubleshoot.md)** for list of messages|
|State              | Shows `ok` when the network is working in order, next to it is the time when the object has a non-empty last-fail property. Shows `error` when the network is not working in order, the time next to it is the time diff between now and the last fail was reported|

1. **Step-1** On the controller level, under `drivers`, click the **create** ![add icon](../../../img/apps/add-button.png) to select and download and install the relevant network. Follow the wizard to continue installing the LoRa® network.
2. **Step-2** Select the LoRa® network. This will download the appropriate modules and drivers.
3. **Step-3** Once all the settings are added click on **Submit** button This should now create the LoRa® and network. Now open the LoRa® network to add a device.

:::info
Adding the LoRa® driver for the first time it will install a module dependency called `LoRa®`.
:::

## Summary Of Ports When Adding a Network

Depending on the LoRa® network use case the correct serial-port must be selected.

![max800px](img/ports.png)


| **Device Type**                          | **LoRa® Port selection on Rubix Platform** |
|------------------------------------------|-------------------------------------------|
| Wireless Sensors - Droplets & Micro Edge | /data/socat/loRa1                         |
| Rubix iO 16 in Wireless Mode             | /data/socat/serialBridge1                 |
| Rubix iO 16 in 485 Mode                  |                             |



![max800px](img/adding-lora-network.gif)

## Adding a LoRa® Sensor

:::info
See Nube iO supported sensors and gateways for more info **[sensors](../../../../hardware/sensors/droplets/droplets-v1/Downloads.md)**  & **[gateway](../../../../hardware/sensors/micro-edge/MicroEdge-V2/Downloads.md)** 
:::

Sensor Models

| Sensor Model | Supports Temperature | Supports Humidity | Supports Motion | Supports Lux |  
|--------------|----------------------|-------------------|-----------------|--------------|
| THLM         | Yes                  | Yes               | Yes             | Yes          | 
| THL          | Yes                  | Yes               | No              | Yes          |  
| TH           | Yes                  | Yes               | No              | No           |  
|Microedge      |No                     |No                 |No            |No|

1. **Step-1** Once inside the `network`, click the **create** ![add icon](../../../img/apps/add-button.png) button and a pop-up will give you the type of sensors to select from. For this example, we will be using a `THLM` Droplet.
2. **Step-2** Follow the wizard to assign a name and description. Ensure to click `Show advanced options` and enable `Auto mapping` before submitting.
3. **Step-3** Enter the 8 digit serial number printed on the sensor and press submit.
4. **Step-4** Once the sensor has been added, view the points by right clicking the newly added device.

![max800px](img/adding-lora-droplet.gif)


:::info
It may be necessary to wait or force a push from the sensor (by clicking the reset button on the sensor) for the values
to show. Additional offsets, scaling fallback values, multiplication factors can also be applied if required. Try also
clicking the 'refresh' button if the values do not update.
:::


