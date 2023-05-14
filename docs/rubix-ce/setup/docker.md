---
sidebar_position: 7
---

# Advanced

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

once you have the token copy the `cmd` below and replace `<GITHUB_TOKEN>` with the token given to you by `nube-io support`

```
docker run -p 1659:1659 -p 1661:1661 -v rubix-volume:/data -e GITHUB_TOKEN=<GITHUB_TOKEN> --rm -it -d --privileged --name bios ghcr.io/nubeio/rubix-bios:1.11.0
```



this will install bios only
then you need to
* install assist by right click on supervisor
* then add a host and right-click install edge