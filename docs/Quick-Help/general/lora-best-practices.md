---
sidebar_position: 1
---

# LoRa Wireless Best Practices

# 1. Introduction
This document provides best practices for deploying LoRa wireless networks, including tips for optimizing signal strength, minimizing interference, and ensuring reliable communication between devices.

Nube-IO makes no guarantees based on the accuracy or completeness of the contents of this document and reserves the right to make changes to specifications and product descriptions at any time without notice.

Before making decisions based on the information within this document please consult an RF planning expert.

<br/>

# 2. Key Concepts

## 2.1 Free space path losses
In telecommunication, free-space path losses (FSPL) is the loss in signal strength of an electromagnetic wave that would result from a line-of-sight path through free space (usually air), with no obstacles nearby to cause reflection or diffraction. It does not include factors such as the gain of the antennas used at the transmitter and receiver, nor any loss associated with hardware imperfections.

Free-space path loss is proportional to the square of the distance between the transmitter and receiver, and also proportional to the square of the frequency of the radio signal. Even if no other sources of attenuation or impairment are assumed, a transmitted signal attenuates over distance because the signal is being spread over a larger area. This form of attenuation is known as free space loss, which can be expressed in terms of the ratio of the radiated power to the power received by the antenna or, in decibels, by taking 10 times the log of that ratio.

The formula to work out free space path loss is:

<img src={require("./img/lora-fspl.png").default} width="50%" />

<br/>

## 2.2 Fresnel Zone
The Fresnel zone is an elliptical shaped body around the direct line of sight path between the end node and the gateway. Any obstacle within this volume, for example buildings, trees, hilltops or ground can weaken the transmitted signal even if there is a direct line of sight between the end node and the gateway. Try to avoid having objects within this area.

<img src={require("./img/fresnelzone1.png").default} width="70%" />

<br/>

<br/>

As a rule of thumb, the Fresnel zone should always be clear of obstruction, but this can be impractical. It is said that beyond 40% blockage, signal loss will become significant.
<img src={require("./img/fresnelzone2.png").default} width="70%" />

<br/>

<br/>

The formula to calculate minimum height for 60% clear:
<img src={require("./img/fresnelzone3.png").default} width="70%" />

<br/>

<br/>

## 2.3 LoRa Link Budget
LoRa link budget is the sum of all of the gains and losses from the transmitter, through the medium (e.g. free space), to the receiver in a telecommunication system. It is a way of quantifying the link performance.
The receiver sensitivity is the lowest power level at which the receiver can receive or demodulate the signal.

<img src={require("./img/lora-link-budget1.png").default} width="70%" />

<br/>

<br/>

## 2.4 RSSI
The Received Signal Strength Indication (RSSI) is the received signal power in milliwatts and is measured in dBm. This value can be used as a measurement of how well a receiver can hear a signal from a sender.
RSSI is an arbitrary value set by the chipset manufacturer, whereas absolute dBA is the actual raw measurement of the signal strength.
Typical RSSI values are:

RSSI minimum = -120 dBm.
- If RSSI=-30dBm: signal is strong.
- If RSSI=-120dBm: signal is weak.

<img src={require("./img/rssi1.png").default} width="75%" />

<br/>

<br/>

## 2.5 SNR (Signal-To-Noise Ratio)
SNR or signal-to-noise ratio is the ratio between the desired information or the power of a signal and the undesired signal or the power of the background noise.

<img src={require("./img/snr1.png").default} width="50%" />

The noise floor is an area of all unwanted interfering signal sources which can corrupt the transmitted signal and therefore re-transmissions will occur.
- If SNR is greater than 0, the received signal operates above the noise floor.
- If SNR is smaller than 0, the received signal operates below the noise floor.

Normally the noise floor is the physical limit of sensitivity, however LoRa works below the noise level.

Typical LoRa SNR values are between: -20dB and +10dB. A value closer to +10dB means the received signal is less corrupted. LoRa can demodulate signals which are -7.5 dB to -20 dB below the noise floor.

<br/>

<br/>

# 3. Antenna Positioning

## 3.1 Antenna Height
The gateway/antenna should be positioned as high as practicable, with as few obstructions as possible in its path. Ideally, this would be on top of a tower, but that is not always feasible. Other alternatives include a high position on a roof or a post. Placement on the side of a tall structure is less desirable but still achievable.
The key consideration with all sites should be line of sight to the sensors. LoRa is a long-distance communication technology, however the more obstructions between the sensors and the gateway, the shorter the range becomes. Hills, trees, and buildings reflect and obstruct the signal and should be considered when positioning the gateway/antenna.


## 3.2 Clear Obstacles in the Antenna Vicinity
Walls, electrically conducting objects and electronic devices (e.g. PC, monitor, LED lighting…) located in the immediate vicinity of an antenna “detune” and degrade its performance. For the transmitter antenna, these obstacles absorb power from the radiation field, thereby decreasing the effective transmission power and operating distance. For the receiver antenna, they influence its directivity and raise the noise level.

While the absolute minimum distance is 6 cm, a common best practice is maintaining at least 70 cm distance between antennas and any obstacles. External antennas must be mounted on a pole rather than at the side of a building.


