---
sidebar_position: 1
---

# Overview

see more info for each protocol

- [BACnet master](bacnet/bacnet-master/bacnet-master.md)
- [BACnet Server](bacnet/bacnet-server/bacnet-server.md)
- [LoRa](lora/lora-raw/lora.md)
- [LoRaWAN](lora/lorawan/lorawan.md)
- [Modbus-RTU](modbus/modbus-rtu/modbus.md)
- [Modbus-TCP](modbus/modbus-tcp/modbus.md)
- [System-Network](system/overview.md)

# Drivers (Protocols)

To add a driver for a new network, return to the driver tab in the controller page. Select "+Create" and then select the
driver from the available list on the dropdown menu. If the required driver does not appear in the menu the plugin will
need to be installed, see previous section for instructions.

![max900px](./img/driver-page.png)

# Adding a network

**Step-1** On the controller level, under `drivers`, click the **create** ![add icon](../img/apps/add-button.png)

**Step-2** select the network you want to add, This will download and install the relevant network dependencies. Follow
the wizard to continue installing the network.

**Step-3** Once all the settings are added click on **Submit** button

This should now create the network of the protocol that you selected. You can then **right-click** Open to open to view
the **devices**

# Drivers Dependencies Overviews

In general all drivers need one app installed called **flow-framework**  (see **[Installing apps](../setup/plugins.md)** to install) , once **flow-framework** is installed each
driver needs a `Module/Plugin` (for more info on modules  **[Module/Plugin](../setup/plugins.md)**)


| Driver Name             | App Name      | Module/Plugin Name | Service Name                     |
|-------------------------|---------------|--------------------|----------------------------------|
| BACnet master           | na            | bacnetmaster       | na                               |
| BACnet Server           | driver-bacnet | na                 | na                               |
| LoRa                    | na            | lora               | na                               |
| LoRaWAN                 | na            | lorawan            | lorawan-gateway, lorawan-service |
| Modbus-RTU & Modbus-TCP | na            | modbus             | na                               |
| System                  | na            | system             | na                               |



# Exporting And Importing 

:::info
for compute rubix-compute backups see **[Installing apps](../setup/snapshots.md)**
:::

This section is for when the user wants to save Network, Device and Points from **Drivers**

For example to a backup of a device with its points and import into another device `rubix-compute`

## Perform a Backup

To back up a Network, Device or Points you can **right-click** **Export** and enter a comment, a comment should be something meaningful to you eg: common IO-16 points 

## Restore a Backup

To restore a back-up of a Network, Device or Points click on the **Import Button** and select the back-up you wish to import