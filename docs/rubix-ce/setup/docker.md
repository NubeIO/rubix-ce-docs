---
sidebar_position: 8
---

# Advanced

:::caution
For assistance with setting up the mentioned feature, please reach out to Nube iO support at support@nube-io.com. Nube iO will be able to provide you with the necessary guidance and support to help you set up the feature according to your requirements.
:::

# Nube iO Cloud Account
A cloud account in Rubix CE serves various purposes and is recommended when the following functionalities are required:

- Providing remote access to view a Building Management System (BMS) or IoT sensor data online.
- Accessing the Nube iO Graphical Dashboard interface for monitoring and control purposes.
- Managing devices across multiple sites centrally.
- Storing long-term historical sensor data securely in the cloud.
- Establishing remote VPN access to BMS sites via the Nube iO VPN to a Rubix Compute for enhanced security and management capabilities.

Having a cloud account enables users to leverage these features and capabilities effectively within Rubix CE.

# Running a simulation of Rubix Stack on your PC

## Install docker

To install Docker, you can follow these steps:

1. Go to the Docker [downloads](https://docs.docker.com/get-docker/).
2. On the downloads page, select your operating system from the options provided.
3. Follow the instructions specific to your operating system to download and install Docker.

By following these steps, you'll be able to install Docker on your system and start using it for containerization purposes.

## Install and Run the Rubix Stack

:::info
To download Docker images from the Nube iO GitHub repository, you will need a **GITHUB_TOKEN** provided by Nube iO support. This token serves as an authentication mechanism to access the private repository where the Docker images are hosted. Once you have the **GITHUB_TOKEN**, you can use it in conjunction with Docker to pull the required images for your deployment. If you haven't received the token yet, please contact Nube iO support to obtain it.
:::

Once you have received the **GITHUB_TOKEN** from Nube iO support, you can use it to authenticate and download Docker images from their private repository. Here's the command you can use, replacing <GITHUB_TOKEN> with the token provided to you:

```
docker run -p 1659:1659 -p 1660:1660 -v <MOUNTING_LOCATION>:/data -e GITHUB_TOKEN=<GITHUB_TOKEN> --rm -it -d --privileged --name bios ghcr.io/nubeio/rubix-bios-legacy:1.13.0
```
In summary, this Docker command creates a container based on the Rubix BIOS Legacy image, exposing certain ports, mounting a directory, setting environment variables, and running the container in detached mode with elevated privileges.


In the provided Docker command, **<MOUNTING_LOCATION>** can be replaced with either /data if you want to mount it in that location or any other absolute directory, or rubix-volume if you want to mount it in a Docker volume.

Mounting in /data or rubix-volume provides flexibility in managing where the data is stored within the container environment. Here's how the command would look with these options:

```
docker run -p 1659:1659 -p 1660:1660 -v /data:/data -e GITHUB_TOKEN=<GITHUB_TOKEN> --rm -it -d --privileged --name bios ghcr.io/nubeio/rubix-bios-legacy:1.13.0
```
or

```
docker run -p 1659:1659 -p 1660:1660 -v rubix-volume:/data -e GITHUB_TOKEN=<GITHUB_TOKEN> --rm -it -d --privileged --name bios ghcr.io/nubeio/rubix-bios-legacy:1.13.0
```

This command installs only the BIOS and creates a platform for installing other Nube applications, with the data stored either in the /data directory or in a Docker volume named rubix-volume.
