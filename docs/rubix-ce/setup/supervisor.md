---
sidebar_position: 3
---

# Create A Supervisor
The Rubix-Platform-CE application can be used to setup and program multiple instances of the Rubix-assist (each customer has their own instance of Rubix-assist running in the cloud or on premises) so the user of CE can engineer multiple sites at once.

An admin can generate multiple tokens for each site specific customer and can also remove the customer from the site by revoking the specific token. See 'Generating a Token'.

## click on the add button
click on the Add ![add-button.png](../img/apps/add-button.png)

then you have 3 choices as below


## Option 1 Using a rubix-compute as the master

:::info
* a rubix-compute is needed to use this method
* this is the simplest way to get started with nube-io
:::

```mermaid
flowchart TD
    A[[Rubix-CE]] --> C[-]
    C[Rubix-Compute-1 As Supervisor] --> D[Rubix-Compute-1]
    C --> E[Rubix-Compute-2]
    C --> F[Rubix-Compute-3]
```


## Option 2 Using nube cloud

:::info 
* a rubix-compute is needed to use this method & a cloud account is needed
* contact nube support to get a cloud account
:::

```mermaid
flowchart TD
    A[[Rubix-CE]] --> C[-]
    C[Nube Cloud] --> D[Rubix-Compute-1]
    C --> E[Rubix-Compute-2]
    C --> F[Rubix-Compute-3]
```

## Option 3 Using your pc running docker

:::info
* no hardware is need for testing this
* you must install docker
:::

:::caution
this is for advanced use only 

see: [setup of docker](docker.md)
:::

```mermaid
flowchart TD
    A[[Rubix-CE]] --> C[-]
    C[Simulated Rubix-Assist Your PC] --> D[Simulated Rubix-Compute]
```