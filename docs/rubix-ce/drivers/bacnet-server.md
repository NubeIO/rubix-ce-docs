---
sidebar_position: 2
---

# BACnet Server

BACnet Server Integration (make the Rubix Compute a discoverable BACnet device)

:::info
Important things to note before proceeding:
Install the BACnet app see link: **[installing apps](../setup/apps.md)** and install the **driver-bacnet** app
:::

:::info
make sure the config is set for the number of AIs and AOs needed. (eg 2x 16s we would need to add in the bacnet-config
16-AIs and 16-AOs)
:::


![max800px](img/bacnet-config.gif)


:::info Important things to note before proceeding
please make sure the correct ethenet port is select.
* ETH-1 is would be set for iface eth0
* ETH-2 is would be set for iface eth1
:::

1. On the 'device level' of the supervisor. Click into the device's 'settings' tab, then click the 'BACnet Config' tab.
2. Click the 'edit' button to see all the configurable fields (server name, BACnet ports, device ID etc)
3. Click the 'Ok' button and refresh for the changes to update. 