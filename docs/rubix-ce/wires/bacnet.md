---
sidebar_position: 6
---

# BACnet

The server node is used to read/write value to the **[driver-bacnet](../setup/apps.md)** so the rubix-compute can be
added to a BACnet-network

:::tip
See also: **[tutorials bacnet-device](../../tutorials/bacnet-device.md)**
:::

The BACnet-server node has 2x use cases

1. Adding the IO (hardware input/output eg: sensors and 0-10dc) to the rubix-compute, via adding the **[Nube-IO IO-16](../../hardware/controllers/io-controllers/IO-16/overview.md)**
2. Adding proxy points (AVs and BVs) to the driver-bacnet

:::info Important thing to note before proceeding:
* Install required **[apps](../setup/apps.md)** **driver-bacnet**
:::

:::danger modbus networks conflict
You cant add a `modbus network` in `driver's` and the `BACnet-server` node in rubix-wires with the same `serial-port`, Its one or the other
:::

# Setup

## Add the bacnet-server node

1. Add the bacnet-server node
2. set the number of IO-16s if applicable to your use case, and also set the serial port

![bacnet-server.png](img/bacnet-server.png)

## Adding points

1. Open the bacnet-server node by right-click and `Open sub flow`
2. Once inside you can right-click to add nodes or drag from the pallet
3. Add a new node either: `AI, AO, AV`
4. Set the node name to set the `BACnet` object name

:::tip
Make sure you set the node `name` to reflect the point `name` on the `BACnet network`
:::


**BACnet point nodes**

| Node Name       | Category | Use Case                                                                 | is writeable              | 
|-----------------|----------|--------------------------------------------------------------------------|---------------------------|
| analogue-input  | bacnet   | Is only used when the IO-16s are added (will work with UIs)              | read only                 |
| analogue-output | bacnet   | Is only used when the IO-16s are added (will work with UOs)              | writeable via in14 & in15 |
| analogue-value  | bacnet   | to read and and write values to AVs on the bacnet-server, eg a set-point | writeable via in14 & in15 |
| binary-value    | bacnet   | to read and and write values to BVs on the bacnet-server, eg an enable   | writeable via in14 & in15 |

## Adding IO-16s

Adding upto 4x IO16s will make the rubix-compute a BACnet-ip IO device

![rc-with-io16s.png](../../hardware/controllers/supervisors/rubix-compute/img/rc-with-io16s.png)

:::info
**[more info on adding IO16s](../../hardware/controllers/supervisors/rubix-compute/overview.md#io-add-on-modules)**
:::

### adding a AI or AO

:::caution
we don't need to add a modbus network in flow-framework to talk to the IO-16s
:::

:::caution
set up the BACnet-Server configuration with the number of IO-16s you will add more info **[bacnet-config](../drivers/bacnet/bacnet-server/bacnet-server.md#bacnet-server-settings)**
:::


Let's start with an example of adding UI-1 on IO-2

1. power down the rubix-compute and plugin 2x IO16s (note the IO-16s are powered via the rubix-compute)
2. set IO16 number 1 to address 1 and number 2 to address 2 via the dip switches, also set the **baud rate** to **38400
   ** **[more info on setting up the IO-16s](../../hardware/controllers/io-controllers/IO-16/parameters.md)**
3. repower the rubix-compute
4. open the bacnet-server node
5. add an analogue-input node
6. right-click on the node and open the node `settings`
7. set the `IO Device Number` and our example it will be 2 (this is the 2nd IO-16)
8. set the `UI Number` to 1 (as in UI1)
9. this will set the *AI9*


:::tip
As the `IO-16` uses `UOs` and `UIs` we can only add `AOs` & `AIs` <br/>
eg: to use `UI-1` as an `DI` we add an `AI node` and set it to `address 1` (`AI1`) and set as as a `digital`
:::

:::tip writing to a UO as digital
Add an `AO` node and set the setting as `digital` the point will accept any value greater then `1` to turn on the `DO` <br/>
eg: `true/false` or `1/0` or `10/0`
:::


## the UI and UO to BACnet addressing

### Example for inputs

| Device Address | IO Number | BACnet address | 
|----------------|-----------|----------------|
| 1              | UI1       | AI1            | 
| 1              | UI2       | AI2            | 
| 1              | UI3       | AI3            | 
| 1              | UI4       | AI4            | 
| 1              | UI5       | AI5            | 
| 1              | UI6       | AI6            | 
| 1              | UI7       | AI7            | 
| 1              | UI8       | AI8            | 
| 2              | UI1       | AI9            | 
| 3              | UI1       | AI17           | 


It will continue up until we get to 4x IO1-6 devices

### Example for outputs


| Device Address | IO Number | BACnet address | 
|----------------|-----------|----------------|
| 1              | UO1       | AO1            | 
| 2              | UO1       | AO9            | 
| 3              | UO1       | AO17           | 
