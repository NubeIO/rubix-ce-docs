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

This should now create the network of the protocol that you selected. You can then **right-click** View to open to view
the **devices**

# Drivers Dependencies Overviews

In general all drivers need one app installed called **flow-framework**  (see **[Installing apps](../setup/plugins.md)** to install) , once **flow-framework** is installed each
driver needs a `Module/Plugin` (for more info on modules  **[Module/Plugin](../setup/plugins.md)**)

### BACnet master

:electric_plug: **Module/Plugin** required `bacnetmaster`

### BACnet Server

:black_square_button: **App** required `driver-bacnet`

### LoRa

:electric_plug: **Module/Plugin** required `lora`

:black_square_button: **App** required `driver-lora`

### LoRaWAN

:electric_plug: **Module/Plugin** required `lorawan`

:black_square_button: **Service** required `lorawan-gateway`

:black_square_button: **Service** required `lorawan-service`

### Modbus-RTU & Modbus-TCP

:electric_plug: **Module/Plugin** required `modbus`


### System

:electric_plug: **Module/Plugin** required `system`




