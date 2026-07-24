# Zoneconnex Quick Start Guide

# 1. Overview/About Product

## 1.1. Product Overview
The ZoneConnex System is Nube iO's integrated HVAC zone control solution for split ducted air conditioning systems in residential and light commercial environments. It combines the ZoneConnex controller, the anywAiR Zone mobile app, and the Touch Point LCD screen to provide flexible local and mobile control of zoned HVAC systems.

Installers can quickly commission and configure the system using the mobile app via a direct Wi-Fi connection, while users can monitor and adjust temperature setpoints, operating modes, and zone airflow through either the mobile app or the wall-mounted LCD interface.

## 1.2. Architecture
- **ZoneConnex Controller:** The master device that communicates with compatible RAC/PAC and VRF air conditioning units via the UART protocol to manage system operation and control.
- **Touch Point LCD:** Wall-mounted touchscreen for local control and monitoring of the air conditioning system.
- **anywAiR Zone Mobile App:** Mobile interface for remote control and monitoring.
- **Droplet (sold separately):** Wireless LoRa sensor that monitors temperature and humidity in each zone, enabling individual zone monitoring.

## 1.3. Product Features

**Zoneconnex**
- **Wireless Connectivity:** Wi-Fi 2.4 GHz and Bluetooth 4.2.
- **Ethernet:** 2x 100 Mbps RJ45 Ethernet ports for LAN connection.
- **RS-485:** 2x RS485 ports — 1x isolated RS-485 (third-party field-bus) and 1x RS-485 (TouchPoint LCD Modbus).
- **Zone Control Ports:** Supports 10x RJ12 24VAC dampers up to 150mA each.
- **TouchPoint LCD Integration:** Provides an 18VDC power source and Modbus connection point for the TouchPoint LCD.
- **LoRa® & LoRaWan:** Supports LoRa and LoRaWan communication.

**TouchPoint LCD**
- **Wireless Connectivity:** Wi-Fi 802.11 b/g/n.
- **RS-485:** 1x RS485 Modbus communication port.
- **DC Power:** 18VDC power input port.
- **USB-C:** Service / programming port for managing the TouchPoint LCD firmware.

<br/>

# 2. Hardware Overview

## 2.1. Zoneconnex Dimensions

|                |                                           |
|----------------|-------------------------------------------|
| Height:        | 105.31 mm (134.1 incl. clips) / 4.15 inches (5.27 incl. clips) |
| Width:         | 111.84 mm / 4.40 inches                   |
| Depth:         | 70.25 mm (72.95 incl. clips) / 2.76 inches (2.87 incl. clips) |
| Enclosure:     | PC/ABS blend (Flame Retardant Grade, UL94 V-0) Matte Black, IP2X Rated |

![max800px](Zoneconnex/img/ZoneConnex-Dimensions.png)

## 2.2. Packing List

Please check the package contents to verify that you have received the items below:
- Zoneconnex Quick Start Guide
- Zoneconnex Controller
- Touch Point LCD
- Wi-Fi Antenna
- LoRa Antenna
- 24VAC Power Supply
- 15m 4-core 24 AWG LCD power/communication cable
- 2m PAP-04V-S UART communication cable
- Pan head self tapping screws (8x M3 x 25mm)

## 2.3. Zoneconnex Controller Introduction

### 2.3.1 Zoneconnex Front View
- 24VAC/DC Power Input: Termination block for connecting the ZoneConnex 24VAC/DC power input.
- U.FL LoRa Antenna: Connects the antenna for LoRa & LoRaWan communication.
- Wi-Fi Antenna: Connects the antenna for Wi-Fi communication.
- Din Rail Clip: Allows for secure din rail mounting and maintenance.
- Mounting Clips: Allows for secure mounting via use of appropriate fixings.
- UART Port: Termination block for connecting the ZoneConnex to UART communication.
- RS485-ISO: Termination block for connecting third party field-bus communication devices to the ZoneConnex.
- LCD RS485: Termination block for connecting the TouchPoint LCD Modbus communication to the ZoneConnex.
- LCD 18VDC Power: Termination block for powering the TouchPoint LCD from the ZoneConnex.

