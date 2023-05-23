---
sidebar_position: 2
---

# LoRa to BACnet
Setup the `rubix-compute` as a native BACnet/IP device with LoRa

:::info reference
`RC` is a `rubix-compute` <br/>
`wires` is a `rubix-wires`
:::

:::info prerequisites
1. You need a **[rubix-compute](../hardware/controllers/supervisors/rubix-compute/overview.md)** and an **[IO-16](../hardware/sensors/droplets/droplets-v1/overview.md)**
2. power the `RC`
3. make sure you can ping the `RC` default IP on ETH-1 is `192.168.15.10` see **[networking](../hardware/controllers/supervisors/rubix-compute/networks.md)** for more info
:::


# Setup

1. **[Download](../rubix-ce/setup/download.md)** once downloaded just double-click on the icon to run 
2. **[Getting setup](../rubix-ce/setup/getting-started.md)** 
3. Add a **[token](../rubix-ce/setup/getting-started.md#add-token)** to download 
4. Add a **[supervisor](../rubix-ce/setup/supervisor.md)**  
5. Add a **[host](../rubix-ce/setup/host.md)** (rubix-compute)
6. Install **[apps](../rubix-ce/setup/apps.md)** **[driver-bacnet](../rubix-ce/drivers/bacnet/bacnet-server/bacnet-server.md)** & **[rubix-wires](../rubix-ce/wires/overview.md)** & **[driver-lora](../rubix-ce/drivers/lora/lora-raw/lora.md)**

# BACnet config
After the `bacnet-driver` is installed we need to 

1. Set the `bacnet device-name`
2. Set the `bacnet device-id`
3. Set how many `IO-16s` we have plugin into the side


# Adding nodes in wires
So a `BACnet-supervisors` can read/write to the BACnet this is archived via by adding some nodes in `wires`

1. Add a node called `bacnet-server` (if not already added)
2. Add a node called `flow-network` (if not already added)


# Mapping

**[mapping](../rubix-ce/wires/mapping.md)**

