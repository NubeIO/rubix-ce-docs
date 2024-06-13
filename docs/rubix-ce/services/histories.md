---
sidebar_position: 2
---

# Histories

To trend data points from devices and sensors, including droplets, Modbus, and LoRaWAN® devices, follow these steps:

1. **Add a Network**: Begin by adding a network. This serves as the overarching framework for connecting and managing your devices and sensors.

2. **Add a Device**: Once the network is set up, add the specific device from which you want to collect data. This could be a droplet, Modbus device, LoRaWAN® device, or any other compatible device.

3. **Add a Point**: After adding the device, proceed to add the individual data points that you wish to trend or monitor. These points represent the specific measurements or values you want to track, such as temperature, pressure, or humidity.

Once you've completed these steps and have points added, you can begin trending the data by accessing the histories or logging functionality. This allows you to visualise and analyse the historical data trends from your devices and sensors over time.

## Enabling History
To enable trending for specific points under the Drivers section, follow these steps:

1. Navigate to the `Drivers` section in `Rubix CE`.

2. Right-click the network where the point you want to trend is located. Click on the `edit` button.

3. In the editing interface, check the following options:
- `History Enable`: This option enables historical data logging for the selected point(s), allowing you to track and analyse past data trends.
- `Auto Mapping Enable`: This option enables automatic mapping for the selected point(s).
3. In the editing interface, check the `History Enable` checkbox. `Click save`.

![histories-point-settings.png](img/history-enable-1.png)

4. Do the same steps 2-3 above, this time instead of network, do this on the device.

5. Open the device, select the point you wish to trend, right click then edit.  Enable history for the point and save the changes.


By checking these options, you ensure that the selected points will be included in the historical data logging process and are ready for trending and analysis within Rubix CE.


## History Type and History Interval

History Type:

**COV (Change of value)**: Select this option if you want to trend data only when the point's value has changed. This helps in capturing data trends efficiently, especially when there are significant changes in the values.<br/>

**COV and Interval**: Choose this option if you want to trend data at every set interval and also when the point's value changes. This provides a comprehensive view of data trends, capturing both regular updates and significant changes. <br/><br/>
**History Interval**:This setting determines how often the history trends occur.<br/>
<br/>If you've selected Interval or COV and Interval for the History Type, specify the desired interval for trending data.
For example, if you set the History Interval to 1 hour, data will be trended every hour.<br/>



![histories-point-settings.png](img/histories-point-settings.png)


## Viewing Histories

**From the services/histories Tab**: You can access history data from the services/histories tab. This tab provides a centralized location for viewing and managing historical data from multiple points or devices within your environment. It offers a comprehensive overview of historical trends and allows for easy navigation and analysis of past data records.


![history-from-point.gif](img/history-from-point.gif)


**Direct from point**: You also has an option to view the history data from the point itself.
![history-from-point.gif](img/history-point.gif)