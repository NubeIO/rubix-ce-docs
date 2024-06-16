---
sidebar_position: 1
---

# Getting Started

To add the BACnet-Master driver to a controller follow the steps in the previous sections: 

Modules (Modules/Plugins) and Drivers (Protocols).

When adding the BACnet driver the default settings should be suitable for most applications but can be changed if
required.

:::info Important things to note before proceeding:
* Install required **[modules/plugins](../../../setup/plugins.md)** **bacnetmaster**
:::


# Adding a BACnet Network

1. Open the host device you wish to add the BACnet network to
2. Click on the Add ![add-button.png](../../../img/apps/add-button.png)
3. Follow the steps in the wizard

![max800px](img/bacnet-add-network-whois.gif)

## Attributes


| Attribute   | Description                                       |
|-------------|---------------------------------------------------|
| Name        | Name of the network                               |
| Description | Description of the network, eg: `level 1 network` |

### Show Advanced Options

| Attribute         | Description                                                                             |
|-------------------|-----------------------------------------------------------------------------------------|
| Port              | Default port is `47808` you can also set it to another port like `47809` if required.    |
| Network interface | Select the network interface: <br/> - ETH-1 interface eth0 <br/> - ETH-2 interface eth1 |
| Max poll rate     | Set max polling rate.                                                                    |


# Editing a BACnet Network

1. You can either click on the **edit icon** ![edit icon](../../../../img/edit-icon.png) or **right-click** and **edit**
2. Update as required
3. To save hit the submit button


![max800px](img/bacnet-master-settings.png)

# Adding a BACnet Device

1. Open the network you added by **right-click** Open
2. Click on the Add ![add-button.png](../../../img/apps/add-button.png)
3. Enter the details required
4. To save hit the submit button


## BACnet Network Device Discovery (BACnet Who Is)

You can also do a BACnet device discovery to add the devices.

Enter into the BACnet tab and click on the **discover** icon.

![max800px](img/whois.gif)

## Adding BACnet Points to a device

### Add Manually

1. Open the BACnet device by **right-click** and **Open**
2. Click on the **add button** ![edit icon](../../../img/apps/add-button.png)
3. Enter the point details then save

### BACnet Network Points Discovery (BACnet Discover Device Objects)

You can also discover and add the BACnet points as required.

![max800px](img/discover-points.gif)

#### Point Settings

##### Poll  Priority

| Attribute | Description                        |
|-----------|------------------------------------|
| Name      | - High <br/> - Normal <br/>  - Low |


##### Poll Rate
Select the required poll rate.

:::info
**the time settings are set in the device settings**
:::

| Attribute | Description                         |
|-----------|-------------------------------------|
| Poll Rate | - Fast <br/> - Normal <br/>  - Slow |



## About BACnet

BACnet stands as a data communications protocol designed for Building Automation and Control Networks. It holds the status of an approved and standardized protocol by esteemed organizations such as the American Society of Heating, Refrigerating, and Air Conditioning Engineers (ASHRAE), the American National Standards Institute (ANSI), and the International Organization for Standardization (ISO). This protocol facilitates communication and control across various applications, including heating, ventilation, air-conditioning, lighting, access, and fire detection systems, along with their associated equipment.

## Supported Services

### Who Is

The BACnet: Who-Is Node allows you to broadcast a Who-Is message and await I-Am replies from BACnet compatible devices
on your network.

| Service                                | Supported |
|----------------------------------------|-----------|
| Who-Is (Device and Object Discovery)   | Yes       |
| I-Am (Device and Object Discovery)     | Yes       |
| Read-Property (Data Sharing)           | Yes       |
| Read-Property Multiple (Data Sharing)  | Yes       |
| Write-Property (Data Sharing)          | Yes       |
| Write-Property Multiple (Data Sharing) | Yes       |
| Subscribe COV                          | No        |

### Read Properties

BACnet point example:

| Object             | Number | Supported For Read |
|--------------------|--------|--------------------|
| Analog Input       | 0      | Yes                |
| Analog Output      | 1      | Yes                |
| Analog Value       | 2      | Yes                |
| Binary Input       | 3      | Yes                |
| Binary Output      | 4      | Yes                |
| Binary Value       | 5      | Yes                |
| Calendar           | 6      | No                 |
| Command            | 7      | No                 |
| Device             | 8      | No                 |
| Event Enrollment   | 9      | No                 |
| File               | 10     | No                 |
| Group              | 11     | No                 |
| Loop               | 12     | No                 |
| Multi-state Input  | 13     | Yes                |
| Multi-state Output | 14     | Yes                |
| Notification Class | 15     | No                 |
| Program            | 16     | No                 |
| Schedule           | 17     | No                 |
| Multi-state Value  | 19     | Yes                |

### Write Properties

BACnet point example:

| Object             | Number | Supported For Write |
|--------------------|--------|---------------------|
| Analog Input       | 0      | No                  |
| Analog Output      | 1      | Yes                 |
| Analog Value       | 2      | Yes                 |
| Binary Input       | 3      | No                  |
| Binary Output      | 4      | Yes                 |
| Binary Value       | 5      | Yes                 |
| Calendar           | 6      | No                  |
| Command            | 7      | No                  |
| Device             | 8      | No                  |
| Event Enrollment   | 9      | No                  |
| File               | 10     | No                  |
| Group              | 11     | No                  |
| Loop               | 12     | No                  |
| Multi-state Input  | 13     | No                  |
| Multi-state Output | 14     | Yes                 |
| Notification Class | 15     | No                  |
| Program            | 16     | No                  |
| Schedule           | 17     | No                  |
| Multi-state Value  | 19     | Yes                 |
