---
sidebar_position: 1
---

# TMV Setup and Commissioning

## 1. Overview

Thermostatic Mixing Valves (TMVs) are a water valve that produces water at a predefined setpoint temperature.  In partnership with Galvin Engineering, a large manufacturer of TMVs in Australia, Nube has developed a wireless system to monitor the flow amount and temperatures of the TMVs via temperature sensors, flow switches, and IO16s.   The wireless communications for this system is via LoRaWAN; it is capable of periodic 1-way pushes from the IO16s, and 2-way communications using Modbus over LoRaWAN.

The IO16s are in small plastic enclosures in the ceiling spaces, with extended temperature sensors (via flow switches) to the TMV flow temperature wells.  There is 1 x IO16 per TMV (although each TMV can have multiple outlets: shower, basic, etc.)

## 2. Components

### 2.1 Temperature Sensor
The outlet temperature of a TMV is  monitored via a 10k type II temperature sensor.  The sensors are each wired through a mechanical flow switch and connected to Universal Input 1 (UI1) of the RIO controller.  

The temperature sensor is to be installed in the 20mm copper TMV outlet pipe.  The sensor probe may be housed to protrude into the flow stream (preferred), or be externally attached to the copper pipe (in such a way that the temperature can be accurately sensed).

Ensure that the Temperature Sensor and Flow Switch are wired according to the provided Galvin TMV Layout and Wiring Schematic.

### 2.2 Solenoid
A solenoid valve can be connected to the RIO Controller Universal Output 1 (UO1).  When enabled this solenoid valve will activate the TMV tap.  This can be utilized to meet regulatory requirements for minimum flow.

Ensure that the Solenoid is wired according to the provided Galvin TMV Layout and Wiring Schematic.

### 2.3 Nube-iO Rubix IO-16 Module (RIO) Controller
The Nube-iO Rubix IO-16 Module (RIO) Controller, pre-loaded with the Galvin CliniMix TMV firmware, monitors the connected temperature sensor and performs on-board logic and calculations to provide reporting data to the TMV Reporting Dashboard, via a Nube-iO Rubix Compute Gateway Controller configured to suit the CliniMix Monitoring and Reporting System.

The RIO Controller communicates with the Nube-iO Rubix Compute Gateway Controller via LoRaWAN (wireless) modbus network connection.

### 2.4 Nube-iO Gateway
The Nube-iO Rubix Gateway, provides LoRaWAN (wireless) modbus network connection to the Nube-iO Rubix IO-16 Module (RIO) Controllers, installed on each TMV.   

The Gateway Controller collects and sends TMV Data, via an internet connection, to the Cloud Reporting Database.

### 2.5 TMV Cloud Reporting Database
The Nube-iO Rubix Compute Gateway Controllers are configured to log data automatically, this data is sent, via an internet connection, to the configured Cloud Reporting Database.  The TMV Cloud Reporting Database collects and stores the TMV data for use by the TMV Cloud Reporting Dashboard.  The TMV Cloud Reporting Database is secured with administrator credentials.

### 2.6 TMV Cloud Reporting Dashboard
Custom web browser based TMV Cloud Reporting Dashboards are configured to provide live visual interaction with the TMV Cloud Reporting Database. This TMV Cloud Reporting Dashboards can include elements like: Alarm Consoles, Charts, Statistics, Raw Data Review, and Reports. The TMV Cloud Reporting Dashboards are secured with administrator and user credentials.

## 3. Gateway Setup 

### 3.1 TMV Master Gateway
A TMV Master Gateway is a linux device that runs a full stack of Nube-iO software. This includes:
- `lorawan-gateway` service
- `lorawan-server` service
- Rubix-OS
- Rubix BIOS

The TMV Master Gateway can be either a Rubix Compute controller (for small numbers of TMVs, <50), or it can be a Linux PC that can have a LoRaWAN concentrator connected.