![max800px](Zoneconnex/img/ACB-ZC-Components-Markup-Front-View-rev3.png)

### 2.3.2 Zoneconnex Top View
- 24VAC/DC Power Input: Termination block for connecting the ZoneConnex 24VAC/DC power input.
- Wi-Fi Antenna: Connects the antenna for Wi-Fi communication.
- Zone Control Ports 1-5: RJ12 outputs to supply 24V AC to control the zone dampers.
- USB-C: Service / programming port used to manage the ZoneConnex firmware.
- 6-Pin STM32 Port: STM32 service / programming port used to manage the ZoneConnex firmware.
- ACBM Reset Button: Used to restart (reboot) the ACBM control board.
- ACBM User Button: Performs a factory reset, clearing all persisted data.
- Zone Control Reset Button: Used to restart (reboot) the Zone Control IO board.
- Zone Control Button: Performs a factory reset, clearing all persisted data.

![max800px](Zoneconnex/img/ACB-ZC-Components-Markup-Top-View-rev3.png)

### 2.3.3 Zoneconnex Bottom View
- Zone Control Ports 6-10: RJ12 outputs to supply 24V AC to control the zone dampers.
- U.FL LoRa Antenna: Connects the antenna for LoRa & LoRaWan communication.
- RJ45 Ethernet Port 1: 100 Mbps RJ45 Ethernet Port for LAN connection.
- RJ45 Ethernet Port 2: 100 Mbps RJ45 Ethernet Port for LAN connection.
- UART Port: Termination block for connecting the ZoneConnex to UART communication.
- RS485-ISO: Termination block for connecting third party field-bus communication devices to the ZoneConnex.
- LCD RS485: Termination block for connecting the TouchPoint LCD Modbus communication to the ZoneConnex.
- LCD 18VDC Power: Termination block for powering the TouchPoint LCD from the ZoneConnex.

![max800px](Zoneconnex/img/ACB-ZC-Components-Markup-Bottom-View-rev3.png)

<br/>

## 2.4. Touch Point LCD Introduction

### 2.4.1 LCD Screen
- 18V DC Power Input: Terminals for powering the Touch Point LCD from the ZoneConnex.
- Wi-Fi Antenna: Connects the antenna for Wi-Fi communication.
- RS485 Connection: Terminals for connecting the Touch Point LCD to the ZoneConnex via RS485 communication.
- USB-C: Service / Programming Port used to manage the Touch Point LCD firmware.
- Reset Button: Used to perform a soft reset on the Touch Point LCD.

![max800px](Touch%20Point%20LCD/img/LCD-Internal-Labelled.jpg)

<br/>

# 3. Installation

## 3.1 Mounting

### 3.1.1 Zoneconnex DIN Rail Mounting
1. Ensure the DIN rail is securely installed inside your enclosure or control panel.
2. Hang the top of the ZoneConnex onto the top edge of the DIN rail.
3. Pivot the bottom of the controller toward the rail and snap the lower clip into place.
4. Gently pull the controller forward to confirm it is securely mounted.

![max800px](Zoneconnex/img/ZoneConnex-DinMounting-v2.png)

### 3.1.2 Zoneconnex Wall Mounting
1. Attach the mounting clips to the back of the ZoneConnex (if not pre-fitted).
2. Hold the controller against the wall and mark the fixing points using the clips as a guide.
3. Drill the holes and insert wall plugs if needed.
4. Secure the Zoneconnex to the wall with screws or fixings.
5. Gently pull the controller forward to confirm it is firmly mounted.

![max800px](Zoneconnex/img/ZoneConnex-FixingMounting-v2.png)

### 3.1.3 Touch Point LCD Mounting
The TouchPoint LCD can be mounted via fixings utilising the mounting holes incorporated in the LCD housing. The TouchPoint LCD should always be mounted in a location such that it will not experience extreme high or low temperatures, liquids or high humidity.

Release the two bottom clips to remove the LCD from its housing. Hold the housing against the wall & mark the fixing points. Drill holes & insert wall plugs if needed. Secure the housing to the wall with screws. Feed the pre-wired cable through the desired entry point. Re-insert the LCD by: Engaging the top clips first, then pressing the bottom clips into place.

