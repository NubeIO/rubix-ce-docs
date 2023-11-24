---
sidebar_position: 8
---

# Advanced

:::caution
Please contact `nube support` for getting this setup.
Support can be contacted via support@nube-io.com
:::

# Nube iO Cloud Account
A cloud account is a prescibed cloud based service and can be used when the following is required:

- Provide a remote access to view a BMS/IoT sensors online.
- Access to the Nube iO Graphical Dashboard interface.
- Multi site device management
- Storage of long term historical sensor data.
- Remote VPN access to a BMS sites via the Nube iO VPN to a Rubix Compute.


# Running a simulation of Rubix Stack on your PC

## Install docker
To install docker go to docker [downloads](https://docs.docker.com/get-docker/) and the `select your OS` and install docker

## Install and run the Rubix Stack

:::info
A **GITHUB_TOKEN** from `nube-io support` is required to download the Docker images 
:::

Once you have the token copy the `cmd` below and replace `<GITHUB_TOKEN>` with the token provided to you by `nube-io support`

```
docker run -p 1659:1659 -p 1660:1660 -v <MOUNTING_LOCATION>:/data -e GITHUB_TOKEN=<GITHUB_TOKEN> --rm -it -d --privileged --name bios ghcr.io/nubeio/rubix-bios-legacy:1.13.0
```

Here `<MOUNTING_LOCATION>` could be:
- `/data`: if you wanna mount it in that location or any other absolute directory
- `rubix-volume`: if you wanna mount it in docker volume

This will install BIOS only and create a platform to install other Nube applications.
