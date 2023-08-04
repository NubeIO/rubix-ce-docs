---
sidebar_position: 1
---

# BACnet overview

## Object IDs

| Object             | Number |
|--------------------|--------|
| Analog Input       | 0      |
| Analog Output      | 1      |
| Analog Value       | 2      |
| Binary Input       | 3      |
| Binary Output      | 4      |
| Binary Value       | 5      |
| Calendar           | 6      |
| Command            | 7      |
| Device             | 8      |
| Event Enrollment   | 9      |
| File               | 10     |
| Group              | 11     |
| Loop               | 12     |
| Multi-state Input  | 13     |
| Multi-state Output | 14     |
| Notification Class | 15     |
| Program            | 16     |
| Schedule           | 17     |
| Multi-state Value  | 19     |

## Common Property's

| PropertyName  | Number |
|---------------|--------|
| objectName    | 77     |
| presentValue  | 85     |
| priorityArray | 87     |
| device        | 8      |

## Common Property's for a device

| PropertyName          | Device | Number |
|-----------------------|--------|--------|
| objectList            | 8      | 76     |
| deviceName            | 8      | 77     |
| manufacture           | 8      | 121    |
| manufacture-id        | 8      | 120    |
| segmentationSupported | 8      | 107    |
| maxApduLength         | 8      | 62     |

## Property's

| PropertyName                   | Number |
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


## wireshark/tshark

### tshark

install
```
sudo apt-get install tshark
```

usage 
```
sudo tshark -i eth0 -f "udp" | grep "BACnet-APDU"
```

## ping port 47808
check and see if port 47808 is open on your target device
```
netcat -v -u -z 192.168.15.155 47808
```
