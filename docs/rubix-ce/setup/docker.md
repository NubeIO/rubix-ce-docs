---
sidebar_position: 8
---

# Advanced

:::caution
Please contact `nube support` for getting this setup
:::

# Nube-IO Cloud Account
A cloud account is a paid cloud based service and can be used when you want to achieve the following

- Give your clients remote access to view their BMS system and or IoT sensors online view the nube-io cloud dashboard
- Store long term historical sensor data in the cloud
- Have remote VPN access to your BMS sites via the nube-io VPN to the rubix-compute


# Running a simulation of rubix-stack on your PC

## install docker
To install docker go to docker [downloads](https://docs.docker.com/get-docker/) and the `select your OS` and install docker

## Install and run the rubix-stack

:::info
You need to get a **GITHUB_TOKEN** from `nube-io support` to download the docker images 
:::

Once you have the token copy the `cmd` below and replace `<GITHUB_TOKEN>` with the token given to you by `nube-io support`

```
docker run -p 1659:1659 -p 1660:1660 -v <MOUNTING_LOCATION>:/data -e GITHUB_TOKEN=<GITHUB_TOKEN> --rm -it -d --privileged --name bios ghcr.io/nubeio/rubix-bios-legacy:1.13.0
```

Here `<MOUNTING_LOCATION>` could be:
- `/data`: if you wanna mount it in that location or any other absolute directory
- `rubix-volume`: if you wanna mount it in docker volume

This will install BIOS only and create a platform to install other Nube applications.