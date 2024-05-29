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

## Drivers (Protocols)

To incorporate a Driver for a new network, go back to the Driver Tab within the controller page. Click on "+ Create", then pick the driver from the dropdown menu. If the necessary Driver isn't visible in the menu, you'll need to install the plugin as outlined in the previous section.

![max900px](./img/driver-page.png)

## Adding a Network

* **Step-1** Navigate to the controller level, then under `drivers`, click on the **create** ![add icon](../img/apps/add-button.png)
* **Step-2** Choose the network you wish to add. This action will initiate the download and installation of the necessary network dependencies. Follow the prompts in the wizard to complete the installation process.
* **Step-3** After all the settings are configured, click on the **Submit** button.

Proceed to generate the network for the chosen protocol. Afterward, simply **right-click** and select "Open" to view the **devices**.

## Drivers Dependencies Overviews

Typically, every driver requires the installation of an application called **flow-framework** (refer to **[Installing apps](../setup/plugins.md)** for instructions). Once **flow-framework** is installed, each driver needs a corresponding `Module/Plugin` (for further details on modules, check **[Module/Plugin](../setup/plugins.md)**).


| Driver Name             | App Name      | Module/Plugin Name | Service Name                     |
|-------------------------|---------------|--------------------|----------------------------------|
| BACnet master           | N/A           | BACnet Master      | N/A                              |
| BACnet Server           | Driver-BACnet | na                 | N/A                              |
| LoRa                    | N/A           | lora               | N/A                              |
| LoRaWAN                 | N/A           | LoRaWAN            | LoRaWAN Gateway, LoRaWAN Service |
| Modbus-RTU & Modbus-TCP | N/A           | Modbus             | N/A                              |
| System                  | N/A           | System             | N/A                              |



## Exporting And Importing 

:::info
To ensure a comprehensive backup of a Rubix Compute, refer to **[backups](../setup/snapshots.md)** for detailed instructions.
:::

This section is designed for users who wish to save a Network, Device, and Points from **Drivers**. <br/> 
For instance, it allows you to create a backup of a device along with its points and then import them into another device, such as a `Rubix Compute`.

### Perform a Backup

To back up a Network, Device, or Points, simply **right-click** on the item you wish to export, then select **Export**. You'll be prompted to enter a meaningful comment, such as "Common Rubix IO16 points", to ensure clarity.

### Restore a Backup

To restore a backup of a Network, Device, or Points, locate and click on the **Import Button**, then choose the backup file you wish to import.


### Point Write Modes

| Mode                   | Use case                                                                                                   | Description                                                                                                                                                   | 
|------------------------|------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Read only              | Mostly used for polling values                                                                             | Only Read Point Value Once                                                                                                                                   |
| Write once             | Used when you want fast network speeds                                                                     | Only Read Point Value (poll rate defined by setting)                                                                                                         |
| Write once read once   | Used on device such as a small thermostat where it has its own set-point so you dont want to override it | Write the value on COV, not Read                                                                                                                           |
| Write always           | Used when you want to write every poll                                                                     | Write the value on every poll (poll rate defined by setting)                                                                                                 |
| Write always then read |                                                                                                            | Write the value on COV, then read on each poll (poll rate defined by setting)                                                                                |
| Write and maintain     |                                                                                                            | Value written on COV, then read on each poll (poll rate defined by setting). <br/> If read value doesn't match written value, rewrite the value. |
