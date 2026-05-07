# Water Meter Installation and Commissioning Guide

# 1. Powering and Installing the Gateway
This section will outline the process required to power and install the gateway.

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

# 2. Micro Edge Re-activation
## 2.1 Re-activating the Micro Edge
Once the gateway is re-powered, you may also repower the Micro Edge by connecting the battery to its terminal. The Micro Edge sensors will restart their data transmission and automatically rejoin the server.

# 3. Sensor Installation
After restoring power to both the gateway and Micro Edge, the pulse cable can be wired into the Micro Edge's pulse terminal.

## 3.1 Fixing the Sensor to the Water Meter
1. For optimal performance, install the aerial vertically, ensuring it is free from obstructions.
2. To mount the Micro Edge, either cable ties or wall fixings should be used
    1. When mounting the Micro Edge with wall fixings, position it close enough to the wall to prevent cable damage from sagging, potential trips, or tangling. (See image 6 as an example)
    2. If using cable ties, the cable ties can be looped through the mounting holes on each side and then looped around the piping. (See image 7 as an example)

<img src={require("./img/wm-img/image6-cropped.png").default} width="50%" />
<img src={require("./img/wm-img/image7-cropped.png").default} width="50%" />   

<br/>

<br/>

## 3.2 Mount the Pulse Cable to the Water Meter
Always install each pulse cable according to the manufacturer's specifications, which should be provided with the unit.

## 3.3 Terminating the Pulse Cable into the Micro Edge
1. Feed the pulse cable into the Micro Edge via the 16mm gland on the bottom left.
2. The cable should then be cut down to length while still leaving an adequate service loop for any future adjustments.
3. The cores from the pulse counter get terminated into the green terminal slots labelled PULSE. (See image 8)

<img src={require("./img/wm-img/image8-cropped.png").default} width="70%" style={{ display: "block", margin: "0 auto" }} />  

<br/>

<br/>

## 3.4 Set Micro Edge Push Rate to 30 Seconds during Testing
Set the Micro Edge's push rate to 30 seconds for commissioning. To do so remove the Micro Edge cover and position dip switch #1 to the ON position and press the 'RST' button.

<img src={require("./img/wm-img/image9-cropped.png").default} width="70%" style={{ display: "block", margin: "0 auto" }} />  

<br/>

<br/>

# 4. Commissioning
After installation, the Micro Edge requires a Rate of Change Validation test. This test aligns calculated and physical meter readings, ensuring they remain within tolerance by recording start and end values as water flows through the meter.

## 4.1 Micro Edge Signal Strength Check (RSSI)
For optimal performance, the Micro Edge's Received Signal Strength Indicator (RSSI) should not exceed -115. An RSSI greater than this may lead to signal dropouts and data loss. For instance, an RSSI of -121 indicates poor signal and necessitates the installation of a more suitable antenna and/or antenna location. If the RSSI is poor, try improving the signal by repositioning the Micro Edge and/or the Gateway.

If the signal does not improve, please contact Nube-iO Support on 0499 949 449.

## 4.2 Entering the Initial Meter Reading Values (Start Values)
To generate an accurate Calculated Meter Reading within the virtual system, each meter requires the input of specific 'Start Value' parameters. These parameters are:
- Litres Per Pulse
- Start Pulses
- Start Meter Reading

Before entering any details, ensure the commissioned site is located on the Rubix CE platform and you are logged into the correct controller. 

<img src={require("./img/wm-img/image10-cropped.png").default} width="80%" style={{ display: "block", margin: "0 auto" }}/> 

<br/>

<br/>

Enter values in any of the 'Start Values' section by right clicking on the point and then select 'write point'. This will open the priority array where the start value can be entered. Clicking the 'send' button will write this value into the program.

<div style={{ display: "flex", flexDirection: "column", gap: 0, margin: 0, padding: 0 }}>
    <img src={require("./img/wm-img/image11-cropped.png").default} width="80%" style={{ display: "block", margin: "0 auto" }} />
    <img src={require("./img/wm-img/image12-cropped.png").default} width="80%" style={{ display: "block", margin: "0 auto" }} />
</div>

<br/>

<br/>

### 4.2.1 Litres Per Pulse
The "Litres per pulse" value is often expressed as a ratio (e.g., 5 litres per pulse as 5:1 or 1:5), and can be found in the pulse counter's support documentation or on the water meter's display. The values are typically 1, 5, or 10. (See T-Probe image as an example)

<img src={require("./img/wm-img/tprobe-pulses.png").default} width="80%" style={{ display: "block", margin: "0 auto" }}/> 

<br/>

<br/>

### 4.2.2 Start Pulses
The start pulses also need to be entered into the Rubix CE software when commissioning the meter. This value, found in the most up-to-date Micro Edge payload, should reflect the water meter's current pulse count to account for any water flow before commissioning, thereby aligning the meter reading with the current pulses.

<img src={require("./img/wm-img/image13-cropped.png").default} width="80%" style={{ display: "block", margin: "0 auto" }}/>

<br/>

<br/>

### 4.2.3 Start Water Meter Reading
The Start Water Meter reading needs to be entered into Rubix CE to match the physical meter reading at the start time of the commissioning process. This needs to be as accurate as possible as this will be the value that accumulates in the software moving forward. See example below and note that as the dial has not yet rolled past the 6 the current reading entered is 5.

<img src={require("./img/wm-img/image14-cropped.png").default} width="100%" style={{ display: "block", margin: "0 auto" }}/>

