---
sidebar_position: 1
---

# Networking

:::caution
Please note that the Rubix Compute will be rebooted after updating an IP address
:::

## Default Network Configuration

When a Rubix Compute is reset to its factory defaults, both Ethernet ports will be configured as follows:

| Port Name | Linux Port Name | Type  | IP            | Subnet        | Gateway      |
|-----------|-----------------|-------|---------------|---------------|--------------|
| ETH-1     | eth0            | Fixed | 192.168.15.10 | 255.255.255.0 | 192.168.15.1 |
| ETH-2     | eth1            | DHCP  | na            | na            | na           |

:::info
Additional info on [DHCP](https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol)
:::

## Changing the Rubix Compute IP address

1. On the 'device level' of the supervisor. Click into the device's 'settings' tab, then click the 'networking' tab.
   Click the notepad and wait for the pop-up to appear.
2. Follow the wizard to set the IP address as either static or dynamic.
3. The wizard will then prompt to reboot the Rubix Compute. Reboot the Rubix Compute to for the new IP address to be updated.

![max800px](img/ip-1.png)
![max800px](img/ip-2.png)


