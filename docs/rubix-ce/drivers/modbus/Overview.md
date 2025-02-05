---
sidebar_position: 1
---

## Modbus

**Modbus** is a widely used communication protocol in the field of automation. It was developed in the late 1970s and has since become a standard for connecting electronic devices in various industries, including manufacturing, energy, and building automation.

Modbus allows for communication between devices such as programmable logic controllers (PLCs), sensors, actuators, and other industrial equipment. It supports both serial (RS-232, RS-485) and Ethernet (TCP/IP) communication protocols, making it versatile and suitable for a wide range of applications.

The protocol is simple and efficient, with basic functions for reading and writing data between devices. It defines a set of message formats for querying device registers and receiving responses. Modbus messages can be used to read sensor values, control actuators, monitor device status, and more.

## Object Type

In the Modbus protocol, there are several types of objects that represent different data or functions within a device. Some common Modbus object types include:

### Coils 
Also known as digital outputs, these represent binary values, typically used for controlling outputs like relays or valves.

### Discrete Inputs
These represent binary values as well, but they are read-only inputs, often used for monitoring the state of sensors or switches.

### Holding Registers
These represent 16-bit registers that can be read from or written to. They are commonly used for storing data like setpoints or control parameters.

### Input Registers
Similar to holding registers, input registers are also 16-bit registers, but they are read-only and typically used for monitoring data like sensor readings.

These object types define the structure of the data exchanged between Modbus devices, allowing for communication and control in industrial automation applications.

## Data Type

**Digital** - Represents a single bit of data, typically used for representing binary states (e.g., ON/OFF).

**16-bit Unsigned Integer** - It can hold values ranging from 0 to 65,535. It does not include negative numbers.

**16-bit Integer** - Represents integer values ranging from -32,768 to 32,767.

**32-bit Unsigned Integer** - Double word, A 32-bit unsigned integer in Modbus is capable of storing integer values ranging from 0 to 4,294,967,295. This data type uses all 32 bits to represent positive integer values and does not include negative numbers.

**32-bit Integer** - Represents integer values ranging from -2,147,483,648 to 2,147,483,647.

**64-bit Unsigned Integer** - Is capable of storing integer values ranging from 0 to 18,446,744,073,709,551,615. This data type utilizes all 64 bits to represent positive integer values and does not include negative numbers.

**64-bit Integer** - Represents integer values ranging from -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807.

**32-bit Floating Point** - Represents a single-precision floating-point value according to the IEEE 754 standard. This data type can represent a wide range of real numbers with decimal points, including both small and large values, and supports scientific notation.

A float 32 data type typically occupies four consecutive 16-bit registers (two words) and is used for applications requiring high precision in representing real-world values, such as sensor readings, temperature measurements, or process control parameters.


**64-bit Floating Point** - A float 64 data type usually occupies eight consecutive 16-bit registers (four words) and is utilized for applications requiring exceptionally high precision in representing real-world values, such as precise measurements in scientific instruments, complex calculations, or advanced control systems.

**mod10-u32** - Proprietary data type specific to a particular application or system.

## Write Modes

Below are descriptions of the `Write Modes` available on Modbus Points in Rubix CE.

| Write Modes | Selection | Description |
|--------------|----------------------|-------------------|
|ReadOnce   |       WriteMode = "read_once"   |         // Only Read Point Value Once.|
|ReadOnly     |     WriteMode = "read_only"    |        // Only Read Point Value (poll rate defined by setting).|
|WriteOnce       |  WriteMode = "write_once"    |       // Write the value on COV, don't Read.|
|WriteOnceReadOnce |WriteMode = "write_once_read_once"| // Write the value on COV, Read Once.|
|WriteAlways      | WriteMode = "write_always"        | // Write the value on every poll (poll rate defined by setting).
|WriteOnceThenRead| WriteMode = "write_once_then_read" |// Write the value on COV, then Read on each poll (poll rate defined by setting).
|WriteAndMaintain | WriteMode = "write_and_maintain"   |// Write the value on COV, then Read on each poll (poll rate defined by setting). If the Read value does not match the Write value, |rite the value again.|

