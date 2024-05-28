---
sidebar_position: 4
---

## Hosts/Rubix Computes

**Rubix Compute** refers to a computing device or platform developed by **Nube iO**. It's designed for various applications in building automation and IoT (Internet of Things) contexts. Rubix Compute can serve as a central hub for collecting, processing, and analyzing data from sensors, devices, and systems within a building or industrial environment. It typically runs specialized software or applications developed by Nube iO or third-party developers to enable functionalities such as data monitoring, control, and optimization. Rubix Compute plays a crucial role in creating smart and interconnected building systems by facilitating data-driven decision-making and automation.

A Rubix Compute (host) is to be added under a `Supervisor`.

:::caution
At this point, you should have already added a `supervisor`. If not, please refer to the instructions for adding a **[supervisor](supervisor.md)**.
:::


![max800px](img/adding-host.gif)

:::info
A Rubix Compute can also serves as a supervisor controller. <br/>
However, you can only add a Rubix Compute after you have already added a **supervisor/location and group**
:::

## Add Location
Click on the `Create new Location` -or- click ![add-button.png](../img/apps/add-button.png)  inside the **Supervisor tab**
![max800px](../img/apps/add-location.png)

:::info
When you add a location, if you click `Save` without entering any information, Rubix will assign a `default name` to the location. You can modify its settings by right-clicking on the location and selecting `Edit`.
:::

![max800px](../img/apps/edit-location.png)


## Add Group
Click ![add-button.png](../img/apps/add-button.png)  inside the **Location tab**. 
![max800px](../img/apps/add-group.png)

![max300px](../img/apps/new-group.png)

Click `save` once you have fill up the name and description (tentative).

## Add Host
Click ![add-button.png](../img/apps/add-button.png)  inside the **Group tab**. 
![max800px](../img/apps/add-host.png)

![max800px](../img/apps/edit-host.png)


### Add a Local Device

This is only applicable when you have only one `Rubix Compute` and wish to connect to it directly, bypassing the need for the `Nube iO cloud`.

:::info pre start checks
- A **[rubix-compute](../../hardware/controllers/supervisors/rubix-compute/overview.md)** with network access to the
  device
- The default IP on `ETH-1` is `192.168.15.10` the 2nd port `ETH-2` is set to `DHCP`
- Set you PC on the same network or set a fixed IP on your PC **[networking](../../hardware/controllers/supervisors/rubix-compute/networks.md)**
:::

```mermaid
flowchart TD
    A[[Rubix-CE]] --> B[Rubix-Compute-1]
```

### Add Device to a Cloud Server
Adding a local device to the Nube iO Servers will only be required when you only have one Rubix Compute, and you want to connect to it `with` using the `Nube iO Cloud`

:::info pre start checks
- Before proceeding, ensure you have added the device following the same steps as outlined above.
- A **[rubix-compute](../../hardware/controllers/supervisors/rubix-compute/overview.md)** with network access to the device and a public IP address assigned.
- Connect your PC to your local network. See **[networking](../../hardware/controllers/supervisors/rubix-compute/networks.md)** to see how.
:::

:::caution
To establish a VPN connection between the cloud and the Rubix Compute, you'll require access to either your office router or a 4G router to assign a temporary public IP address to the Rubix Compute.
:::

```mermaid
flowchart TD
    A[[Rubix-CE]] --> B[Nube-IO Cloud]
    B[Nube-IO Cloud]--> C[Rubix-Compute-1]
```

<b>OpenVPN Service</b>

Open the **device/apps**

<b> Connect to the VPN </b>

Right Click on the device you want to add the `vpn` to





