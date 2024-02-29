# Modbus Communications #

Nube-iO Rubix iO Modules are a pure modbus device; All communications with the iO Modules are via modbus. Modbus settings are configured via the onboard DIP switches. Modbus settings on the gateway controller must match those set on the
connected iO Modules. All devices on a modbus network must have the same modbus
network settings.

## Default Modbus Network Settings ##

Initially modbus settings for the iO Modules will be set as follows:

        Device Address: 1
        Baud rate: 38400
        Parity: None
        Stopbits: 1
        Bytesize: 8

## Modbus Points ##

This section describes the available modbus points that are used to interact with the iO
Modules.

Rubix iO Module modbus points are grouped into two categories: **Modbus Configuration Points**, and Modbus Value Points.

**Modbus Configuration Points** are used to initially configure the types of each Universal Input
(UI) and Universal Output (UO). Digital Outputs do not need configuration values as they only
support Digital type.

**Modbus Value Points** are divided into two categories Input Value Points, and Output Value
Points:

- **Input Value Points** are used to READ the values of the Universal Inputs (the units of
these values depend on the associated Modbus Configuration Point).
- **Output Value Points** are used to WRITE values to the Universal/Digital Outputs;
writing to these points will change the physical output terminals (the units of these
values depend on the associated Modbus Configuration Point).

### Universal Output Modbus Configuration Points ###

These Modbus Configuration Points are used to configure the types of each Universal Output
(UO).
The following tables detail the Universal Output Type Configuration Registers and the valid
config setting values.

**Universal Output Configuration Values**

| **Config Type** 	| **Write Value** 	| **Valid VALUE REGISTER Write Values for this Config Type** * 	|
|:---------------:	|:---------------:	|:-----------------------------------------------------------:	|
| 0–10 VDC        	| 1               	| 0 to 10 ⇒ 0 to 10 VDC                                       	|
| Digital         	| 2               	| 0 = OFF, 1 = ON                                             	|
_These are the values that can be written to the VALUE REGISTERS listed in Section 6.2.1.2_ 

**Universal Output Configuration Registers**

| **Point**   	| **Description** 	| **Register** 	| **Register Type** 	| **Data Type** 	| **Function Code** 	|
|-------------	|-----------------	|--------------	|-------------------	|---------------	|-------------------	|
| U01 Config  	| Set type of U01 	| 5001         	| Holding           	| UINT16        	| 3,6,16            	|
| U02 Config  	| Set type of U02 	| 5002         	| Holding           	| UINT16        	| 3,6,16            	|
| U03 Config  	| Set type of U03 	| 5003         	| Holding           	| UINT16        	| 3,6,16            	|
| U04 Config  	| Set type of U04 	| 5004         	| Holding           	| UINT16        	| 3,6,16            	|
| U05 Config  	| Set type of U05 	| 5005         	| Holding           	| UINT16        	| 3,6,16            	|
| U06 Config* 	| Set type of U06 	| 5006         	| Holding           	| UINT16        	| 3,6,16            	|
| U07 Config* 	| Set type of U07 	| 5007         	| Holding           	| UINT16        	| 3,6,16            	|
| U08 Config* 	| Set type of U08 	| 5008         	| Holding           	| UINT16        	| 3,6,16            	|

### Output Modbus Value Points ###