<br/>

<br/>

## 4.3 Rate of Change Test
A Rate of Change test must be carried out in order to verify that the physical meter and the start meter values entered in the Rubix CE program move in alignment when water moves through the meter. Before starting this test, adjust the Micro Edge push rate from 15 minutes to 30 seconds. Once the test is complete, revert the push rate to 15 minutes.

### 4.3.1 Check Micro Edge push rate is 30 seconds
Refer to section 3.4 on how to set Micro Edge push rate to 30 seconds.

### 4.3.2 Rate of Change Test Process
This test needs to be done to verify that the physical and calculated readings do not drift apart over time. Run a minimum of 50 litres of water through the water meter and then ensure that the Calculated Meter Reading aligns with the Physical Water Meter reading in Litres.

## 4.4 Recording the Finish Commissioning Values
Once adequate water has flowed through the meter, record the final values on the commissioning sheet. These should include the RSSI, battery voltage, current pulses, physical meter reading, and calculated meter reading, and then cross-reference them with the physical reading.

### 4.4.1 RSSI (Received Signal Strength Indicator)
The RSSI value from the Micro Edge device data as listed in step 4.1 should be no greater than -115. Any greater than this and the device may have dropouts and lost data due to poor signal. Eg. -121 is a failure and will require a more suitable antenna to be fitted.

### 4.4.2 Battery Voltage
The battery voltage from the Micro Edge device data should be greater than 3.6 volts.

### 4.4.3 Current Pulses
This current pulses value should be recorded at the time of taking the final reading for comparison with the initial pulse value.

### 4.4.4 Physical Meter Reading and Calculated Meter Reading
For the Rate of Change test to pass, the recorded physical and calculated readings must be compared and fall within an acceptable tolerance. This tolerance is determined by the pulse-per-liter value. For instance, if the meter registers 5 liters per pulse, the physical and calculated readings should not differ by more than 5 liters. The example provided illustrates a pass: with a 5-liter-per-pulse meter, the readings are only 2 liters apart.

<img src={require("./img/wm-img/image15-cropped.png").default} width="80%" style={{ display: "block", margin: "0 auto" }}/>

<br/>

<br/>

### 4.4.5 Return the Micro Edge Dip Switch to the 15 Minute Position
1. The Micro Edge push rate needs to be reset to 15 minutes for normal operation. To do so position dip switch #1 to the OFF position.
2. Press the reset button 'RST'
3. Install the Micro Edge cover.

<img src={require("./img/wm-img/image16-cropped.png").default} width="60%" style={{ display: "block", margin: "0 auto" }}/>

<br/>

<br/>

# 5. Nube iO Rubix Compute Gateway and Micro Edge Topology

<img src={require("./img/wm-img/image17-cropped.png").default} width="70%" style={{ display: "block", margin: "0 auto" }}/>

<br/>

<br/>

# 6. Troubleshooting

## 6.1 No Pulses recorded by the Micro Edge
If there are no pulses being recorded by the Micro Edge the input needs to be tested and then followed by testing the pulse probe is outputting pulses.

### 6.1.1 Testing the Input
Due to the power-saving feature of the Micro Edge, which records pulse count only during the wake phase from sleep state, it's important to avoid pressing the reset button before the

device wakes up on its own. This precaution is necessary to prevent loss of pulse data. To

effectively test the pulse counter, follow these steps:
1. Disconnect water Meter: Ensure the water meter is disconnected from the device to facilitate an isolated test environment.
2. Configuration Setting: Adjust the device's push interval to 30 seconds, Refer to the datasheet, dips = '100' for 30 seconds.
3. Device Reset: Initiate a reset by pressing the device's reset button.
4. Terminal Shorting: Manually short the pulse terminals several times to simulate input signals.
5. Wait for Data Transmission: After the terminal shorting, allow a wait time of 30 seconds you will see the leds flash when a message is sent.

## 6.2 Micro Edge Offline
If the Micro Edge is offline or not reporting data to the gateway, follow the below steps:
1. Check the antenna is connected well and not damaged.
2. Open the cover of the Micro Edge and inspect for any visible damage such as corrosion or loose connections (eg loose antenna cable)
3. Press the reset button (RST) and check if the LED indicators are 'Blinking'. The The blinking indicates the Micro Edge is powered and attempting to communicate with the Gateway.

<img src={require("./img/wm-img/image17-cropped.png").default} width="70%" style={{ display: "block", margin: "0 auto" }}/>

4. If the LEDs do not 'Blink' remove the battery and check the voltage. A healthy battery will be greater than 3.6V. A battery that is between 3.4 V - 3.6 V is partially drained and may need to be replaced soon. A battery voltage below 3.4V can be considered a flat/drained battery and will require replacing.
    1. If battery is above 3.5V move to step 5
    2. If the battery is below 3.5V replace the battery. Once the new battery is plugged in repeat step 3 then check if the Gateway has received data from the Micro Edge. If no data move to step 5
5. If there is still no data to the Gateway or LED indicators active, proceed to replace the Micro Edge and re-complete the Rate of Change Validation.
6. If the Micro Edge is under warranty please contact service@nube-io.com to initiate the warranty claim process.

<br/>

## 6.2 Contacting Support
If further assistance or support is required please contact Nube iO's service channel using the below details:<br/>
**Phone:** 0499 949 449 <br/>
**Email:** service@nube-io.com
