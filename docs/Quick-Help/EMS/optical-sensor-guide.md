---
sidebar_position: 4
---

# Optical Sensor Installation and Commissioning Guide

# 1. Powering and Installing the Gateway
This section will outline the process required to power and install the gateway.

:::info
If the gateway is already installed onsite please proceed to section 2.
:::

## 1.1 Re-attaching the Aerials
Before powering on the gateway, ensure the LoRa and 4G aerials are securely screwed into their correctly labeled ports on top of the gateway. The LoRa aerial is identifiable by two lines around its base (see Images 1 and 2).

<img src={require("./img/wm-img/image1-cropped.png").default} width="50%" />
<img src={require("./img/wm-img/image2-cropped.png").default} width="50%" />

<br/>

<br/>

The aerials are stored inside the enclosure during shipping to prevent damage. To access them, unscrew the four corner screws on the enclosure lid (these are only finger-tight when shipped). (See images 3 and 4)

<img src={require("./img/wm-img/image3-cropped.png").default} width="50%" />
<img src={require("./img/wm-img/image4-cropped.png").default} width="50%" />

<br/>

<br/>

During this step confirm the circuit breaker is in the 'ON' position before re-installing the enclosure lid. The up position is when the circuit breaker is ON. (See Image 5)

<img src={require("./img/wm-img/image5-cropped.png").default} width="70%" style={{ display: "block", margin: "0 auto" }} />

<br/>

## 1.2 Installing the Gateway
If securing the gateway to a wall, use four fixings - one in each corner of the enclosure. The choice of fixings will depend on the wall material.

If wall-mounting is not required, ensure the gateway is stored in a safe and secure location, free from any stress on the power cable.

## 1.3 Powering the Gateway
The gateways come with a pre-wired 3-pin plug. Simply connect this to a power outlet and switch it on. Allow up to 5 minutes for the 4G router and Rubix Compute to power up completely.

<br/>

<br/>

# 2. Optical Sensor Activation

## 2.1 Optical Sensor Contents
Open the Optical sensor box and confirm the following components are present:
- Optical sensor
- 1 x Optical Pulse Cable (pre-wired to the Optical sensor)
- 1 x LoRa Antenna
- 1 x 3.6V Lithium Battery
- 4 x 3M Adhesive Velcro Pads 
- 1 x LoRa F to F Adapter (optional)
- 1 x LoRa Extension Cable (optional)

<img src={require("./img/op-img/optical-contents.png").default} width="70%" style={{ display: "block", margin: "0 auto" }} />

<br/>

## 2.2 Activating the Optical Sensor
Once the gateway is powered, you may also power the Optical sensor by connecting the battery to its terminal. The Optical sensors will restart their data transmission and automatically rejoin the server.

***Insert Image of Components***

# 3. Sensor Installation
After restoring power to both the gateway and Optical, the optical pulse cable can be stuck over the OP1 or Pulse 1 terminal on the EDMI Electrical meter using the following steps:
1. For optimal performance, install the aerial vertically, ensuring it is free from obstructions.
    1. When mounting the Optical sensor with Velcro, ensure the surface is clean and dry. Peel the backing strips off one side of the Velcro pads and stick them to the back of the Optical sensor. Then, remove the remaining backing strips and press the Optical sensor firmly against the wall or surface where it will be mounted. Maintain firm pressure for approximately 30 seconds to ensure a strong bond.
    2. When mounting the Optical sensor with wall fixings, position it close enough to the EDMI meter to prevent cable damage from sagging, potential trips, or tangling. Hold the Optical in place and mark the wall for drilling. Drill the holes and secure the Optical to the wall using appropriate fixings ensuring it is free from obstructions.
    3. If using cable ties, the cable ties can be looped through the mounting holes on each side and then looped around the mounting surface. Ensure the cable ties are tight enough to hold the Optical securely in place, but not so tight that they damage the cable or the Optical sensor.  
2. Clean the area around the OP1 or Pulse 1 LED on the meter with a clean cloth to remove any dust or debris.
3. Peel the backing off the optical pulse cable and stick it over the OP1 or Pulse 1 LED on the meter. Ensure the cable is aligned with the LED and pressed firmly to ensure a good connection.
4. Once the optical pulse cable is in place, check that it is securely attached and not loose. If necessary, use cable ties to secure the cable to the meter or surrounding area to prevent it from moving or becoming dislodged.
5. If necessary, use the LoRa SMA Adapter and LoRa Extension Cable to extend the LoRa Antenna away from the Optical sensor and the meter to a more suitable location (eg external to the switchboard). Ensure the extension cable is securely connected to both the Optical sensor and SMA adapter, and that it is not loose or dangling. If required seal the adaptor penetration point with silicone to prevent water ingress and use cable ties to secure the extention cable to the surrounding area to prevent it from moving or becoming dislodged.