The following table details the Universal Output (UO) and Digital Output (DO) Value
Registers. Writing to these registers will drive the Physical Output points. For UOs the type
of each output must be configured correctly via Type Select Onboard Switches [section 5.4.1](Installation-and-Configuration.md#left-bank-dip-switches---modbus-addressing) and Config Registers (Section 6.2.1). See Section 6.2.1 for valid Write Values for each Config Type.

| **Point** 	| **Description**  	| **Register** 	| **Register Type** 	| **Data Type** 	| **Function Code** 	|
|-----------	|------------------	|--------------	|-------------------	|---------------	|-------------------	|
| U01       	| Set value of U01 	| 801          	| Holding           	| FLOAT         	| 3,6,16            	|
| U02       	| Set value of U02 	| 803          	| Holding           	| FLOAT         	| 3,6,16            	|
| U03       	| Set value of U03 	| 805          	| Holding           	| FLOAT         	| 3,6,16            	|
| U04       	| Set value of U04 	| 807          	| Holding           	| FLOAT         	| 3,6,16            	|
| U05       	| Set value of U05 	| 809          	| Holding           	| FLOAT         	| 3,6,16            	|
| U06*      	| Set value of U05 	| 811          	| Holding           	| FLOAT         	| 3,6,16            	|
| U07*      	| Set value of U05 	| 813          	| Holding           	| FLOAT         	| 3,6,16            	|
| U08*      	| Set value of U05 	| 815          	| Holding           	| FLOAT         	| 3,6,16            	|
| DO1**     	| Set value of DO1 	| 501          	| Coil              	| DIGITAL       	| 1,5,15            	|
| DO2**     	| Set value of DO2 	| 502          	| Coil              	| 3,6,16        	| 1,5,15            	|

_* IO-16 Only <br/>
** IO-11 Only_

### Universal Input Type Configuration Registers ###

These Modbus Configuration Points are used to configure the types of each Universal Input (UI).
The following tables detail the Universal Input Modbus Configuration Point Registers and the valid config setting values.

**Universal Input Configuration Values**

| **Config Type**                     	| **Value** 	|
|-------------------------------------	|-----------	|
| 10k Thermistor                      	| 1         	|
| Resistance                          	| 2         	|
| 0–10 VDC                            	| 3         	|
| 4-20mA                              	| 4         	|
| Digital                             	| 5         	|
| Digital Hold On RISING Edge         	| 6         	|
| Digital Hold On FALLING Edge        	| 7         	|
| Digital Pulse Count on RISING Edge  	| 8         	|
| Digital Pulse Count on FALLING Edge 	| 9         	|

**Universal Input Configuration Registers**

| **Point**   	| **Description** 	| **Register** 	| **Register Type** 	| **Data Type** 	| **Function Code** 	|
|-------------	|-----------------	|--------------	|-------------------	|---------------	|-------------------	|
| UI1 Config  	| Set type of UI1 	| 5201         	| Holding           	| UINT16        	| 3,6,16            	|
| UI2 Config  	| Set type of UI2 	| 5202         	| Holding           	| UINT16        	| 3,6,16            	|
| UI3 Config  	| Set type of UI3 	| 5203         	| Holding           	| UINT16        	| 3,6,16            	|
| UI4 Config  	| Set type of UI4 	| 5204         	| Holding           	| UINT16        	| 3,6,16            	|
| UI5 Config  	| Set type of UI5 	| 5205         	| Holding           	| UINT16        	| 3,6,16            	|
| UI6 Config  	| Set type of UI6 	| 5206         	| Holding           	| UINT16        	| 3,6,16            	|
| UI7 Config* 	| Set type of UI7 	| 5207         	| Holding           	| UINT16        	| 3,6,16            	|
| UI8 Config* 	| Set type of UI8 	| 5208         	| Holding           	| UINT16        	| 3,6,16            	|
_* IO-16 Only_

### Universal Input Modbus Value Points ###

The following table details the Universal Input (UI) Modbus Value Point Registers. The type of each output must be configured correctly via Type Select Onboard Switches (Section 5.4.1) and Config Registers (Section 6.2.3) [Universal Input Type Configuration Registers](#universal-input-type-configuration-registers). See Section 6.2.3 for valid Write Values for each Config Type.

| **Point** 	| **Description**  	| **Register** 	| **Register Type** 	| **Data Type** 	| **Function Code** 	|
|-----------	|------------------	|--------------	|-------------------	|---------------	|-------------------	|
| UI1       	| Set value of UI1 	| 801          	| Input             	| FLOAT         	| 4                 	|
| UI2       	| Set value of UI2 	| 803          	| Input             	| FLOAT         	| 4                 	|
| UI3       	| Set value of UI3 	| 805          	| Input             	| FLOAT         	| 4                 	|
| UI4       	| Set value of UI4 	| 807          	| Input             	| FLOAT         	| 4                 	|
| UI5       	| Set value of UI5 	| 809          	| Input             	| FLOAT         	| 4                 	|
| UI6       	| Set value of UI6 	| 811          	| Input             	| FLOAT         	| 4                 	|
| UI7*      	| Set value of UI7 	| 813          	| Input             	| FLOAT         	| 4                 	|
| UI8*      	| Set value of UI8 	| 815          	| Input             	| FLOAT         	| 4                 	|
_* IO-16 Only_



