---
sidebar_position: 2
---

# Alerts

## GetAlerts
Get all the alerts from the supervisor
```
GetAlerts() any
```

## AddAlert
Add a new alert to a host
```
AddAlert(hostIDName string, body any)
```

### example

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

## UpdateAlertStatus
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


## TimeDate
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

## GetGroups
Get all the groups from a supervisor

```
GetGroups() any
```

## GetAllHostsStatus
Get all the hosts status

```
GetAllHostsStatus() any
```

## GetHostsStatus
Get all the hosts status from group

```
GetHostsStatus(groupUUID string) any
```

# Rule Logs
Get all the logs that have been stored in a rule that is set to run at an interval

```go
type RuleLogsResponse struct {
	Result []storage.Result
	Error  string
}
```

```
GetRuleLogs(uuidName string) *RuleLogsResponse 
```

# Numbers

## RandInt
RandInt returns a random int within the specified range.

```
RandInt(range1, range2 int) int
```

## RandFloat
RandFloat returns a random float64 within the specified range.

```
RandFloat(range1, range2 float64) float64
```

## LimitToRange
LimitToRange returns the input value clamped within the specified range

```
LimitToRange(value float64, range1 float64, range2 float64) float64 
```

## RoundTo
RoundTo returns the input value rounded to the specified number of decimal places.

```
RoundTo(value float64, decimals uint32) float64 
```

## Scale
Scale returns the (float64) input value (between inputMin and inputMax) scaled to a value between outputMin and outputMax
```
Scale(value, inMin, inMax, outMin, outMax float64) float64
```