![max800px](Touch%20Point%20LCD/img/LCD-Mounting-v3.png)

<img src={require("./Touch Point LCD/img/Top-Retaining-Clips-v2.png").default} width="50%" />
<img src={require("./Touch Point LCD/img/Bottom-Retaining-Clips-v2.png").default} width="50%" />

![max1000px](Touch%20Point%20LCD/img/LCD-Clip-Release-v2.png)

|**Correct**            | **Incorrect**                           |
|-----------------------|-----------------------------------------|
|Insert a flat blade screwdriver onto the angled edge of the retaining clip (furthest from the LCD screen) and gently lever the clip away from the housing.| Do not insert the screwdriver into the slot closest to the LCD screen, as the clip cannot be safely or effectively levered away from the housing in this position. |

<br/>

## 3.2 Zoneconnex Connections

> ⚠️ **Please note:** The Air Conditioning unit should be isolated and off prior to any power & wiring.

### 3.2.1 Zoneconnex Power Supply
The ZoneConnex is powered by a 24V AC power supply on the 24VAC power terminals (1 & 2) as shown below. The unit is supplied with a prewired power supply.

|            | ![max300px](Zoneconnex/img/ZC-24VAC-DC-Wiring.png) |
|----------- |----------------------------------------|
| Pin 1 **(L)** | 24V AC **Live (L)** |
| Pin 2 **(N)** | 24V AC **Neutral (N)** |

![max800px](Zoneconnex/img/24VAC-ADAPTOR-BOLD-2.png)

### 3.2.2 UART Connection
The Zoneconnex is equipped to interface with compatible RAC/PAC and VRF Air Conditioning units via the UART protocol. Route the UART cable into the Air Conditioning unit control panel and connect it to the **CN65** or **CN75** port via the UART interface. The UART connection is terminated and installed as shown below.

|            | ![max300px](Zoneconnex/img/ZC-UART-Wiring.png)     |
|----------- |----------------                        |
| Pin 3 (**G**) | **Ground** of UART Network       |
| Pin 4 (**RX**) | **RX** of UART Network       |
| Pin 5 (**TX**) | **TX** of UART Network                 |
| Pin 6 (**Spare**) | NOT USED                     |

![max1000px](Zoneconnex/img/ACB-ZC-UART-PAP-04V-S-rev3.png)

![max300px](Zoneconnex/img/UART-Cable-photo.jpg)

### 3.2.3 RS485-ISO
The RS485-ISO allows connection of third-party field-bus devices to the ZoneConnex. The RS485 connector is terminated and installed as shown below.

|            | ![max300px](Zoneconnex/img/ZC-RS485-ISO-Wiring.png)     |
|----------- |----------------                        |
| Pin 7 (**+**) | **A** or **+** of RS485 Network       |
| Pin 8 (**-**) | **B** or **-** of RS485 Network        |
| Pin 9 (**G**) | **C** or **Ground**                    |

### 3.2.4 LCD RS485 & Power Supply
The LCD RS485 connects the Touch Point LCD to the ZoneConnex, and the ZoneConnex supplies 18V DC to power the LCD via the LCD 18VDC Power terminals. Connect the 15m 4-core 24 AWG LCD power/communication cable between the TouchPoint LCD and Zoneconnex as shown below.

![max300px](Zoneconnex/img/LCD-Cable-photo.jpg)

|            | ![max300px](Zoneconnex/img/ZC-LCD-RS485-Wiring.png)     |
|----------- |----------------                        |
| Pin 10 (**+**) | **A** or **+** of RS485 Network       |
| Pin 11 (**-**) | **B** or **-** of RS485 Network        |
| Pin 12 **(+)** | 18V DC **+** |
| Pin 13 **(-)** | 18V DC **−** |

<br/>

## 3.3 Touch Point LCD Connections

The Touch Point LCD utilises **Push-To-Release** terminals. Gently press down on the terminal pin to release the clamp, insert or remove the cable, then release the pin to lock the cable in place. The LCD is powered by an 18V DC connection supplied by the Zoneconnex and communicates via a Modbus RS485 connection. The pins are terminated and installed as shown below.

