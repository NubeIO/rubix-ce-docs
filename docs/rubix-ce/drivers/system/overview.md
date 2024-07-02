---
sidebar_position: 1
---

# Overview

The system module serves a dual purpose within the system:

**Generic Points Driver**: This functionality enables the system module to handle points in a non-protocol-specific manner. It allows for the management and control of various types of points, such as sensors, actuators, and other devices, without being tied to a specific communication protocol.

**Time Schedules**: Additionally, the system module facilitates the implementation and management of time schedules. It provides the capability to define and execute schedules for various system operations, such as device activations, alarms, or data logging, based on specific time criteria.

## Adding a System Network

1. **Step-1** On the controller level, under `drivers`, click the **create** ![add-button](img/add-button.png) to select and download and install the relevant network. 
2. **Step-2** Select the **System Network** . This will download the appropriate modules and drivers.
3. **Step-3** Configure the System Network. Add the network name and description.
4. **Step-4** Once all the settings are configured click on **Create Network** button. This will now create the System network. Now open the System network to add a device.

![max800px](img/System-Network.gif) 

## Adding a Device in the Network
1. **Step-1** On System Network, under `drivers`, click the **create new device** ![add-button](img/add-button.png) .
2. **Step-2** Fill out the details in the pop-up window with the correct information for the device you are adding. Information such as device name and description. Click `Save` to confirm.

![max800px](img/System-Device.gif) 

## Adding Points to the Device
1. **Step-1** Locate the device you want to add points to from the list under the System Network. Right-click to open its settings.
2. **Step-2** Click the **create new point** ![add-button](img/add-button.png).
3. **Step-3** Provide the necessary details in the pop-up window. Click the `Save` button to finalize.

![max800px](img/System-Points.gif) 

**Name:** The identifier or label given to a specific data entity or parameter.

**Description:** A brief explanation or text that provides more details about the purpose, usage, or characteristics of the data or parameter.

**Data Type:**

* ***Digital:*** Represents data as binary states, typically 0 or 1.

* ***U-Int16, Int16:*** Unsigned and signed 16-bit integer, respectively.

* ***U-Int32, Int32:*** Unsigned and signed 32-bit integer, respectively.

* ***U-Int64, Int64:*** Unsigned and signed 64-bit integer, respectively.

* ***Float32, Float64:*** Single-precision and double-precision floating-point numbers, respectively.

* ***Mod10-U32:*** A specialized data type, likely referring to a 32-bit unsigned integer that adheres to a modulus 10 check (commonly used in checksum algorithms).

**Multiplication Factor:** A numeric value used to scale the raw input data, typically applied before any other adjustments like scaling or offset.

**Scale: Input/Device Min:** The minimum value expected or capable of being measured or received from the input or device.

**Scale: Input/Device Max:** The maximum value expected or capable of being measured or received from the input or device.

**Scale: Output/Point Min:** The minimum value to which the input data will be scaled or mapped in the output or point context.

**Scale: Output/Point Max:** The maximum value to which the input data will be scaled or mapped in the output or point context.

**Offset:** A fixed value added to the scaled input data to adjust or correct its representation.

**Round to Decimals:** Specifies the number of decimal places to which the data should be rounded after scaling and offset adjustments.

**Fallback:** Refers to the number of retries or attempts a device makes to establish communication or to perform an operation before it considers an action as unsuccessful.

**Unit:** Specifies the unit of measurement or representation associated with the data, such as degrees Celsius (°C), meters (m), or percentage (%), providing context to the numerical data.

**History Type** Determines how historical data is recorded or stored for the point.

**History Interval** Specifies the time interval between consecutive history samples recorded for the point. 

**History COV Threshold (Change of Value Threshold)** Sets the threshold value that triggers a change of value notification for historical records. When the object's value changes by an amount exceeding this threshold, a history update is recorded.

**Tags**               Right-click the network then `tags, meta-tags` to add in query key words                

**Meta-Tags**           Right-click the network then `tags, meta-tags` to add in query key words    

**Message**             See **[Troubleshooting](../../../setup/Troubleshoot.md)** for list of messages

**State**               Shows `ok` when a point is working in order, next to it is the time when the object has a non-empty last-fail property. Shows `error` when a point is not working in order, the time next to it is the time diff between now and the last fail was reported