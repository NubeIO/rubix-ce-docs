---
sidebar_position: 1
---

# Overview

Rubix CE supports various network drivers, enabling seamless integration with industrial protocols. These drivers allow the system to communicate with different devices and systems for automation and control. Supported protocols include:

- [BACnet master](bacnet/bacnet-master/bacnet-master.md)
- [BACnet Server](bacnet/bacnet-server/bacnet-server.md)
- [LoRa®](lora/lora-raw/lora.md)
- [LoRaWAN®](lora/lorawan/lorawan.md)
- [Modbus-RTU](modbus/modbus-rtu/modbus.md)
- [Modbus-TCP](modbus/modbus-tcp/modbus.md)
- [System-Network](system/overview.md)


## Adding a Network Driver  

Follow these steps to add a new network driver in Rubix CE:

1. **Access the Controller**  
   - Navigate to the `host` and select the target controller.  

2. **Add a Driver**  
   - Open the `Drivers` tab and click on  `Create` ![add icon](../img/apps/add-button.png).  
   - Choose the required driver from the dropdown list.  
   - If the desired driver is not listed, ensure the required applications are installed. Refer to **[Installing Apps](../setup/apps.md)**.  

   ![max800px](./img/driver-page.png)

3. **Configure the Network**  
   - Follow the setup wizard to install dependencies and configure network settings.  

4. **Complete Setup**  
   - After configuring, click `Submit` to create the network.  
   - To manage devices within the network, right-click on the network and select `Open`.  

---

## Driver Dependencies  

Each driver requires specific applications and modules to function correctly. The table below outlines the dependencies:  

| **Driver Name**    | **App Name**   | **Module/Plugin Name** | **Service Name**              |
|--------------------|---------------|------------------------|------------------------------|
| BACnet Master     | N/A           | BACnet Master         | N/A                          |
| BACnet Server     | Driver-BACnet | N/A                    | N/A                          |
| LoRa®             | N/A           | LoRa                   | N/A                          |
| LoRaWAN®         | N/A           | LoRaWAN®               | LoRaWAN® Gateway, LoRaWAN® Service |
| Modbus-RTU & TCP  | N/A           | Modbus                 | N/A                          |
| System            | N/A           | System                 | N/A                          |

For more details on modules, refer to the **[Modules Guide](../setup/Modules.md)**.  

---

## Exporting and Importing Configurations  

Rubix CE allows users to export and import network, device, and point configurations for easy backup and restoration.  

- **Export Configuration**  
    
  - To create back up /  export a Network, Device, or Points,
   `Right-click` on the network -> device -> point you wish to export.  
  - Select `Export` and enter a description for clarity.  

- **Import Configuration**  
  - To restore / import a backup of a Network, Device, or Points, locate. Click `Import` and upload the desired configuration file.
  You'll be prompted to enter a meaningful comment, such as "Common Rubix IO16 points", to ensure clarity.  

For a full guide on backup and recovery, visit the **[backups](../setup/snapshots.md)** section.  

---

## Point Write Modes  

Rubix CE provides various point write modes for different operational needs:  

| **Mode**                     | **Description**                                            |
|-----------------------------|----------------------------------------------------------|
| **Read Only**                | Reads values but does not write any changes.             |
| **Write Once**               | Writes a value once but does not update further.         |
| **Write Once Read Once**     | Writes a value when changed but does not re-read.       |
| **Write Always**             | Continuously writes values on every poll cycle.         |
| **Write Always Then Read**   | Writes on change and reads values at each poll cycle.   |
| **Write and Maintain**       | Writes on change, reads on every poll, and rewrites if values differ. |

