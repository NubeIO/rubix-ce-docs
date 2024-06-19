---
sidebar_position: 9
---
# Troubleshooting

## Device Offline

Rubix CE can detect if a device is offline. To check the availability of the device, navigate to the Host View.
![max800px](../img/apps/is-online.png) <br/>
Click ![update-status-button.png](../img/apps/update-status-icon.png) to update the current online/offline status of the devices.

:::info Device Offline
<b>Network Downtime: </b> Network signal is poor or nonexistent, the on-site engineer is advised to take the following steps to ensure connectivity: <br/>
<ul><li>Check on the router's reception indicator.</li>
<li>Restart the problematic device or check if the router is working correctly.</li>
<li>Inspect the SIM integrity.</li></ul>
:::

## System Performace
If **Rubix CE** experiences performance issues, you can diagnose potential causes by accessing system information in the `Info` section under `settings`. This information includes CPU usage, memory usage, swap memory usage, and disk usage. analysing these metrics can help pinpoint the source of performance degradation and guide troubleshooting efforts to address the underlying issues.

![max800px](../img/apps/info.png)

## Plugin Not Enabled or No Valid message from the Network
* If a network is highlighted in orange, scroll right to identify potential issues. In this example, the error message indicates either the plugin is not enabled or there's no valid message from the network.
![max800px](../img/apps/plug-in-unable.png)
* You will need to confirm that the module is installed correctly, the app is enabled, and functioning properly. For instructions on navigating through apps and modules, please refer to   **[modules](Modules.md)** and  **[apps](apps.md)** respectively.
![max800px](../img/apps/plug-in-unable-2.png)
* In the image above, observe that BacNet is currently activating. This can be the reason why the plugin is is highlighted in orange. 
* Restart the driver to refresh the connection. See if problem still persists.
* Sometimes, even if the plugin is enabled, errors persist due to incorrect parameters. Ensure that the parameters configured in your driver match those of the devices you're attempting to connect to. You can edit the these parameters at the drivers tab. See **[drivers](../drivers/overview.md)** and select the driver you wanted to explore.

## Rubix Host/Supervisor Level Troubleshooting
* Initiate a ping to the Host/Supervisor by right-clicking on it as shown in the image below:
![max800px](../img/apps/Ping.png)
* After confirming connectivity with the host/supervisor, authenticate by right-clicking and selecting `Login`.
* Once logged in, verify the presence of Rubix-OS. If it is not installed, you can install it by right-clicking on Rubix-OS and selecting `Install`.
* Additionally, for troubleshooting purposes, you can restart Rubix-OS from the right-click menu, which can resolve issues on problematic systems. Restarting Rubix-OS can help resolve various issues by resetting its state and clearing temporary glitches or errors that may have occurred during operation. 


