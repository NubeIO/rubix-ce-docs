---
sidebar_position: 3
---

# Modbus To IO-16
Setup the `rubix-compute` as a Modbus-Master to the `IO-16` and read `UI1` as a `10K sensor`

:::info reference
`RC` is a `rubix-compute` <br/>
`wires` is a `rubix-wires`
:::

:::info prerequisites
1. You need a **[rubix-compute](../hardware/controllers/supervisors/rubix-compute/overview.md)** and an **[IO-16](../hardware/controllers/io-controllers/IO-16/overview.md)**
2. wire the `IO-16` into the `rs485-1` the `RC`  and power the `RC`, and `IO16` and set the `IO-16` address to `1` and `baud-rate` `38400`
3. make sure you can ping the `RC` default IP on ETH-1 is `192.168.15.10` see **[networking](../hardware/controllers/supervisors/rubix-compute/networks.md)** for more info
:::


# Setup

1. **[Download](../rubix-ce/setup/download.md)** once downloaded just double-click on the icon to run 
2. **[Getting setup](../rubix-ce/setup/getting-started.md)** 
3. Add a **[token](../rubix-ce/setup/getting-started.md#add-token)** to download 
4. Add a **[supervisor](../rubix-ce/setup/supervisor.md)**  
5. Add a **[host](../rubix-ce/setup/host.md)** (rubix-compute)
6. Install module/plugin `modbus`


# Add a network
We will add a modbus network with these settings

Network settings will be
* serial port on `485-1` (left port on the rubix-compute)
* set modbus `baud-rate` to `38400`

Device settings (take off the cover to access the dip switches)
* on the `left` dip-switch bank set the dip switches `00000001` (address `1`)
* on the `right` dip-switch bank set the dip switches `00000001` (device mode:`rs485 mode` modbus settings `baud-rate`:38400)

:::tip
see **[dip switches](../hardware/controllers/io-controllers/IO-16/parameters.md#dip-switch-configuration)** for more info
:::

:::tip
see **[registers](../hardware/controllers/io-controllers/IO-16/registers.md#registers)** list for the `IO-16`
:::

# Add a Device and point to read a 10K sensor

1. Open drivers and add a new network of type `Modbus-RTU` and set the port to `485-1` for more info on: **[ports](../hardware/controllers/supervisors/rubix-compute/ports.md)**
2. Add a device and set the address to `1`
3. Add a point of type `read register` and address `1` as type `int16` and the write mode to `Read Always` and `Multiplication Factor` to `0.01`

# Add a Device and point to write a 0-10dc

1. Open drivers and add a new network of type `Modbus-RTU` and set the port to `485-1` for more info on: **[ports](../hardware/controllers/supervisors/rubix-compute/ports.md)**
2. Add a device and set the address to `1`
3. Add a point of type `write holidng register` and address `1` as type `int16` and the write mode to `Write Always` and `Multiplication Factor` to `0.01`

:::tip
see point write/read **[modes](../rubix-ce/drivers/overview.md#point-write-modes)** for the different point `polling` methods
:::