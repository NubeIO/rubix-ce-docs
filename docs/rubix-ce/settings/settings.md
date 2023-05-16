---
sidebar_position: 1
---

# Settings

# Networking

## Default Network Configuration

When a Rubix Compute Controller is reset to factory defaults the two off Ethernet ports will be configured as follows:

| Port Name | Linux Port Name | Type  | IP            | Subnet        | Gateway      |
|-----------|-----------------|-------|---------------|---------------|--------------|
| ETH-1     | eth0            | Fixed | 192.168.15.10 | 255.255.255.0 | 192.168.15.1 |
| ETH-2     | eth1            | DHCP  | na            | na            | na           |

:::info
more info on [DHCP](https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol)
:::

## Changing the Rubix Compute's IP

1. On the 'device level' of the supervisor. Click into the device's 'settings' tab, then click the 'networking' tab.
   Click the notepad and wait for the pop-up.
2. Follow the wizard to set IP as either static or dynamic
3. The wizard will then prompt the user to reboot the controller Reboot the controller for the new IP to take into
   effect.

![max800px](img/ip-1.png)
![max800px](img/ip-2.png)

# Changing the Date / Time Settings

To update the rubix-compute date and time



![max800px](img/time-overview.png)

## Updating the Rubix Compute's time and date
Set the time and date as required

If the device has the internet by default it will auto update so you dont need to set the time/data <br/>
But you may need to update the `timezone`

![max800px](img/select-date.png)

## Updating the Time Zone

To set the Rubix-Computes’s click on the button and set the zone as required <br/>
The default timezone is `Australia/Sydney AEST`

![max800px](img/set-tz.png)

## Enabling / Disabling the NTP Service

To maintain your Rubix-Computes’s time, the operating system calls external servers to get the current time for your time zone.

![max800px](img/time-ntp.png)