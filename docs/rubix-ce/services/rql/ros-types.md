---
sidebar_position: 5
---

# Rubix OS Types

As part of RQL we provide a methods to convert to ROS types. <br/>
For example we will use the RQL proxy to get the points from ROS and then convert them to a ROS type points.

Example: <br/>
In this example we perform an HTTP Proxy GET all points and then convert them into a **[points model](https://github.com/NubeIO/nubeio-rubix-lib-models-go/blob/master/pkg/v1/model/points.go#L198)** interface
```js
let apiGet = RQL.Get("rc", "points?with_priority=true");
let points = RQL.ToPoints(apiGet.Body());
```

## Networks

```
ToNetwork(body []byte) model.Network
```

```
ToNetworks(body []byte) []model.Network
```

## Devices

```
ToDevice(body []byte) model.Device
```

```
ToDevices(body []byte) []model.Device
```


## Points

```
ToPoint(body []byte) model.Point
```

```
ToPoints(body []byte) []model.Point
```



## Alerts

```
ToAlert(body []byte) model.Alert
```

```
ToAlerts(body []byte) []model.Alert
```


## Groups

```
ToGroup(body []byte) model.Group
```

```
ToGroups(body []byte) []model.Group
```