|            | ![max300px](Touch%20Point%20LCD/img/LCD-Wiring-Terminations.png) |
|----------- |----------------------------------------|
| Pin 1 (**A** or **+**) | **A** or **+** of RS485 Network       |
| Pin 2 (**B** or **-**) | **B** or **-** of RS485 Network        |
| Pin 3 (**+**) | 18V DC **+** |
| Pin 4 (**-**) | 18V DC **−** |

<br/>

# 4. Configuration

## 4.1 anywAiR Zone Mobile App

Scan the QR code below to download the anywAiR Zone Mobile App for iOS or Android.

| Android | iOS |
|-|-|
| ![max300px](img/googleplay-qr-code.png) | ![max300px](img/iOS-anywair-zone-qr-code.png) |
| <a href="https://play.google.com/store/apps/details?id=com.nubeio.mia"> ![max300px](MIA%20Mobile%20App/img/google-play-icon.png) </a> | <a href="https://apps.apple.com/au/app/anywair-zone/id6748876162"> ![max300px](MIA%20Mobile%20App/img/Apple-app-download-icon.png) </a> |

<br/>

## 4.2 Wifi Configuration

1. On the Touch Point LCD, press **Wi-Fi**.
2. If no network is connected, press **Scan Wi-Fi** to search for available networks.
3. Select your desired network and press **Connect**.
4. Enter the network password using the on-screen keyboard, then press **Connect**.
5. Once connected, the Wi-Fi setup screen will show the network and connection details, including QR code, signal strength, speed, security type, and channel.

![max300px](Touch%20Point%20LCD/img/LCD-Screenshots/No-Wifi.png)
*Scan Wi-Fi*

![max300px](Touch%20Point%20LCD/img/LCD-Screenshots/Wifi-Info.png)
*Connection details*

## 4.3 Installer Mode

To access installer mode, follow the prompts below in accordance with the Installer Mode anywAiR Zone Mobile App workflow:

1. On the TouchPoint LCD home screen, tap the **Settings** icon.
2. On the settings/about screen, tap the **System** card **8 times**.

![max800px](Touch%20Point%20LCD/img/LCD-Screenshots/Tap-Settings-8x-Card.svg)

3. Enter the **installer password (default 898989)** and confirm.
4. Open the **anywAiR Zone Mobile App**. Select **Continue as Installer**. Scan the **left QR** for connecting to Zoneconnex Access Point Wi-Fi.

![max800px](Touch%20Point%20LCD/img/LCD-Screenshots/Installer-Connection-LeftQR.svg)

5. Once connected to the Zoneconnex Access Point Wi-Fi, scan the **right QR** to access installer mode for the Zoneconnex.

![max800px](Touch%20Point%20LCD/img/LCD-Screenshots/Installer-Connection-RightQR.svg)

**Note:** To exit Installer Mode at any time, press **Exit Installer Mode** in the app.

<br/>

## 4.4 Zone Configuration
By default, zones are configured in a 1:1 pairing with dampers (Zone 1 to Damper 1, and so on up to 10 zones), allowing quick commissioning with minimal configuration. If required, zone-to-damper assignments can be customised during the zone configuration.

Use the following steps to complete the zone configuration from the Installer menu on the anywAiR Zone app:

1. Enter the total Number of Zones and required Relief Zones, then press **Next**.
2. Select the required Relief Zones, then press **Configure Zones**.
3. Configure the first zone:
    - Set Zone Name.
    - Enable Primary Zone (if required).
    - Enable Relief Zone (if required).
    - Toggle Zone Power to test control.
    - Set Minimum and Maximum Airflow (%).
    - Add/remove Dampers and Droplets (sold separately; the Zoneconnex is rated to support RJ12 24VAC dampers up to 150mA).
4. Press **Next** to save the zone settings.
5. Repeat zone configuration for all remaining zones (press **Back** if needed to return to the previous zone).
6. On the final zone, press **Complete** to finish and open the Zones screen for monitoring and control.

<br/>

## 5. User Manuals

For full setup instructions and product documentation, scan the QR code below.

[![max300px](img/onlinedocs-qr-code.png)](https://nubeio.github.io/rubix-ce-docs/docs/overview)

<br/>
