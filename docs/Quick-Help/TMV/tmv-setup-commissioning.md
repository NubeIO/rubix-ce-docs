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

### 3.1 TMV Slave Gateway
TMV Slave Gateways are linux devices that run the `lorawan-gateway` service.  These devices are connected via ethernet/IP networks.  The TMV Slave Gateways only receive/transmit messages to their local TMV IO16s.  All received messages are sent to the Master Gateway for processing, all transmissions are commanded from the Master Gateway.

#### 3.1.1 Slave Gateway Setup
This section describes the setup of a TMV Slave Gateway.

1. The TMV Slave Gateway must run a compatible version of Linux.
2. The TMV Slave Gateway must have Rubix BIOS Installed.
3. The TMV Slave Gateway must have Rubix-OS installed.
4. The TMV Slave Gateway must have the `lorawan-gateway` service installed.
5. The TMV Slave Gateway must have the `lorawan-server` service installed.
6. The TMV Slave Gateway configuration must be updated so that it references the TMV Master Gateway. 

##### 3.1.1.1 Installing Rubix-OS
Rubix-OS can now be installed same as any other Rubix-OS installation. See [**Hosts**](../../rubix-ce/setup/Hosts.md) for more information.

##### 3.1.1.2 Slave Lorawan Setup
In order to update the Lorawan setup on a Slave Gateway and retrieve the `gateway_ID`, SSH should be used to access the config file.

1. First find the lorawan config file. There are several versions of Lorwan used, so the exact directory will depend on the version. Eg:
    - `sudo nano ~/lorawan-complete-2.5.2/gateway/sx1302/global_conf.json`
    - `sudo nano ~/lorawan-complete-2.3.2/gateway/pico/pkt_fwd/global_conf.json`

2. In the `global_conf.json` file, find the `gateway_ID` value and copy this value for later use.
3. In the same `global_conf.json` file, find the `server_address` value and update this to the IP address of the TMV Master Gateway.
4. Save the `gateway_conf.json` file and restart the device. 

See below example global_conf.json:

```json
"gateway_conf": {
        "gateway_ID": "0016c001ff1f0123", <-- RETRIEVE THIS VALUE FOR LATER USE>
        "server_address": "192.168.15.10", <-- UPDATE THIS TO THE MASTER GATEWAY IP ADDRESS>
        "serv_port_up": 1700,
        "serv_port_down": 1700,
        "keepalive_interval": 10,
        "stat_interval": 30,
        "push_timeout_ms": 100,
        "forward_crc_valid": true,
        "forward_crc_error": false,
        "forward_crc_disabled": false,
                "autoquit_threshold": 0
```


<br/>

### 3.2 TMV Master Gateway
A TMV Master Gateway is a linux device that runs a full stack of Nube-iO software. This includes:
- `lorawan-gateway` service
- `lorawan-server` service
- Rubix-OS
- Rubix BIOS

The TMV Master Gateway can be either a Rubix Compute controller (for small numbers of TMVs, <50), or it can be a Linux PC (HP EliteDesk 800 G5 Mini PC) that can have Rubix BIOS and Rubix-OS installed.