The Master Gateway is a HP EliteDesk 800 G5 Mini PC. This Mini PC gets built into a plastic enclosure box (same as the other gateways). The specifications for this Mini PC are here: [**HP EliteDesk 800 G5 Mini PC**](https://drive.google.com/file/d/1hhPLv66LYMg2oy9hxzLxl0X3zMeiXyPN/view)

### 3.1.1 Master Gateway Setup
This section describes the setup of the TMV Master Gateway.

1. The TMV Master Gateway must run a compatible version of Linux.
2. The TMV Master Gateway BIOS must be installed and configured so that it boots automatically on power up.  As well as any other configurations for stable operation of the device with no manual intervention. 
3. The TMV Master Gateway must have Rubix BIOS Installed.
4. The TMV Master Gateway must have Rubix-OS installed.
5. The TMV Master Gateway must have the `lorawan-gateway` service installed.
6. The TMV Master Gateway must have the `lorawan-server` service installed.
7. The TMV Master Gateway must have the `module-oem-galvintmv` ROS module installed.
8. The Chirpstack API Token must be entered into the `module-oem-galvintmv` ROS module configuration. 
9. Setup APIs must be run for the TMV Deployment setup. 
10. Slave Gateways should be added via Chirpstack with the `gateway_ID` values collected during the Slave Gateway setup. 

<br/>

#### 3.1.1.1 Installing Linux
The TMV Master Gateway must run a compatible version of Linux. The recommended distribution is Ubuntu Server 22.04 LTS, however other distributions may be compatible. 

Use the steps outlined in the following Ubuntu guide: [**Install Ubuntu  24.04 LTS**](https://ubuntu.com/tutorials/install-ubuntu-desktop#2-download-an-ubuntu-image)

<br/>

#### 3.1.1.2 Installing and Configuring BIOS
Once Linux is installed, the TMV Master Gateway BIOS must be installed and configured. Use the following steps and commands to install and configure the BIOS:

1. Download the latest version of the Nube-iO Rubix BIOS from the Nube-iO repository [**Rubix-Bios**](https://github.com/NubeIO/rubix-bios/releases/tag/v1.5.0) or use the following command: 
```bash
curl -L -H "Accept: application/octet-stream" -H "Authorization: Bearer <YOUR_GITHUB_TOKEN>" -H "X-GitHub-Api-Version: 2022-11-28" https://api.github.com/repos/NubeIO/rubix-bios/releases/assets/140275339 -o rubix-bios-1.5.0-03a596bf.amd64.zip
```
2. Open a command line terminal and extract the downloaded Rubix BIOS zip file using the following command:
```bash
unzip rubix-bios-1.5.0-03a596bf.amd64.zip
```
3. Install rubix BIOS on the TMV Master Gateway using the following command: 
```bash
sudo ./rubix-bios install --arch=amd64
``` 

<br/>

#### 3.1.1.3 Installing SSH

1. Install the OpenSSH Server package using the following commands:
```bash
sudo apt update
sudo apt install openssh-server
```
2. Enable the SSH service to start on boot using the following command:
```bash
sudo systemctl enable ssh
sudo systemctl start ssh
```

3. Verify that the SSH service is running using the following command:
```bash
sudo systemctl status ssh
```
:::info
The ssh username and password will be the same as the Linux user account created during the Linux installation.  It is recommended to create a user account specifically for the TMV Master Gateway, and to use a strong password.
:::

<br/>

#### 3.1.1.4 Installing Rubix-OS
Rubix-OS can now be installed same as any other Rubix-OS installation. See [**Hosts**](../../rubix-ce/setup/Hosts.md) for more information.


<br/>

#### 3.1.1.5 Docker and MQTT Service Installation
The `lorawan-gateway` and `lorawan-server` services run in Docker containers, so Docker must be installed on the TMV Master Gateway. The following commands can be used to install Docker and MQTT:
```bash
docker pull --platform linux/arm/v7 postgres:9.6-alpine
docker tag postgres:9.6-alpine postgres:local
docker save -o docker-build/postgres-local.tar postgres:local
docker pull --platform linux/arm/v7 redis:5-alpine
docker tag redis:5-alpine redis:local
docker save -o docker-build/redis-local.tar redis:local
Install mosquitto
```

<br/>

#### 3.1.1.6 Installing lorawan-gateway and lorawan-server services
The `lorawan-gateway` and `lorawan-server` services can be installed using the following commands:

**Download:**
```bash 
wget https://github.com/NubeIO/lorawan-complete/archive/refs/tags/v$LORAWAN_VERSION.zip && wget https://github.com/NubeIO/lorawan-complete/releases/download/v$LORAWAN_VERSION/docker-builds.zip && unzip v$LORAWAN_VERSION.zip && unzip docker-builds.zip -d lorawan-complete-$LORAWAN_VERSION/docker-build && sudo rm docker-builds.zip && cd lorawan-complete-$LORAWAN_VERSION/
```

**Install Gateway:**
```bash
sudo bash install-gateway-sx1302.sh -h
OR
sudo bash install-gateway-pico.sh -h
OR
sudo bash install-gateway-rak2247.sh -h
```

**Install Server:**
```bash
sudo bash install-server.sh -h
```

<br/>





<br/>

### 3.2 TMV Slave Gateway
TMV Slave Gateways are linux devices that run the `lorawan-gateway` service.  These devices are connected via ethernet/IP networks.  The TMV Slave Gateways only receive/transmit messages to their local TMV IO16s.  All received messages are sent to the Master Gateway for processing, all transmissions are commanded from the Master Gateway.
