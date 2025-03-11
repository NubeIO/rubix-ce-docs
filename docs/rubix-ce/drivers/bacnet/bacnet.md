---
sidebar_position: 1
---

# BACnet Overview

## About BACnet

BACnet stands as a data communications protocol designed for Building Automation and Control Networks. It holds the status of an approved and standardized protocol by esteemed organizations such as the American Society of Heating, Refrigerating, and Air Conditioning Engineers (ASHRAE), the American National Standards Institute (ANSI), and the International Organization for Standardization (ISO). This protocol facilitates communication and control across various applications, including heating, ventilation, air-conditioning, lighting, access, and fire detection systems, along with their associated equipment.

## BACnet Object IDs

| Object           | Number | Description                                                                 |
|-----------------------|------------|-----------------------------------------------------------------------------|
| Analog Input          | 0          | Represents a continuously variable physical input, such as temperature or humidity. |
| Analog Output         | 1          | Controls an analog output, such as a variable-speed fan or dimmable lighting. |
| Analog Value          | 2          | Stores and processes analog values for calculations or logic operations.     |
| Binary Input          | 3          | Represents a digital (on/off) input, such as a switch or sensor.             |
| Binary Output         | 4          | Controls a digital (on/off) output, such as a relay or actuator.             |
| Binary Value          | 5          | Stores and processes binary values for logical operations.                  |
| Calendar              | 6          | Defines date-based schedules for automation processes.                      |
| Command               | 7          | Executes predefined commands or sequences.                                  |
| Device                | 8          | Represents a BACnet device and its associated properties.                   |
| Event Enrollment      | 9          | Manages event-based notifications and alerts.                               |
| File                  | 10         | Represents a file object used for data storage and transfer.                |
| Group                 | 11         | Groups multiple objects for simplified control and monitoring.              |
| Loop                  | 12         | Represents a control loop for process control applications.                 |
| Multi-state Input     | 13         | Represents an input with multiple discrete states.                          |
| Multi-state Output    | 14         | Controls an output that has multiple states.                                |
| Notification Class    | 15         | Manages notifications and alarms for BACnet objects.                        |
| Program               | 16         | Represents executable logic, such as scripts or automation routines.        |
| Schedule              | 17         | Defines time-based automation schedules for devices.                        |
| Multi-state Value     | 19         | Stores and processes values with multiple discrete states.                  |


## BACnet Common Property's

| Property Name  | Number |
|---------------|--------|
| objectName    | 77     |
| presentValue  | 85     |
| priorityArray | 87     |
| device        | 8      |

## BACnet Common Property's for a Device

| Property Name            | Device | Identifier | Description                                                                 |
|--------------------------|----------|------------|-----------------------------------------------------------------------------|
| `objectList`             | 8    | 76         | Lists all objects that belong to the device.                                |
| `deviceName`             | 8    | 77         | The human-readable name of the device.                                      |
| `manufacturer`           | 8    | 121        | The name of the device manufacturer.                                        |
| `manufacturer-id`        | 8    | 120        | A unique identifier assigned to the manufacturer.                           |
| `segmentationSupported`  | 8    | 107        | Indicates whether the device supports segmentation.                         |
| `maxApduLengthAccepted`  | 8    | 62         | Specifies the maximum APDU size the device can process.                     |


## BACnet Property's

