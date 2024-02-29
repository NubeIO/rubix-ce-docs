---
sidebar_position: 1
---


# Overviews

The Rubix iO Modules are Nube-iO’s versatile, low-cost physical Input/Output module. They
provide expandable modular monitoring and control points in a small package.
With one or more modules plugged directly into the side of a Rubix Compute, or wired via RS485,
these Rubix iO Modules allow for BMS implementations of any size.
In addition to being a slave physical input/output device, the Rubix iO Modules can be configured
as standalone HVAC application controllers. With configuration and monitoring of the HVAC
applications via Modbus these modules allow for low cost distributed control and central
monitoring of many types of systems.
The Rubix iO Modules are a pure Modbus device, making them useful in systems even beyond
the Nube-iO platform.
Optional LoRa wireless version of the Rubix iO allows for wireless communication with the iO
Modules. LoRa wireless technology provides a very long transmission range that is less
susceptible to object interference than other wireless technologies.
When using LoRa wireless to communicate with the Rubix iO Modules the RS485 port can be
used as a Modbus passthrough, this allows for wireless communication with any wired (RS485)
Modbus device.

![max200px](../../../img/io-16.png)

# Technical Specifications

### Physical Attributes 

![io-16-size.jpg](img/io-16-size.jpg)

![dimensions-t.png](img/dimensions-t.png)

### Power Requirements

![power-t.png](img/power-t.png)

### Communication Options

![communication-t.png](img/communication-t.png)

### Physical Inputs and Outputs

![max400px](img/physical-inputs-outputs.jpg)

| Type IO-11            	| Count 	| IO-16 	| Count Details                                                                                      	|
|-----------------------	|-------	|-------	|----------------------------------------------------------------------------------------------------	|
|  Universal Input (UI) 	|   6   	|   8   	| ● 0 - 10 VDC Signal <br/> ● 10k Thermistor <br/> ● Resistance <br/> ● Digital / Switch / Dry Contact <br/> ● 4-20mA Signal 	|
| Universal Output (UO) 	|   5   	|   8   	| ● Analog: 0 to 10 VDC (50ma Max) <br/> ● Digital: 0 or 12 VDC 0V[OFF] / 12VDC[ON] (700mA Max)            	|
|  Digital Output (DO)  	|   2*  	|   0   	| ● 0 or 12 VDC 0V[OFF] / 12VDC[ON] (700mA Max)                                                      	|
_ The DO terminals on the IO-11 are located on the side of the controller. When Rubix iO Modules are plugged directly
into each other, or to a Rubix Compute via the side connections, the DO terminals will not be available._

### Regulatory Compliance ###

| **Manufacturer/Model** 	| **Regulatory**           	| **Notes**      	|
|------------------------	|--------------------------	|----------------	|
| Nube IO / IO-11        	| AS/NZS CISPR 32: 2015    	| IO-11 device   	|
| Nube IO / IO-16        	| AS/NZS CISPR 32: 2015    	| IO-16 device   	|
| HopeRF / RFM95         	| FCC: Class B 3M Radiated 	| LoRa RF module 	|





:::tip Downloads
:arrow_down: [Datasheet](https://raw.githubusercontent.com/NubeIO/rubix-docs/master/pdfs/hardware/io-modules/Rubix%20IO-16%20-%20Datasheet.pdf)






[def]: img/dimensions-t.png