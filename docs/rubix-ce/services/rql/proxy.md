---
sidebar_position: 4
---

# Rubix-OS API

# Rubix-OS Proxy
As apart of RQL we provide a generic HTTP client to interact with ROS.

The main use case for the proxy is to give the RQL developer flexibility in being able to interact with ROS

- GET
- POST
- PUT
- PATCH
- DELETE

## HTTP Proxy Example
Perform a HTTP GET see types conversion: **[ros-types](../../services/rql/ros-types.md)**


```js
let apiGet = RQL.Get("rc", "points?with_priority=true");
let points = RQL.ToPoints(apiGet.Body());

let resp = {
  status: apiGet.Status(),
  points: points,
  count: points.length,
};

RQL.Result = resp;
```