---
sidebar_position: 2
---

# BACnet device
Setup the `rubix-compute` as a native BACnet/IP device

:::info reference
`RC` is a `rubix-compute` <br/>
`wires` is a `rubix-wires`
:::

:::info prerequisites
1. You need a **[rubix-compute](../hardware/controllers/supervisors/rubix-compute/overview.md)** and an **[IO-16](../hardware/controllers/io-controllers/IO-16/overview.md)**
2. plugin the `IO-16` into the side of the `RC`  and power the `RC` and set the `IO-16` address to `1`
3. make sure you can ping the `RC` default IP on ETH-1 is `192.168.15.10` see **[networking](../hardware/controllers/supervisors/rubix-compute/networks.md)** for more info
:::


# Setup

1. **[Download](../rubix-ce/setup/download.md)** once downloaded just double-click on the icon to run 
2. **[Getting setup](../rubix-ce/setup/getting-started.md)** 
3. Add a **[token](../rubix-ce/setup/getting-started.md#add-token)** to download 
4. Add a **[supervisor](../rubix-ce/setup/supervisor.md)**  
5. Add a **[host](../rubix-ce/setup/host.md)** (rubix-compute)
6. Install **[apps](../rubix-ce/setup/apps.md)** **[driver-bacnet](../rubix-ce/drivers/bacnet/bacnet-server/bacnet-server.md)** & **[rubix-wires](../rubix-ce/wires/overview.md)**

# BACnet config
After the `bacnet-driver` is installed we need to 

1. Set the `bacnet device-name`
2. Set the `bacnet device-id`
3. Set how many `IO-16s` we have plugin into the side


# Adding nodes in wires
So a `BACnet-supervisors` can read/write to the BACnet this is archived via by adding some nodes in `wires`

## Reading a 10K temperature sensor via UI-1
Lets started with a simple example of reading a `10K sensor` on `UI-1` on `device-1` (address 1)
1. Add a node called `bacnet-server` (if not already added)
2. Right-click on the `bacnet-server` node and `Open Sub Flow`
3. Add a node called `analog-input`
4. Right-click on the `analog-input` node and edit the node `settings`
5. Set the `IO Device Address` to `1`
6. Set the `UI number` to `1`
7. Set the `UI Input Type` to `thermistor_10k_type_2`
8. Deploy the flow

## Writing to a relay via UO-1
Lets started with a simple example of writing a `12vdc Relay` on `UO-1` on `device-1` (address 1)
1. Add a node called `bacnet-server` (if not already added)
2. Right-click on the `bacnet-server` node and `Open Sub Flow`
3. Add a node called `analog-ouput`
4. Right-click on the `analog-ouput` node and edit the node `settings`
5. Set the `IO Device Address` to `1`
6. Set the `UI number` to `1`
7. Set the `UI Ouput Type` to `digital`
8. To turn on/off the relay every 50 loop's (rubix-wires runtime looping) let's add a node called `flow-loop-count` 
9. Wire the `toggle` of the `flow-loop-count` to the `in15` of the `analog-ouput` node
10. Deploy the flow