---
sidebar_position: 1
---


# Overview

## Rubix-Assist
Rubix-Assist is used to manage a group of Rubix-computes, Rubix-assist can either run in the cloud or on a single Rubix-compute.


### performs tasks like:
* Updating Rubix-computes apps

### runs on hardware
Runs in the `cloud` or on a `Rubix-compute`

### port

runs on port `http`
```
1662
```
runs on port `https`
```
ra-YOURACCOUNT.nube-iiot.com
```

### service name
```
sudo systemctl status nubeio-rubix-assist
```




## Rubix-Edge
Rubix-Edge is used to connect to rubix-assist

### performs tasks like

* Updating rubix-computes apps
* Updating the device networking, time and firewall

### runs on hardware
Runs in the `cloud` or on a `Rubix-compute`

### port

runs on port `http`
```
1662
```
runs on port  `https`
```
re-YOURACCOUNT.nube-iiot.com
```

### service name
```
sudo systemctl status nubeio-rubix-edge
```

## Rubix-Edge-Bios
Rubix-Edge is used to connect to rubix-assist

### performs tasks like

* Updating rubix-computes apps
* Updating the device networking, time and firewall

### runs on hardware
Runs in the `cloud` or on a `Rubix-compute`

### port

runs on port `http`
```
1662
```
runs on port  `https`
```
443
rb-YOURACCOUNT.nube-iiot.com
```

### service name
```
sudo systemctl status nubeio-rubix-edge-bios
```



## Flow-framework
Flow-framework is used for managing protocols like lora, bacnet

## performs tasks like

* Scheduling
* Connections to the Nube-IO cloud
* Protocols like Lora, Modbus and BACnet

### runs on hardware
Runs in the `cloud` or on a `Rubix-compute`

### port

runs on port `http`
```
1660
```
runs on port  `https`
```
ff-YOURACCOUNT.nube-iiot.com
```

### service name
```
sudo systemctl status nubeio-flow-framework
```



### Rubix-Edge-Wires
Rubix-Edge-Wires is a building automation control runtime for controlling HVAC equipment, lighting. Rubix-Edge-Wires uses a flow based programming runtime

## performs tasks like

* bms HVAC flow based programming


### runs on hardware
Runs in the `cloud` or on a `Rubix-compute`

### port

runs on port `http`
```
1665
```


### service name
```
sudo systemctl status nubeio-rubix-edge-wires
```





