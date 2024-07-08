---
sidebar_position: 6
---

# Example RQL script



# How to use

- Copy, paste and modify example script.

# Examples

1. [Alerts](#1-alerts)
    1. [Gateway Offline Alerts](#i-gateway-offline-alerts)
    2. [Sensor Offline Alerts](#ii-sensor-offline-alerts)
    3. [Sensor Flat Line/NoData Alerts](#iii-sensor-flatlinenodata-alerts)
    4. [High/Low Threshold Alerts](#iv-highlow-threshold-alerts)
2. [Filter with Tags/MetaTags](#2-filter-with-tagsmetatags)
    1. [Points filter with Tags/MetaTags](#i-points-filter-with-tagsmetatags)
    2. [Histories filter with Tags/MetaTags](#ii-histories-filter-with-tagsmetatags)
3. [Histories metrics(Count,Sum,Avg,Min,Max)](#3-histories-metricscountsumavgminmax)

***

## 1. Alerts

> Alerts:
>    - EntityType: `gateway`,`network`, `device`, `point` and `service`.
>    - Type: `ping`, `fault`, `threshold` and `flat-line`.
>    - Severity: `crucial`,`minor`,`info` and `warning`.
>

### i. Gateway Offline Alerts

<details><summary><u><i>Show script</i></u></summary>

```js
let result = [];

groups = RQL.ROS.GetGroups();

for (let group of groups) {
    try {
        hostStatusResult = RQL.ROS.UpdateHostsStatus(group?.UUID);
        for (let host of hostStatusResult?.Hosts) {
            if (host.PingFailCount > 0) {
                alert = {
                    HostUUID: host.UUID,
                    EntityType: "gateway",
                    Type: "ping",
                    Status: "active",
                    Severity: "crucial",
                    Title: "gateway offline",
                    Body: `host: ${host.Name}, ping-fail-count: ${host.PingFailCount}`,
                    Tags: [
                        {
                            tag: "ping",
                        },
                    ],
                };

                alertResult = RQL.AddAlert(alert.HostUUID, alert);
                result.push(alertResult);
            }
        }
    } catch (_) {
    }
}

RQL.Result = result.length > 0 ? result : "no alerts";
```

</details>

### ii. Sensor Offline Alerts

<details><summary><u><i>Show script</i></u></summary>

```js
let result = [];
let networks = [];
const connectionErrorMessage = "Connection error";

function addAlert(hostUUID, entityType, type, severity, title, body, tags = []) {
    alert = {
        HostUUID: hostUUID,
        EntityType: entityType,
        Type: type,
        Status: "active",
        Severity: severity,
        Title: title,
        Body: body,
        Tags: tags,
    };
    try {
        res = RQL.AddAlert(alert.HostUUID, alert);
        result.push(res);
    } catch (ex) {
    }
}

hosts = RQL.ROS.GetHosts();
for (let host of hosts) {
    opts = {
        Args: {
            WithDevices: true,
            WithPoints: true,
        },
        HostUUID: host.UUID,
    };
    try {
        networks = RQL.ROS.GetNetworks(opts);


        for (let network of networks) {
            body = `host: ${host.Name}, network: ${network.Name}`;
            if (network.Enable == false) {
                addAlert(host.UUID, "network", "fault", "info", "network offline", `${body} is disabled`);
                continue;
            }

            for (let device of network.Devices) {
                body = `${body}, device: ${device.Name}`;
                if (device.Enable == false) {
                    addAlert(host.UUID, "device", "fault", "info", "device disabled", `${body} is disabled`);
                    continue;
                }

                for (let point of device.Points) {
                    body = `${body}, point: ${point.Name}, address-uuid: ${point.AddressUUID}`;
                    if (point.Enable == false) {
                        addAlert(host.UUID, "point", "fault", "info", "point disabled", `${body} is disabled`);
                        continue;
                    }

                    if (point.Message.includes(connectionErrorMessage)) {
                        addAlert(host.UUID, "point", "ping", "crucial", "sensor offline", `${body} is offline`);
                        continue;
                    }
                }
            }
        }
    } catch (ex) {
    }
}

RQL.Result = result.length > 0 ? result : "no alerts";

```

</details>

### iii. Sensor FlatLine/NoData Alerts

<details><summary><u><i>Show script</i></u></summary>

```js
let result = [];
const hour = 1;
const serverHostUUID = "hos_b1f62bf4358443de";

function addAlert(hostUUID, entityType, entityUUID, type, severity, title, body, tags = []) {
    try {
        alert = {
            HostUUID: hostUUID,
            EntityUUID: entityUUID,
            EntityType: entityType,
            Type: type,
            Status: "active",
            Severity: severity,
            Title: title,
            Body: body,
            Tags: tags,
        };
        res = RQL.AddAlert(alert.HostUUID, alert);
        result.push(res);
    } catch (_) {
    }
}

function getNHoursBeforeNow(n) {
    const now = new Date();
    now.setTime(now.getTime() - n * 60 * 60 * 1000);
    return now.toISOString();
}

function isFlatLine(data = []) {
    if (data.length === 0) {
        return false;
    }

    const val = data[0].Value;
    return data.every((history) => history.Value === val);
}

hosts = RQL.ROS.GetHosts();
for (let host of hosts) {
    if (host.UUID === serverHostUUID) {
        continue
    }
    try {
        netOpts = {
            Args: {
                WithDevices: true,
                WithPoints: true,
            },
            HostUUID: host.UUID,
        };
        networks = RQL.ROS.GetNetworks(netOpts);

        for (let network of networks) {
            if (network.Enable == false || network.HistoryEnable == false) {
                continue;
            }

            for (let device of network.Devices) {
                if (device.Enable == false || device.HistoryEnable == false) {
                    continue;
                }

                for (let point of device.Points) {
                    if (point.Enable == false || point.HistoryEnable == false) {
                        continue;
                    }
                    try {
                        timestamp = getNHoursBeforeNow(hour);
                        histBody = {
                            Filter: `host_uuid=${host.UUID}&&point_uuid=${point.UUID}`,
                            FilterHistory: `timestamp>=${timestamp}`,
                        };
                        histOpts = {
                            Args: {},
                            HostUUID: serverHostUUID,
                        };
                        res = RQL.ROS.GetHistories(histBody, histOpts);

                        body = `host: ${host.Name}, network: ${network.Name}, device: ${device.Name},point: ${point.Name}, address-uuid: ${point.AddressUUID}`;
                        if (res.Data.length === 0) {
                            body = `${body} no data`
                            addAlert(host.UUID, "point", point.UUID, "fault", "crucial", "sensor no data", body);
                            continue;
                        }
                        if (isFlatLine(res.Data)) {
                            body = `${body} value:${res.Data[0].Value} flat line`
                            addAlert(host.UUID, "point", point.UUID, "flat-line", "crucial", "sensor flat line", body);
                        }
                    } catch (_) {
                    }
                }
            }
        }
    } catch (_) {
    }
}

RQL.Result = result.length > 0 ? result : "no alerts";


```

</details>

### iv. High/Low Threshold Alerts

<details><summary><u><i>Show script</i></u></summary>

```js
let result = [];
const highThresholdKey = "HighThreshold";
const lowThresholdKey = "LowThreshold";

function addAlert(hostUUID, entityType, entityUUID, type, severity, title, body, tags = []) {
    try {
        alert = {
            HostUUID: hostUUID,
            EntityType: entityType,
            EntityUUID: entityUUID,
            Type: type,
            Status: "active",
            Severity: severity,
            Title: title,
            Body: body,
            Tags: tags,
        };

        res = RQL.AddAlert(alert.HostUUID, alert);
        result.push(res);
    } catch (_) {
    }
}

hosts = RQL.ROS.GetHosts();
for (let host of hosts) {
    try {
        netOpts = {
            Args: {
                WithDevices: true,
                WithPoints: true,
                WithMetaTags: true,
            },
            HostUUID: host.UUID,
        };
        networks = RQL.ROS.GetNetworks(netOpts);

        for (let network of networks) {
            if (network.Enable == false) {
                continue;
            }
            for (let device of network.Devices) {
                if (device.Enable == false) {
                    continue;
                }
                for (let point of device.Points) {
                    if (point.Enable == false) {
                        continue;
                    }
                    for (let metaTag of point.MetaTags) {
                        title = ""
                        if (metaTag.Key === lowThresholdKey && metaTag.Value > point.PresentValue) {
                            title = "low threshold"
                        } else if (metaTag.Key === highThresholdKey && metaTag.Value < point.PresentValue) {
                            title = "high threshold";
                        }

                        if (title !== "") {
                            body = `host-name: ${host.Name}, network: ${network.Name}, device: ${device.Name},point: ${point.Name},
              address-uuid: ${point.AddressUUID}, value:  ${point.PresentValue}`;
                            addAlert(host.UUID, "point", point.UUID, "threshold", "crucial", title, body);
                        }
                    }
                }
            }
        }
    } catch (_) {
    }
}

RQL.Result = result.length > 0 ? result : "no alerts";


```

</details>

***

## 2. Filter with Tags/MetaTags

### i. Points filter with Tags/MetaTags

<details><summary><u><i>Show script</i></u></summary>

```js
hostUUID = "";
opts = {
    Args: {},
    HostUUID: hostUUID,
};
body = {
    Filter: "",
};

result = RQL.ROS.GetPoints(body, opts);

RQL.Result = result.length > 0 ? result : "no points";

```

#### With tags

>
> - **Fields**
> - `tag:<tag>` -> _Network/Device/Point tag._
> - `point_tag:<tag>` -> _Point tag._
> - **Operators**
> - Comparison Operators
> - `=` -> _Equal to._
> - `!=` -> _Not equal to._
> - Logical Operators
> - `&&` -> _And._
> - `||` -> _Or._
>
> >
> > **Filter examples:**
> > - `Filter:"(tag=tag1&&tag!=tag2)"`
> > - `Filter:"(tag=tag1||tag!=tag2)"`
> > - `Filter:"(point_tag=tag1&&point_tag!=tag2)"`
> > - `Filter:"(point_tag=tag1||point_tag!=tag2)"`
> >
>

#### With meta tags

>
> - **Fields**
> - `meta_tag_key_value:<key>:<value>` -> _Network/Device/Point meta tag key and value._
> - `meta_tag_key_or_value:<key>:<value>` -> _Network/Device/Point meta tag key or value._
> - `point_meta_tag_key_value:<key>:<value>` -> _Point meta tag key and value._
> - `point_meta_tag_key_or_value:<key>:<value>` -> _Point meta tag key or value._
> - **Operators**
> - Comparison Operators
> - `=` -> _Equal to._
> - `!=` -> _Not equal to._
> - Logical Operators
> - `&&` -> _And._
> - `||` -> _Or._
>
> >
> > **Filter examples:**
> > - `Filter:"(meta_tag_key_value=key1:value1&&meta_tag_key_value=key2:value2)"`
> > - `Filter:"(meta_tag_key_or_value=key1:value1&&meta_tag_key_or_value=key2:value2)"`
> > - `Filter:"(point_meta_tag_key_value=key1:value1&&point_meta_tag_key_value=key2:value2)"`
> > - `Filter:"(point_meta_tag_key_or_value=key1:value1&&point_meta_tag_key_or_value=key2:value2)"`
> >
>

</details>

### ii. Histories filter with Tags/MetaTags

<details><summary><u><i>Show script</i></u></summary>

```js
hostUUID = "";
opts = {
    Args: {},
    HostUUID: hostUUID,
};
body = {
    Filter: "",
};

RQL.Result = RQL.ROS.GetHistories(body, opts);

```

### With tags

>
> - **Fields**
> - `tag:<tag>` -> _Network/Device/Point tag._
> - `network_tag:<tag>` -> _Network tag._
> - `device_tag:<tag>` -> _Device tag._
> - `point_tag:<tag>` -> _Point tag._
> - **Operators**
> - Comparison Operators
> - `=` -> _Equal to._
> - `!=` -> _Not equal to._
> - Logical Operators
> - `&&` -> _And._
> - `||` -> _Or._
>
> >
> > **Filter examples:**
> > - `Filter:"(tag=tag1&&tag=tag2)"`
> > - `Filter:"(tag=tag1||tag=tag2)"`
> > - `Filter:"(network_tag=tag1&&device_tag=tag2&&point_tag=tag3)"`
> > - `Filter:"(network_tag=tag1||device_tag=tag2||point_tag=tag3)"`
> >
>

### With Meta tags

> - **Fields**
> - `meta_tag_key_value:<key>:<value>` -> _Network/Device/Point meta tag key and value._
> - `meta_tag_key_or_value:<key>:<value>` -> _Network/Device/Point meta tag key or value._
> - `network_meta_tag_key_value:<key>:<value>` -> _Network meta tag key and value._
> - `network_meta_tag_key_or_value:<key>:<value>` -> _Network meta tag key or value._
> - `device_meta_tag_key_value:<key>:<value>` -> _Device meta tag key and value._
> - `device_meta_tag_key_or_value:<key>:<value>` -> _Device meta tag key or value._
> - `point_meta_tag_key_value:<key>:<value>` -> _Point meta tag key and value._
> - `point_meta_tag_key_or_value:<key>:<value>` -> _Point meta tag key or value._
> - **Operators**
> - Comparison Operators
> - `=` -> _Equal to._
> - `!=` -> _Not equal to._
> - Logical Operators
> - `&&` -> _And._
> - `||` -> _Or._
>
> >
> > **Filter examples:**
> > - `Filter:"(meta_tag_key_value=tag1;value1:100&&meta_tag_key_or_value=tag2;value2)"`
> > - `Filter:"(meta_tag_key_value=tag1;value1:100||meta_tag_key_or_value=tag2;value2)"`
> > - `Filter:"(metwork_meta_tag_key_value=tag1;value1:100&&device_meta_tag_key_value=tag2;value2&&point_meta_tag_key_value=tag3;value3)"`
> > - `Filter:"(metwork_meta_tag_key_or_value=tag1;value1:100&&device_meta_tag_key_or_value=tag2;value2&&point_meta_tag_key_or_value=tag3;value3)"`
> >
>

</details>

***

## 3. Histories metrics(Count,Sum,Avg,Min,Max)

<details><summary><u><i>Show script</i></u></summary>

```js
result = {
    OverallMetrics: {Count: 0, Sum: 0, Average: 0, Min: 0, Max: 0},
    IndividualMetrics: [],
};
hostUUID = "hos_b1f62bf4358443de";
opts = {
    Args: {},
    HostUUID: hostUUID,
};

function calculateMetrics(values) {
    Count = values.length;
    if (Count === 0) {
        return {Count: 0, Sum: 0, Average: 0, Min: 0, Max: 0};
    }

    Sum = values.reduce((sum, value) => sum + value.Value, 0);
    Average = Sum / Count;

    valueArr = values.map((value) => value.Value);
    Min = Math.min(...valueArr);
    Max = Math.max(...valueArr);

    return {Count, Sum, Average, Min, Max};
}

body = {
    Filter: "",
    FilterHistory: `timestamp>2024-05-01T01:00:00Z&&timestamp<2024-06-30T01:00:00Z`,
};

histories = RQL.ROS.GetHistories(body, opts);

allValues = histories.Data.flatMap((history) => history.Values);

result.OverallMetrics = calculateMetrics(allValues);

for (history of histories.Data) {
    metrics = calculateMetrics(history.Values);
    result.IndividualMetrics.push({...history, ...{Metrics: metrics}});
}

RQL.Result = result;

```

</details>