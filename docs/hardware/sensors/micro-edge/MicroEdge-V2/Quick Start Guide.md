# MicroEdge Quick Start Guide

# 1. Product Overview

The MicroEdge is Nube iO’s multi-purpose wireless (LoRa®) IoT asset monitoring sensor. Designed to interface with low-level sensors, and pulse sensors (water, electrical, gas, etc.), in a small package, with minimum install time.
LoRa® wireless IoT technology provides a very long transmission range that is energy efficient and less susceptible to object interference than other wireless technologies.
The MicroEdge provides 3 analog Inputs and 1 Digital Pulse Accumulation Input. Values are sent wirelessly to the gateway controller, making installation hassle-free.
Powered by a 4000mAh battery, the MicroEdge has a runtime of 2 - 8 years depending on the configured push rate.


![max400px](img/MICROEDGE-Front.png)

## 1.3 Product Features
- **LoRa®:** Provides long-range, low-power wireless connectivity for IoT devices, easily penetrating walls and obstacles.
- **3 x Analog input:** 10k thermistor, digital / dry contact
- **1 x Digital pulse:** (Dry Contact or 3.3v max) accumulation
- **Battery:** Powered by a 4000 mAh battery for multi-year operation

<br/>

# 2. Hardware Overview

## 2.1 Packing List

Please check the package contents to verify that you have received the items below:
- MicroEdge Start Guide
- MicroEdge 
- 4000 mAh battery 
- LoRa Antenna

## 2.2 MicroEdge Introduction

### 2.2.1 External View

<br/>

![max800px](img%2Fexternal.png)

<br/>

### 2.2.2 Internal View

<br/>

![max700px](img%2Finternal.png)

<br/>

<br/>

# 3. Installation

<br/>

# 3.1 Mounting

1. Hold the MicroEdge against the wall and mark the fixing points using the mounting holes as a guide.  
3. Drill the holes and insert wall plugs if needed.  
4. Secure the MicroEdge to the wall with screws or fixings.  
5. Gently pull the controller forward to confirm it is firmly mounted.

![max700px](img/ME-Mounting.png)


<br/>

## 3.2 Connections

### 3.2.1 Battery Connection
Connect the battery to power the device; LEDs will flash briefly during activation and transmission, then turn off to save energy.


### 3.2.1 Universal & Pulse Inputs Connections
<!-- Universal Inputs: Can be used as analog or digital. Digital reads open/closed circuits (switches, buttons, relays), while analog reads sensor values like temperature, humidity, pressure, CO₂, or position.  -->

**Universal Inputs (UI1–UI3)** can be configured as:
- **Digital:** On/Off signals (e.g. switches, relays)  
- **Analog:** Resistive sensors (e.g. 10K thermistors)

> ⚠️ Max input voltage: **3.3V**

**Pulse Input:**
- Used for counting pulses (e.g. energy, water, or gas meters)

Refer to the example connections in the diagram below.

![max500px](img%2Fterminal.png)

<br/>

<br/>

<br/>

# 4. Dip Switch Configuration

The MicroEdge sensor includes a bank of 8 DIP switches used for configuration. To access them, remove the cover by loosening the four captive screws.

![max500px](img%2Fdips_ME.png)

* Switches 1-3: Control the LoRa® data push rate.
* Switch 6: Resets the pulse count.
* Switch 7: Activates test mode for device diagnostics.

DIP switches 1 to 3 are used to set the push rate of the MicroEdge sensor. After setting the desired push rate, press the reset button to apply the new configuration. 

**Note:** The **UP** position is active.

| Minutes | DIP Switch Position  |
|---------|-------------------| 
| 0.5     | ![max200px](img\dip1.png) |
| 1       | ![max200px](img\dip2.png) |
| 3       | ![max200px](img\dip3.png) |
| 5       | ![max200px](img\dip4.png) |
| 10      | ![max200px](img\dip5.png) |
| 15      | ![max200px](img\dip0.png) | 
| 30      | ![max200px](img\dip6.png) |
| 60      | ![max200px](img\dip7.png) |

<br/>

<br/>

## 5. Engineering Tool

Scan the QR code below to download the Rubix Computer Edition engineering software for MacOS, Windows or Linux.

[![max300px](img/CE-Releases-qr-code.png)](https://github.com/NubeIO/rubix-ce-builds/releases)

<!-- | Android | IOS |
|-|-|
| ![max300px](img/googleplay-qr-code.png) | ![max300px](img/testflight-qr-code.png) |
| <a href="https://play.google.com/store/apps/details?id=com.nubeio.mia"> ![max300px](MIA%20Mobile%20App/img/google-play-icon.png) </a> | <a href="https://testflight.apple.com/v1/app/6754748732?build=193360892"> ![max300px](MIA%20Mobile%20App/img/Apple-app-download-icon.png) </a> | -->

<br/>

<br/>

## 6. User Manuals 

For full setup instructions and product documentation, scan the QR code below.

[![max300px](img/ME-Docs-qr-code.png)](https://nubeio.github.io/rubix-ce-docs/docs/category/microedge-v2)

<br/>

<br/>

<!-- # 5. Document Revision

| Revision | Date       | Change Description                  |
|----------|------------|------------------------------------|
| 1.0      | 28-11-2025 | Initial release of the document.   |
| 1.1      | DD-MM-YYYY | Description of the next change.    |
| 1.2      | DD-MM-YYYY | Description of the next change.    | -->




