---
sidebar_position: 2
---


# Installation and Configuration

## External

![external.png](img%2Fexternal.png)

* U.FL Connector: Connects the antenna for wireless communication.
* Mounting Holes: Enables secure attachment to fixtures.
* Captive Screws: Allows for easy opening of the device.
* Cable Gland: Facilitates the entry of cables into the device.
* M16 Plug: Accommodates extra cable glands for additional wiring.


## Internal

![internal.png](img%2Finternal.png)

* Reset Button: Power cycles the device.
* Dip Switches: Adjusts the data push rate and resets the pulse counter.
* Screw Terminal: Connects analog and digital inputs to the device.
* Battery Connector: Links the battery to the device for power supply.
* Battery: Provides a long-lasting power source for the device.


## Dip Switches
The MicroEdge sensors feature a bank of 8 small DIP switches located on the top of PCB.
These switches are used to configure the functionality of the MicroEdge.
To access them, simply open the sensor cover, by undoing the four captive screws.

![dips_ME.png](img%2Fdips_ME.png)

* Switches 1-3: Control the LoRa data push rate.
* Switch 6: Resets the pulse count.
* Switch 7: Activates test mode for device diagnostics.


## Inputs
![terminal.png](img%2Fterminal.png)

### Universal inputs
The  Universal Inputs can be used as Analog or Digital inputs.
Integrated pull-up resistor ensures reliable digital input readings.
- Digital Inputs:
    - Binary states: Open (no connection) or Closed (connected) circuit.
    - Suitable for: Switches, buttons, relays, and dry contacts (e.g., device status signals).
- Analog Inputs:
    - Varied states based on Voltage, Resistance, or Current measurements.
    - Compatible with sensors for: Temperature, Humidity, Pressure, CO2 levels, Position Feedback.

:::info 
Maximum input voltage is 3.3V.
:::

### Pulse input
* Dedicated input for counting and accumulating pulse signals.
* Suitable for measuring flow rates in utilities like water, gas, and electricity.



## Mounting
* Surface Mounting: Designed for attachment to flat surfaces using external screws.
* Antenna Orientation: Optimal performance when mounted with the antenna facing upwards.
* Temperature Considerations: Avoid locations with extreme temperatures for consistent operation.
* Gateway Proximity: Choose a mounting location considering its relative position to the LoRa gateway for optimal signal strength.


## Connecting the battery
* Connect the battery to power the device.
* Upon activation, LEDs will flash, indicating the device is on and a message is being transmitted.
* LEDs will turn off post-transmission to conserve energy.



## Push rate
DIP switches 1 to 3 are used to set the push rate of the MicroEdge sensor.
After setting the desired push rate, press the reset button to apply the new configuration.


| Minutes | Register Number   |
|---------|-------------------| 
| 0.5     | ![](img\dip1.png) |
| 1       | ![](img\dip2.png) |
| 3       | ![](img\dip3.png) |
| 5       | ![](img\dip4.png) |
| 10      | ![](img\dip5.png) |
| 15      | ![](img\dip0.png) | 
| 30      | ![](img\dip6.png) |
| 60      | ![](img\dip7.png) |



## Reset Pulse Count
The procedure for resetting the pulse count involves a series of steps with the device's DIP switch and reset button.
1. Set DIP switch 7 to ON/1.
2. Press the Reset Button.
3. Wait for 5 seconds.
4. Set DIP switch 6 back to OFF/0.
5. Press the Reset Button again to complete the reset process.

![dip64.png](img%2Fdip64.png)


## Testing pulse input
Due to the power-saving feature of the MicroEdge, which records pulse count only during the wake phase from sleep state,
it's important to avoid pressing the reset button before the device wakes up on its own. 
This precaution is necessary to prevent loss of pulse data. To effectively test the pulse counter, follow these steps:
1. Water Meter Disconnection: Ensure the water meter is disconnected from the device to facilitate an isolated test environment.
2. Configuration Setting: Adjust the device's push interval to 30 seconds,  Refer to the datasheet, dips = '100' for 30 seconds .
3. Device Reset: Initiate a reset by pressing the device's reset button.
4. Terminal Shorting: Manually short the pulse terminals several times to simulate input signals.
5. Wait for Data Transmission : After the terminal shorting, allow a wait time of 30 seconds you will see the leds flash when a message is sent.



## Test mode
Test mode is used for diagnostics and performance verification, ensuring reliable operation before deployment.
In test mode, the device transmits data at a fixed, rapid interval (every 8 seconds) with a static Sensor ID, 
facilitating real-time testing and troubleshooting.
* Set DIP switch 6 ON/1
  * State: Overrides all Push Rate settings.
  * Uses a fixed Sensor ID (AAACAAAA).
  * Transmits data every 8 seconds.
* Set DIP switch 6 OFF/0
  * State: Returns to normal operation.
  * Follows pre-configured push rate.
  * Utilizes the device's unique Sensor ID.
  After setting the test mode switch to ON/1 or OFF/0, press the reset button to apply the new configuration.


![dip32.png](img%2Fdip32.png)