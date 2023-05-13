---
sidebar_position: 1
---

# Settings

# Networking

## Default Network Configuration

When a Rubix Compute Controller is reset to factory defaults the 2 x Ethernet ports will be configured as follows:

| Port Name | Linux Port Name | Type  | IP            | Subnet        | Gateway      |
|-----------|-----------------|-------|---------------|---------------|--------------|
| ETH-1     | eth0            | Fixed | 192.168.15.10 | 255.255.255.0 | 192.168.15.1 |
| ETH-2     | eth1            | DHCP  | na            | na            | na           |

## Changing the Rubix Compute's IP

1. On the 'device level' of the supervisor. Click into the device's 'settings' tab, then click the 'networking' tab.
   Click the notepad and wait for the pop-up.
2. Follow the wizard to set IP as either static or dynamic
3. The wizard will then prompt the user to reboot the controller Reboot the controller for the new IP to take into
   effect.

![max800px](img/ip-1.png)
![max800px](img/ip-2.png)

# Changing the Date / Time Settings

![max800px](img/time-overview.png)

## Updating the Rubix Compute's time and date

![max800px](img/select-date.png)

## Updating the Time Zone

![max800px](img/set-tz.png)

## Enabling / Disabling the NTP Service

![max800px](img/time-ntp.png)