| Property Name                  | Number |
|--------------------------------|--------|
| ackedTransitions               | 0      |
| ackRequired                    | 1      |
| action                         | 2      |
| actionText                     | 3      |
| activeText                     | 4      |
| activeVtSessions               | 5      |
| alarmValue                     | 6      |
| alarmValues                    | 7      |
| all                            | 8      |
| allWritesSuccessful            | 9      |
| apduSegmentTimeout             | 10     |
| apduTimeout                    | 11     |
| applicationSoftwareVersion     | 12     |
| archive                        | 13     |
| bias                           | 14     |
| changeOfStateCount             | 15     |
| changeOfStateTime              | 16     |
| notificationClass              | 17     |
| none                           | 18     |
| controlledVariableReference    | 19     |
| controlledVariableUnits        | 20     |
| controlledVariableValue        | 21     |
| covIncrement                   | 22     |
| datelist                       | 23     |
| daylightSavingsStatus          | 24     |
| deadband                       | 25     |
| derivativeConstant             | 26     |
| derivativeConstantUnits        | 27     |
| description                    | 28     |
| descriptionOfHalt              | 29     |
| deviceAddressBinding           | 30     |
| deviceType                     | 31     |
| effectivePeriod                | 32     |
| elapsedActiveTime              | 33     |
| errorLimit                     | 34     |
| eventEnable                    | 35     |
| eventState                     | 36     |
| eventType                      | 37     |
| exceptionSchedule              | 38     |
| faultValues                    | 39     |
| feedbackValue                  | 40     |
| fileAccessMethod               | 41     |
| fileSize                       | 42     |
| fileType                       | 43     |
| firmwareRevision               | 44     |
| highLimit                      | 45     |
| inactiveText                   | 46     |
| inProcess                      | 47     |
| instanceOf                     | 48     |
| integralConstant               | 49     |
| integralConstantUnits          | 50     |
| issueConfirmedNotifications    | 51     |
| limitEnable                    | 52     |
| listOfGroupMembers             | 53     |
| listOfObjectPropertyReferences | 54     |
| listOfSessionKeys              | 55     |
| localDate                      | 56     |
| localTime                      | 57     |
| location                       | 58     |
| lowLimit                       | 59     |
| manipulatedVariableReference   | 60     |
| maximumOutput                  | 61     |
| maxApduLengthAccepted          | 62     |
| maxInfoFrames                  | 63     |
| maxMaster                      | 64     |
| maxPresValue                   | 65     |
| minimumOffTime                 | 66     |
| minimumOnTime                  | 67     |
| minimumOutput                  | 68     |
| minPresValue                   | 69     |
| modelName                      | 70     |
| modificationDate               | 71     |
| notifyType                     | 72     |
| numberOfAPDURetries            | 73     |
| numberOfStates                 | 74     |
| objectIdentifier               | 75     |
| objectList                     | 76     |
| objectName                     | 77     |
| objectPropertyReference        | 78     |
| objectType                     | 79     |
| optional                       | 80     |
| outOfService                   | 81     |
| outputUnits                    | 82     |
| eventParameters                | 83     |
| polarity                       | 84     |
| presentValue                   | 85     |
| priority                       | 86     |
| priorityArray                  | 87     |
| priorityForWriting             | 88     |
| processIdentifier              | 89     |
| programChange                  | 90     |
| programLocation                | 91     |
| programState                   | 92     |
| proportionalConstant           | 93     |
| proportionalConstantUnits      | 94     |
| protocolConformanceClass       | 95     |
| protocolObjectTypesSupported   | 96     |
| protocolServicesSupported      | 97     |
| protocolVersion                | 98     |
| readOnly                       | 99     |
| reasonForHalt                  | 100    |
| recipient                      | 101    |
| recipientList                  | 102    |
| reliability                    | 103    |
| relinquishDefault              | 104    |
| required                       | 105    |
| resolution                     | 106    |
| segmentationSupported          | 107    |
| setpoint                       | 108    |
| setpointReference              | 109    |
| stateText                      | 110    |
| statusFlags                    | 111    |
| systemStatus                   | 112    |
| timeDelay                      | 113    |
| timeOfActiveTimeReset          | 114    |
| timeOfStateCountReset          | 115    |
| timeSynchronizationRecipients  | 116    |
| units                          | 117    |
| updateInterval                 | 118    |
| utcOffset                      | 119    |
| vendorIdentifier               | 120    |
| vendorName                     | 121    |
| vtClassesSupported             | 122    |
| weeklySchedule                 | 123    |





# Debugging


## Wireshark/Tshark

### Tshark

Install
```
sudo apt-get install tshark
```

Usage 
```
sudo tshark -i eth0 -f "udp" | grep "BACnet-APDU"
```

## Ping Port 47808
Check and see if port 47808 is open on your target device.
```
Netcat -v -u -z 192.168.15.155 47808
```