The HP EliteDesk 800 G5 Mini PC gets built into a plastic enclosure box (same as the other gateways). The specifications for this Mini PC are located here: [**HP EliteDesk 800 G5 Mini PC**](https://drive.google.com/file/d/1hhPLv66LYMg2oy9hxzLxl0X3zMeiXyPN/view)

<br/>

#### 3.2.1 Master Gateway Setup
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

##### 3.2.1.1 Installing Linux
The TMV Master Gateway must run a compatible version of Linux. The recommended distribution is Ubuntu Server 22.04 LTS, however other distributions may be compatible. 

Use the steps outlined in the following Ubuntu guide: [**Install Ubuntu  24.04 LTS**](https://ubuntu.com/tutorials/install-ubuntu-desktop#2-download-an-ubuntu-image)

<br/>

##### 3.2.1.2 Installing and Configuring BIOS
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

##### 3.2.1.3 Installing SSH

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

##### 3.2.1.4 Installing Rubix-OS
Rubix-OS can now be installed same as any other Rubix-OS installation. See [**Hosts**](../../rubix-ce/setup/Hosts.md) for more information.


<br/>

##### 3.2.1.5 Docker and MQTT Service Installation
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

##### 3.2.1.6 Installing lorawan-gateway and lorawan-server services
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

##### 3.2.1.7 Installing Apps and Modules
The Rubix Apps and Modules can now be installed same as any other Rubix installation. 

See:
- [**Apps**](../../rubix-ce/setup/apps.md) for more information.
- [**Modules**](../../rubix-ce/setup/Modules.md) for more information.

The following Apps and Modules must be installed on the TMV Master Gateway:
- lorawan-modbus-bridge (App) - `>= v1.0.0`
- module-oem-galvintmv (Module) - `>= v0.3.2`
- module-core-lorawan (Module) - `>= v1.0.0`
- module-core-modbus (Module) - `>= v1.0.5`
- module-core-history (Module) - `>= v1.0.3`
- module-core-postgres (Module) - `>= v1.0.2`

<br/>

##### 3.2.1.8 module-oem-galvintmv Configuration
The **module-oem-galvintmv** Rubix-OS (ROS) module has been developed to support the configuration, commissioning, maintenance, and reporting of the Galvin TMV system. 

This module runs on the Master Gateway to configure the system.  It also runs on the cloud supervisor to support dashboard data APIs. 


The **module-oem-galvintmv** module must be configured as follows:
- **postgres** - This configuration only needs to be set on the cloud supervisor for access to postgres for dashboard APIs. Obtain the relevant details from the Nube K8 sheet. 
```yaml
postgres:
  host: <HOST_ADDRESS>
  user: <USERNAME>
  password: <PASSWORD>
  db_name: <DB_NAME>
  port: <PORT_NUMBER>
  ssl_mode: disable
```

- **enable_config_steps** - Set to `false`.  Not required.
- **enable_commissioning** - Set to `false` for long term operation.  When set to `true` this turns on the automatic calls to the `lorawan_point_rename` API and `lorwan_history_config/cov`; these API calls are made 3 times a day (at midnight, 8am, and 4pm). 
- **enable_bacnet** - Set to `false`.  Not required.
- **rtc_write_enable** - Set to `true` for normal operation, this turns on the automatic writing of the RTC and RTC_Offset points.  This occurs 3 times a day.  These writes are responsible for preventing the modbus watchdog reset. 
- **rtc_write_enable** - Set to `false` for long term operation.  Set to `true` if you need to produce logs in the `/data/galvin-tmv/rtc-write-logs` directory.  Note that this will fill up disk space if the logs are not deleted.
- **frequency** - Set to `30m`.  Not used.
- **chirpstack_host** - Set to `0.0.0.0`.
- **chirpstack_application_number** - Set to match the Chirpstack Application number where the TMV IO16s are added.
- **chirpstack_network_key** - Set to `0301021604050f07e6095a0b0c12630f`.  This is the Lorawan activation key.
- **chirpstack_token** - Generate a token in Chirpstack and then paste the token.  This must be done before ROS can communicate with Lorawan. 
- **tmv_json_file_path** - Not required.
- **sync_points_with_db** - Set to `false` for normal operation.  Can be set to `true` to force sync the points to postgres DB; the postgres config must also be set.  It is preferable to use the `postgres` module to sync the points instead. 
- **sync_tags_with_db** - Set to `false`.  Not required.
- **sync_meta_tags_with_db** - Set to `false`.  Not required.
- **log_level** - Set to `DEBUG`.  Shows module logs in the Rubix-OS service logs.

See below example configuration:
```yaml
postgres:
  host: "timescale-example.nube-iiot.com"
  user: exampleuser
  password: <PASSWORD>
  db_name: exampledb
  port: 1234
  ssl_mode: disable
job:
  enable_config_steps: false
  enable_commissioning: false
  enable_bacnet: false
  rtc_write_enable: true
  rtc_write_logging_enable: false
  frequency: 30m
  chirpstack_host: 0.0.0.0
  chirpstack_application_number: 1
  chirpstack_network_key: 0301021604050f07e6095a0b0c12630f
  chirpstack_token: <CHIRPSTACK_TOKEN>
  tmv_json_file_path: ""
  sync_points_with_db: false
  sync_tags_with_db: false
  sync_meta_tags_with_db: false
log_level: DEBUG
```

<br/>

##### 3.2.1.9 Adding Slave Gateways 
Slave Gateways must be added via Chirpstack with the `gateway_ID` values collected during the Slave Gateway setup. 
1. Log in to the Chirpstack web interface and navigate to the **Gateways** section.
2. Click on the **Create** button to add a new gateway.
3. In the **Create Gateway** form, enter the following details:
    - **Gateway Name**: Enter a name for the gateway (e.g., "TMV_Slave_Gateway_1").
    - **Gateway Description**: Enter a description for the gateway (e.g., "TMV_Slave_Gateway_1").
    - **Gateway ID**: Enter the `gateway_ID` value collected from section [3.1.1.2 Slave Lorawan Setup](#3112-slave-lorawan-setup).
    - **Network Server**: Select `local-network-server` as thenetwork server for the gateway.
    - **Service Profile**: Select `local-service-profile-default` as the service profile for the gateway.
    - **Gateway Profile**: Select `AU915_0` as the gateway profile for the gateway.
    - **Gateway Discovery Enabled**: Set to `false`.
    - **Gateway altitude**: Can be left set to `0`.

4. Click on the **Create Gateway** button to save the new gateway.

<br/>

## 4. Adding TMV IO16s
Prior to each batch of TMV IO16s being dispatched to site, there will be automated factory testing done to ensure that the IO16s are stable and do not exhibit abnormal behaviour. Units will also undergo a quality assurance inspection before dispatch. All IO16s and checks must be recorded in the Deployment Tracking spreadsheet in the project folder using the following template: `*TEMPLATE* TMV Factory Flashing and QA.xlsx`. This spreadsheet is used by the configuration scripts so the specific format is important.

<br/>

### 4.1 Commissioning Tool

Adding the TMV IO16s to the system utilises a commissioning tool to add, link and configure the TMV IO16s in the Chirpstack Network Server and the `module-oem-galvintmv` ROS module. This commissioning tool is a command line executable that takes in the TMV IO16 details directly from the Deployment Tracking spreadsheet (eg. DevEUI, Device name, modbus address, etc.) and then performs all the necessary API calls to add the device to Chirpstack, link it to the correct modbus network, and then add the device details to the `module-oem-galvintmv` configuration.

**Commissioning tool:** [**tmv-add-device.exe**](https://drive.google.com/file/d/123J1yfj6K0pLpzZfgXoXNpw6e3pasVW5/view)

<br/>

### 4.2 Commissioning Steps
