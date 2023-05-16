---
sidebar_position: 6
---

# Modules

# Overview

**Modules/Plugins** are a way to extend the ability of flow-framework, for example rather than bloating the
rubix-compute with every feature or protocol's the user can add/remove **Modules/Plugins** as required.

The following features are supported

* Reading point values (sensors, logical)
* Writing to points, priority array supported
* Writing time schedules
* Mass control operations, for example mass updates of time schedules (Command Groups)
* Updates to the gateway app's

# A list of common Modules/Plugins

| Name         | Is a Protocol      | Supports <br/>Networks | Description                                                                   | Use Case                                             | 
|--------------|--------------------|------------------------|-------------------------------------------------------------------------------|------------------------------------------------------|
| system       | yes rest-api       | yes                    | a generic proxy network/devices/points that are not related to any protocol   | Schedules, proxy points                              | 
| lora         | yes LoRa           | yes                    | used with nube-io lora sensors                                                | When you want to use wireless sensors                | 
| lorawan      | yes LoRaWAN        | yes                    | used with any supported LoraWAN sensors                                       | When you want to add LoRaWAN sensors                 | 
| bacnetmaster | yes BACnet-Master  | yes                    | to read/write to BACnet device                                                | When you want to be a BACnet-master                  | 
| modbus       | yes Modbus RTU/TCP | yes                    | to read/write to Modbus device, can be either vai rs485 or modbus TCP         | When you want to be a Modbus-master                  | 
| history      | no                 | no                     | internal service for proving histories for points                             | When you want to have local or cloud historical data | 
| postgres     | no                 | no                     | send data into postgres (history plugin is needed to use the postgres plugin) | Used for edge to cloud histories for points          | 


# Rubix-Compute

The Rubix-Compute is the NubeIO gateway. It is a small wireless gateway capable of monitoring and controlling various
applications. For example, it can be used in building to control and monitor the heating, cooling and ventilation
systems.

# Modules (Plugins)

Modules (or Plugins) are software applications used to enable various functions on the Rubix Compute. Once controllers
have been installed on Rubix-Platform-CE (see here add link), modules will have to be installed to enable supported
functions such as Lora, Bacnet or Modbus communications.

![-](../img/apps/plugins-page.png)

## Install A Plugin

* To install a plugin toggle the button to the `on` position, then enable the plugin via the select and click on the button `enable plugin`
* To uninstall a plugin toggle the button to the `off` position 

:::info enable plugin
if a plugin isn't enabled you will get errors when trying to add the plugin
:::

:::info
this will not delete the network if you uninstall an plugin that was already installed
:::

![-](../img/apps/plugin-install.png)
