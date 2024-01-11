---
sidebar_position: 3
---

# Inbuilt RQL Functions

To use an in built RQL function we need to use the key work `RQL` followed by `.` and the function name we wish to call.

Example
```
RQL.Date()
```

Working example, run this and the debug will return the current date when the script is called
```
RQL.Result = RQL.Date()
```

# Alerts

## Get Alerts
Get all the alerts from the supervisor
```
GetAlerts() any
```

## Add Alert
Add a new alert to a host
```
AddAlert(hostIDName string, body any)
```

### Example

```
let body = {
hostUUID: "hos_c8ab2fe07e7a413c",
entityType: "device",
type: "ping",
status: "active",
severity: "crucial",
};

let alert = RQL.AddAlert("hos_c8ab2fe07e7a413c", body);

RQL.Result = alert.CreatedAt;
```

## Update Alert Status
Update an alert

```
UpdateAlertStatus(hostIDName, uuid, status string) any
```

# Date

## Sleep
Time delay of the rule loop

```
Sleep(duration int)
```


## Time Date
TimeDate returns time/date formatted as `2006.01.02 15:04:05`

```
TimeDate() string 
```

## Time
Time returns time formatted as `15:04:05`

```
Time() string 
```

## Date
Date returns date formatted as `2006.01.02`

```
Date() string 
```

# Hosts and Groups

## Get Groups
Get all the groups from a supervisor

```
GetGroups() any
```

## Get All Hosts Status
Get all the hosts status

```
GetAllHostsStatus() any
```

## Get Hosts Status
Get all the hosts status from group

```
GetHostsStatus(groupUUID string) any
```

## Get Rule Logs
Get all the logs that have been stored in a rule that is set to run at an interval


```
GetRuleLogs(uuidName string) any 
```

### Return Body

```
[
  {
    Result: 3,
    Time: "2023-10-17T09:05:21.556313433-05:00",
    Timestamp: "Tue, 17 Oct 2023 09:05:21 -05",
  },
  {
    Result: 6,
    Time: "2023-10-17T09:05:23.570618144-05:00",
    Timestamp: "Tue, 17 Oct 2023 09:05:23 -05",
  }
]
```

### Example
get the first log and its value. The script name is `test`
```
RQL.Result = RQL.GetRuleLogs("test")[0].Result;
```

# Numbers

## R and Int
RandInt returns a random int within the specified range.

```
RandInt(range1, range2 int) int
```

## R and Float
RandFloat returns a random float64 within the specified range.

```
RandFloat(range1, range2 float64) float64
```

## Limit To Range
LimitToRange returns the input value clamped within the specified range

```
LimitToRange(value float64, range1 float64, range2 float64) float64 
```

## Round To
RoundTo returns the input value rounded to the specified number of decimal places.


```
RoundTo(value float64, decimals uint32) float64 
```

## Scale
Scale returns the (float64) input value (between inputMin and inputMax) scaled to a value between outputMin and outputMax
```
Scale(value, inMin, inMax, outMin, outMax float64) float64
```

# Networking

## Ping
Ping ping an list of IP address eg: ["192.168.15.1", "192.168.15.2"]
```go
type PingResult struct {
	Ip string `json:"ip"`
	Ok bool   `json:"ok"`
}
```

```
Ping(ipList []string) []PingResult 
```

# RQS Points

## Get Points
Get all the points from a host by passing in the name or uuid

```
GetPoints(hostIDName string) any
```

## Get Point
Get a point from a host by passing in the name or uuid, and the point uuid

```
GetPoint(hostIDName, uuid string) any 
```

## Write Point Value Priority
Write a point value from a host by passing in the name or uuid, and the point uuid, the priority value and the write value

```
WritePointValuePriority(hostIDName, uuid string, pri int, value float64) any 
```

# RQL Variables
Variables are added from the Rubix CE UI

returned result of a variable
```
{
  Name: "test",
  Password: "",
  UUID: "rql_2b0065e41311",
  Variable: 1234.0,
}
```
## Example
to get a variable value by its name
```js
RQL.Result = RQL.GetVariable("test").Variable;
```

## Get Variables
Get all the variables that where added to the RQl database

```
GetVariables() any 
```

## Get Variable
Get a variable by its name or its uuid

```
GetVariable(uuidName string) any 
```


## Update Variable Value
Update a variable by its name or its uuid

```
UpdateVariableValue(uuidName string, value any) any 
```

