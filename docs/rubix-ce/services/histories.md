---
sidebar_position: 2
---

# Histories

To trend data points from devices and sensors, including droplets, modbus and LoRaWAN devices:

If you have no points added please first add:
1. A network, then
2. A Device, and
3. A Point


Under the Drivers  section:  <br/>
Click the edit button on the point/s that you want to trend.  <br/>
* Check: 'history Enable'
* Check: 'auto mapping enable'


Select the History Type and History Interval:

History Type: <br/>
Interval: trends data at set time base
* COV (Change of value): trends data only when the point's value has changed
* COV and Interval: trends data at every set interval and change of values
* History Interval: How often the history trends


![histories-point-settings.png](img/histories-point-settings.png)


# Viewing Histories
You can either view a history directly from a point or from the `services/histories` tab.

## From a point

![history-from-point.gif](img/history-from-point.gif)


