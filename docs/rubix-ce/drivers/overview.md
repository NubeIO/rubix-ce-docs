---
sidebar_position: 1
---

# Overview
See more info for each protocol:

- [BACnet master](bacnet/bacnet-master/bacnet-master.md)
- [BACnet Server](bacnet/bacnet-server/bacnet-server.md)
- [LoRa](lora/lora-raw/lora.md)
- [LoRaWAN](lora/lorawan/lorawan.md)
- [Modbus-RTU](modbus/modbus-rtu/modbus.md)
- [Modbus-TCP](modbus/modbus-tcp/modbus.md)
- [System-Network](system/overview.md)

# Drivers (Protocols)

To add a Driver for a new network, return to the Driver Tab in the controller page. Select "+ Create" and then select the
driver from the available list on the dropdown menu. If the required Driver does not appear in the menu the plugin will
need to be installed, see previous section for instructions.

![max900px](./img/driver-page.png)

# Adding a Network

* **Step-1** On the controller level, under `drivers`, click the **create** ![add icon](../img/apps/add-button.png)
* **Step-2** select the network you want to add, This will download and install the relevant network dependencies. Follow the wizard to continue installing the network.
* **Step-3** Once all the settings are added click on **Submit** button

This should now create the network of the protocol that you selected. You can then **right-click** `Open` to view the **devices**

# Drivers Dependencies Overviews

In general all drivers need one app installed called **flow-framework**  (see **[Installing apps](../setup/plugins.md)** to install) , once **flow-framework** is installed each
driver needs a `Module/Plugin` (for more info on modules  **[Module/Plugin](../setup/plugins.md)**)


| Driver Name             | App Name      | Module/Plugin Name | Service Name                     |
|-------------------------|---------------|--------------------|----------------------------------|
| BACnet master           | N/A           | BACnet Master      | N/A                              |
| BACnet Server           | Driver-BACnet | na                 | N/A                              |
| LoRa                    | N/A           | lora               | N/A                              |
| LoRaWAN                 | N/A           | LoRaWAN            | LoRaWAN Gateway, LoRaWAN Service |
| Modbus-RTU & Modbus-TCP | N/A           | Modbus             | N/A                              |
| System                  | N/A           | System             | N/A                              |



# Exporting And Importing 

:::info
For complete backup of a Rubix Compute see **[backups](../setup/snapshots.md)**
:::

This section is for when the user wants to save a Network, Device and Points from **Drivers** <br/>
For example, to create a backup of a device with its points and import into another device `Rubix Compute`

## Perform a Backup

To backup a Network, Device or Points you can **right-click** **Export** and enter a comment, a comment should be something meaningful to you eg: Common Rubix IO16 points.

## Restore a Backup

To restore a backup of a Network, Device or Points click on the **Import Button** and select the back-up you wish to import.


# Point Write Modes

| Mode                   | Use case                                                                                                   | Description                                                                                                                                                   | 
|------------------------|------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Read only              | Mostly used for polling values                                                                             | Only Read Point Value Once                                                                                                                                   |
| Write once             | Used when you want fast network speeds                                                                     | Only Read Point Value (poll rate defined by setting)                                                                                                         |
| Write once read once   | Used on device such as a small thermostat where it has its own set-point so you dont want to override it | Write the value on COV, don't Read                                                                                                                           |
| Write always           | Used when you want to write every poll                                                                     | Write the value on every poll (poll rate defined by setting)                                                                                                 |
| Write always then read |                                                                                                            | Write the value on COV, then Read on each poll (poll rate defined by setting)                                                                                |
| Write and maintain     |                                                                                                            | Write the value on COV, then Read on each poll (poll rate defined by setting) <br/> If the Read value does not match the Write value, Write the value again |
