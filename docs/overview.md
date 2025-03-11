---
sidebar_position: 1
---
# Overview

Rubix CE (Computer Edition) is Nube iO's desktop software designed for offline programming and product management. Engineered to be swift, efficient, and portable, it empowers users and technicians to configure and modify systems remotely without requiring a continuous internet connection.

## Core Components

### Rubix OS (Operating System)

The Rubix OS serves as the core runtime environment, operating either on the Rubix Compute hardware or within the Nube iO cloud. Key functionalities include:

- **Application Management**: Updating Rubix Compute applications, points, histories, and network drivers.
- **Scheduling**: Managing and executing scheduled tasks.
- **Cloud Connectivity**: Establishing secure connections to the Nube iO cloud.
- **Protocol Support**: Handling protocols such as LoRa, Modbus, and BACnet.

**Default Ports:**

- **HTTP**: Port 1660
- **HTTPS**: Accessible via `rb-YOURACCOUNT.nube-iiot.com`

### Rubix Bios

Rubix Bios facilitates seamless interactions with the Rubix OS. Its primary function includes:

- **OS Updates**: Managing and deploying updates to the Rubix OS.

**Default Ports:**

- **HTTP**: Port 1659
- **HTTPS**: Port 443, accessible via `rb-YOURACCOUNT.nube-iiot.com`

### Rubix Edge Wires

Rubix Edge Wires is a block logic Building Automation Control runtime designed for:

- **HVAC Control**: Managing heating, ventilation, and air conditioning systems.
- **Lighting Systems**: Controlling and automating lighting solutions.
- **Flow-Based Programming**: Creating function block logic programs for building management systems (BMS) or direct digital control (DDC).

**Default Port:**

- **HTTP**: Port 1665

## Additional Services and Drivers

### BACnet Driver

Supports the BACnet communication protocol for both master and device configurations.

**Default Port:**

- **UDP**: Port 47808

### LoRa Driver

Enables wireless communication for Nube iO LoRa sensors and other devices.

**Note**: LoRa and LoRaWAN are distinct protocols. For third-party LoRaWAN devices, a compatible driver and gateway are required.

### Rubix Compute I/O Driver

Facilitates communication with Rubix Compute I/O hardware.

**Default Port:**

- **HTTP**: Port 5001

### VPN Service

Provides a secure VPN connection for Rubix Compute devices to communicate with the Nube iO Cloud.

**Default Port:**

- **TLS**: Port 443

### MQTT Broker

Utilized for internal service communications within the Rubix ecosystem.

**Default Port:**

- **TCP**: Port 1883

### LoRaWAN Dashboard

A web-based interface for managing the LoRaWAN server.

**Default Port:**

- **HTTP**: Port 8080

## Deployment Options

Rubix CE components can be deployed in two ways:

- **Cloud** – Runs within the Nube iO cloud for remote access and management.
- **Rubix Compute** – Operates locally on Rubix Compute devices for on-premises control.

## Port Forwarding for Remote Access

For remote access, ensure the following ports are configured for port-forwarding:

| Service Name      | Port | Requirement                        |
| ----------------- | ---- | ---------------------------------- |
| Rubix OS          | 1660 | Mandatory                          |
| Rubix Bios        | 1659 | Mandatory                          |
| OpenVPN           | 443  | Mandatory when using Nube iO Cloud |
| LoRaWAN Dashboard | 8080 | Optional                           |

By configuring these components and services appropriately, users can fully leverage the capabilities of the Rubix CE platform for efficient building automation and management.