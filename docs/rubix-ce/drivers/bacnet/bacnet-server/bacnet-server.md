---
sidebar_position: 2
---

# Getting Started

BACnet Server Integration (make the Rubix Compute a discoverable BACnet device.

:::info Important things to note before proceeding:
* Install required **[apps](../../../setup/apps.md)** **driver-bacnet**
:::


:::info
Make sure the config is set for the number of AIs and AOs needed. (eg 2x **[Nube-IO IO-16](../../../../hardware/controllers/io-controllers/IO-16/overview.md)** we would need to add in the bacnet-config
16-AIs and 16-AOs)
:::


:::info rubix-wires bacnet-server node
To make the Rubix Compute a native BACnet device please see link: **[bacnet](../../../wires/bacnet.md)** 
:::

See below for installing the BACnet-driver and editing the sever settings

![max800px](img/bacnet-config.gif)

## BACnet Server Settings

![config.png](img/config.png)


:::info Important things to note before proceeding
please make sure the correct ethernet port is select.
* ETH-1 is would be set for `iface` `eth0`
* ETH-2 is would be set for `iface` `eth1`
:::

1. On the `device level` of the supervisor. Click into the device's `settings` tab, then click the `BACnet Config` tab.
2. Click the `edit` button to see all the configurable fields (server name, BACnet ports, device ID etc)
3. Click the `Ok` button and refresh for the changes to update. 