***Insert Example installation Images***

<!-- <img src={require("./img/wm-img/image6-cropped.png").default} width="50%" />
<img src={require("./img/wm-img/image7-cropped.png").default} width="50%" />    -->
  

<br/>

# 4. Commissioning
After installation, the Optical sensor requires a signal check and a Rate of Change Validation test. This test aligns the calculated and physical meter readings, ensuring they remain within tolerance by recording start and end values as electrical usage (kWh) accumulates on the meter.

## 4.1 Optical Signal Strength Check 

### 4.1.1 RSSI
For optimal performance, the Optical sensors Received Signal Strength Indicator (RSSI) should not exceed -115. An RSSI greater than this may lead to signal dropouts and data loss. For instance, an RSSI of -121 indicates poor signal and necessitates the installation of a more suitable antenna and/or antenna location. If the RSSI is poor, try improving the signal by repositioning the Optical and/or the Gateway.

If the signal does not improve, please contact Nube-iO Support on 0499 949 449.

### 4.1.2 SNR
For optimal performance, the Optical sensors Signal-to-Noise Ratio (SNR) should be greater than 0. For moderate performance, the SNR should be greater than -10. A low SNR may indicate high interference in the area, which can lead to signal dropouts and data loss. For instance, an SNR of -12 indicates high interference in the area and necessitates the installation of the LoRa antenna extension to a more suitable location.

If the signal does not improve, please contact Nube-iO Support on 0499 949 449.

## 4.2 Entering the Initial Meter Reading Values (Start Values)
To generate an accurate Calculated Meter Reading within the virtual system, each meter requires the input of specific 'Start Value' parameters. These parameters are:
- kWh Per Pulse 
- Start Pulses
- Start Meter Reading

Before entering any details, ensure the commissioned site is located on the Rubix CE platform and you are logged into the correct controller.

***Update Image***

<img src={require("./img/wm-img/image10-cropped.png").default} width="80%" style={{ display: "block", margin: "0 auto" }}/> 

<br/>

<br/>

Enter values in any of the 'Start Values' section by right clicking on the point and then select 'write point'. This will open the priority array where the start value can be entered. Clicking the 'send' button will write this value into the program.

***Update Image***

<div style={{ display: "flex", flexDirection: "column", gap: 0, margin: 0, padding: 0 }}>
    <img src={require("./img/wm-img/image11-cropped.png").default} width="80%" style={{ display: "block", margin: "0 auto" }} />
    <img src={require("./img/wm-img/image12-cropped.png").default} width="80%" style={{ display: "block", margin: "0 auto" }} />
</div>

<br/>

<br/>

### 4.2.1 kWh Per Pulse
The "kWh per pulse" value is often expressed as a ratio (e.g., 5 kWh per pulse as 5:1 or 1:5), and can be found in the pulse counter's support documentation or on the electricity meter's display. The values are typically 1, 5, or 10. (See T-Probe image as an example)

Typical Mk10A and MK10E Pulse constants:
- 1000 imp/kWh → 1 Wh per pulse 
- 100 imp/kWh → 10 Wh per pulse 
- 10 imp/kWh → 100 Wh per pulse 
- 1 imp/kWh → 1 kWh per pulse

***Update Image***

<img src={require("./img/wm-img/tprobe-pulses.png").default} width="80%" style={{ display: "block", margin: "0 auto" }}/> 

<br/>

<br/>

### 4.2.2 Start Pulses
The start pulses also need to be entered into the Rubix CE software when commissioning the meter. This value, found in the most up-to-date Micro Edge payload, should reflect the water meter's current pulse count to account for any water flow before commissioning, thereby aligning the meter reading with the current pulses.

***Update Image***

<img src={require("./img/wm-img/image13-cropped.png").default} width="80%" style={{ display: "block", margin: "0 auto" }}/>

<br/>

<br/>

### 4.2.3 Start Water Meter Reading
The Start Water Meter reading needs to be entered into Rubix CE to match the physical meter reading at the start time of the commissioning process. This needs to be as accurate as possible as this will be the value that accumulates in the software moving forward. See example below and note that as the dial has not yet rolled past the 6 the current reading entered is 5.

***Update Image***

<img src={require("./img/wm-img/image14-cropped.png").default} width="100%" style={{ display: "block", margin: "0 auto" }}/>

<br/>