## 3.3 Antenna Orientation
Antenna orientation refers to the positioning of the antenna, whether that be vertical or horizontal. Antennas can be generally classified into two main groups - directional and omnidirectional. The most used antenna is omnidirectional and sends out a signal in all directions.

Accurate antenna orientation is important to ensure maximum coverage. Due to variation in radiation patterns, different antenna types should be oriented differently. Omnidirectional antennas should be oriented vertically to get the most effective range. If the antenna must be placed horizontally, it should be placed at 90 degrees to the  receiver. Confirm that the polarisation of the receiver antenna matches that of the transmitter antenna to optimise signal reception.

<br/>

<br/>

# 4. Gateway Positioning

## 4.1 Centralised Gateway
The position of the gateway needs to be taken into consideration for improving signal reliability and signal quality. The gateway should be in a position central to the most number of nodes possible. This ensures that blackspots or low signal zones are minimised and that the most number of nodes have a strong signal.


## 4.2 Coax Cable Extension
It might not be feasible, whether for accessibility, maintenance, or other reasons, to mount the gateway to the most appropriate location - this is where the use of extension coax cable is suitable. Coax cable can be used to mount the antenna far distances away from the gateway whilst maintaining functionality.

Coax cable comes in different radio guide measurement (RG) ratings, with each rating suitable for different requirements. There are different types of coaxial cable, which vary by gauge and impedance. Gauge refers to the cable’s thickness and is measured by the RG number. The higher the RG number, the thinner the central conductor core is.

Another benefit of coaxial cable is the electromagnetic field carrying the signal exists only in the space between the inner and outer conductors. This means coaxial cable can be installed next to metal objects without losing power, unlike other types of transmission lines as well as increased resistance to electromagnetic interference.

<br/>

<br/>

# 5. Nodes Positioning

## 5.1 Internal Antenna

An internal antenna is self-contained within the node. The benefit of this is that the node is smaller and no external mounting antennas are needed. Due to the compact nature of the internal antenna, signal strength will not be as strong as nodes with external or extended antennas.

## 5.2 External Antenna
An external antenna is an antenna mounted on the outside of the node. External antennas protrude out of the node. The benefit to external antennas is that signal strength is better than that of internal antennas. The type of antenna can be changed for each use case, with a selection of sizes and types available, allowing specific scenarios to be adapted to.

## 5.3 Extended Antenna
Due to environmental factors such as concrete obstructions, only available placement of the gateway in relation to the node, aesthetical reasons, or signal strength, it is not always possible to use internal or external antennas. In these situations, a suitable option would be to use an extended antenna. An extended antenna is attached to the node via the desired length of coaxial cable and is placed in a more appropriate position.

# 6. Antenna Selection

## 6.1 Antenna Gain
Antenna gain is the ratio of the power of a signal that has been transmitted and then received to the initial power. The higher the gain the narrower and further the effective signal coverage will be, shown in the figure below. For indoor applications, lower gain antennas are generally used as they allow for greater flexibility of sensors and gateways, while high gain antennas are generally used for outdoor multi building applications.

<img src={require("./img/antenna-gain1.png").default} width="70%" />

## 6.2 Omni vs Directional Antennas
There are two types of antennas: omnidirectional and directional. Omnidirectional antennas send and receive signals equally in all directions, while directional antennas only emit signals in one direction. Which type of antenna is best depends on your specific needs, but there are some general guidelines that can help make the decision easier. Because of the inherent trade-off between utility and signal strength, the antenna type you choose is usually determined by your network and applications.

Omnidirectional antennas give you more flexibility regarding device and gateway placement. A directional antenna may be appropriate if your transmitter and gateway are fixed and the direction of data communications is well defined. Directional antennas have substantially better signal strength than omnidirectional antennas. This is due to the fact that the transmission energy is concentrated in one direction rather than being spread across the system. As a result, undesired interference can be eliminated, and signal strength can be improved with less energy.

<br/>

<br/>

# 7. General Rules

## 7.1 Evaluate Installation Site

### Gateway/Antenna

- Centralise gateway/antenna.
    - Extend antenna cable to allow better positioning.
    - Separate gateway with ethernet backbone.
- Select an appropriate antenna for both gain and direction.
- Orient the antenna for optimal coverage and to match sensors.
- The antenna should be at a height to meet the 60% clear Fresnel zone.
- The antenna should have a clearance of at least 6 cm.

### Sensors

- Calculate LoRa link budget for sensor position.
- Orient the antenna to match the gateway.
- The antenna should be at a height to meet the 60% clear Fresnel zone.
- Use external antenna when available.
- Extend antenna cable to allow better positioning.

<br/>

<br/>

# 8. Quick Reference / Tables

## 8.1 Obstacle Penetration

<img src={require("./img/obstacle-penetration.png").default} width="70%" />

## 8.2 Free Space Losses

<img src={require("./img/free-space-losses.png").default} width="70%" />

## 8.3 Fresnel Zone (Minimum Height for 60% Clearance)

<img src={require("./img/fresnelzone4.png").default} width="70%" />

## 8.4 Example Office Installation

<img src={require("./img/lora-example-office.png").default} width="100%" />
<img src={require("./img/lora-example-office-table.png").default} width="100%" />

