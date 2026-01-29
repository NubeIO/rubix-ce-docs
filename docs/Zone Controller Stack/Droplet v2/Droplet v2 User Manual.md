# Droplet v2 User Manual

# 1. Overview/About Product

## 1.1. Product Overview
Droplet Gen2 by Nube iO is the next evolution of our industry-leading wireless LoRa® IoT sensor, engineered to capture accurate Temperature and Humidity data with greater reliability and performance than previous generations. Designed as a surface-mount, fully wireless device, Droplet Gen2 eliminates the need for physical sensor wiring, significantly reducing installation time, labour costs, and disruption for building occupants.

Built on our enhanced Gen2 architecture, the Droplet leverages LoRa® technology to deliver a robust transmission range, energy efficiency, and minimal susceptibility to object interference compared to other wireless technologies. These advancements make Droplet Gen2 an ideal choice for monitoring, controlling, and optimising various spaces.

## 1.2. Architecture
**Droplet:** This wireless LoRa device monitors temperature and humitidy in each zone transmitting data to the ZoneConnex allowing for individual zone control. <br/>
**ZoneConnex Controller:** Acts as the master device, interfacing with compatible RAC/PAC and VRF Air Conditioning units via the UART protocal. It manages data transmission to and from the field devices and manages the control of the air conditioning system. <br/>
**Touch Point LCD:** This wall-mounted touchscreen provides a local control interface for the user to manage and monitor the air conditioning system. <br/>
**Nube iO Mobile App:** This mobile application provides a remote control interface for the user to manage and monitor the air conditioning system. <br/>


## 1.3. Product Features
**LoRa®:** The Droplet supports LoRa wireless communication. <br/>
**Temperature Monitoring:** The Droplet monitors temperature with an accuracy of ±0.2°C within the range of –40°C to 85°C. <br/>
**Relative Humidity Monitoring:** The Droplet monitors relative humidity with an accuracy of ±2% RH within the range of 0% to 100%. <br/>

<br/>

# 2. Hardware Overview

## 2.1. Packing List
*Include Images and Description of Included Parts*

## 2.2. Product Dimensions
*Include Diagram with Dimensions*

## 2.3. Product Component Breakdown
*Include Diagram with descriptions of components*
- *Eg Buttons, LEDs, Terminals, Plugs etc*

### 2.3.1 External

### 2.3.2 Internal

<br/>

# 2. Installation & Configuration

## 2.1. Mounting
*Insert descriptions of mounting options*

*Insert Diagram of Best Mounting*

## 2.2. Dip Switch Configuration (If Applicable*)
*Insert Description Table Showing Dip Switch Configuration and Descriptions*

<!-- Examples Below

| Minutes | Register Number   |
|---------|-------------------| 
| 0.5     | ![max200px](img\dip1.png) |
| 1       | ![max200px](img\dip2.png) |
| 3       | ![max200px](img\dip3.png) |
| 5       | ![max200px](img\dip4.png) |
| 10      | ![max200px](img\dip5.png) |
| 15      | ![max200px](img\dip0.png) | 
| 30      | ![max200px](img\dip6.png) |
| 60      | ![max200px](img\dip7.png) | -->



<!-- |                    	| **[Dip-Switch: 1, 2] - Operation Mode** 	|
|:--------------------:	|:--------------------------------------:	|
| **Switch Setting** 	| **Operation Mode**                     	|
| 00                 	| RS485 (Wired)                          	|
| 10                 	| LoRa® Wireless*                         	|
| 01                 	| RS485 -> LoRa® Passthrough**            	|
| 11                 	| Settings Reset***                       	|
|                    	|  **[Dip-Switch: 3, 4, 5]- Baud Rate**  	|
| **Switch Setting** 	| **Baud Rate**                          	|
| 000                	| 38400                                  	|
| 100                	| 9600                                   	|
| 010               	| 19200                                  	|
|                    	|     **[Dip-Switch: 6, 7] - Parity**    	|
| **Switch Setting** 	| **Parity**                             	|
| 00                 	| None                                   	|
| 10                 	| Even                                   	|
| 01                 	| Odd                                    	| -->


<br/>


<!-- ## 2.3. Power Connections (If Applicable*)
*Insert Description and Diagram of Power Connection*

Example Below:

|           	| ![max200px](img/IO-16-wiring.png)     |
|-----------	|----------------	                    |
| Pin 1 (+) 	| 24VDC          	                    |
| Pin 2 ( ) 	| Do Not Connect 	                    |
| Pin 3 (-) 	| DC Ground      	                    | -->

<br/>

## 2.4. Communication Connections (If Applicable*)
*Insert Description and Diagram of Communications Connection*

Example Below:


<!-- |           	| ![max200px](img/IO-16-wiring.png)     |
|-----------	|----------------	                    |
| Pin 1 (**+**) | **A** or **+** of RS485 Network       |
| Pin 2 (-) 	| **B** or - of of RS485 Network        |
| Pin 3 (**G**) | **C** or **Ground**      	            | -->

<br/>

## 3. I/O Connections (If Applicable*)
*Insert Description and Diagram of Overall I/O Connections*

### 3.1. Inputs
*Insert Description and Diagram of Input Connections*

#### 3.1.1. Digial Inputs
*Insert Description and Diagram of Digital Input Connections*

#### 3.1.2. Analog Inputs
*Insert Description and Diagram of Analog Input Connections*

<br/>

### 3.2. Ouputs
*Insert Description and Diagram of Output Connections*

#### 3.2.1. Digial Ouputs
*Insert Description and Diagram of Digital Input Connections*

#### 3.2.2. Analog Ouputs
*Insert Description and Diagram of Analog Input Connections*


# 4. Operation Guide
*Insert Operational information and descriptions*

<br/>

# 5. Point Register (If Applicable*)
*Insert Point Register for device including a point table*

<!-- Example:

| **0-10VDC**    	|                   	|
|----------------	|-------------------	|
| Register Type  	| Holding Registers 	|
| Data Type      	| UINT16            	|
| Function Codes 	| 3,6,16            	|
| Description    	| Set value         	|
| Value Scale    	| x0.01              	|

| Point 	| Register 	|
|-------	|----------	|
| U01   	| 1        	|
| U02   	| 2        	|
| U03   	| 3        	|
| U04   	| 4        	|
| U05   	| 5        	|
| U06   	| 6        	|
| U07   	| 7        	|
| U08   	| 8        	| -->

<br/>

# 6. Document Revision

| Revision | Date       | Change Description                  |
|----------|------------|------------------------------------|
| 1.0      | 28-11-2025 | Initial release of the document.   |
| 1.1      | DD-MM-YYYY | Description of the next change.    |
| 1.2      | DD-MM-YYYY | Description of the next change.    |

