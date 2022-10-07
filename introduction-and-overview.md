# Introduction and Overview

### 2. Introduction and Overview

### 2.1 Introduction&#x20;

Introducing the Automotive Industry's first open and robust platform for the Raspberry Pi. The neoVI PI has a built-in Raspberry Pi 4 Compute Module (RPi4 CM) that contains quad 64-bit processors and a gigabit Ethernet port, paired with Intrepid’s CAN FD technology. This allows you to simulate, test and datalog with the flexibility that the Raspberry Pi 4 Compute allows. The neoVI Pi has all the features of the RPi4 CM plus up to four CAN FD networks.&#x20;

The neoVI PI is designed and tested for the automotive environment. This includes a wide power supply range, EMC protection, rugged packaging and environmental testing. The neoVI PI allows you to use the Raspberry Pi 4 Compute while avoiding additional development to adapt to the automotive network environment. That makes the neoVI PI powerful enough to solve your vehicle network problems, yet small enough to fit in your backpack.

### 2.2 Package Contents

**The neoVI PI package includes hardware and drivers**

#### 2.2.1. Hardware&#x20;

The package contains the following:&#x20;

* The neoVI PI network interface device.&#x20;
* Quick Start Card to help you get going quickly with your device.&#x20;

#### 2.2.2. Drivers&#x20;

The neoVI PI package includes media containing:

* A copy of vehicle network software.&#x20;
* Drivers for the neoVI PI adapters.&#x20;
* An API install kit containing the neoVI Explorer utility for configuring the device.&#x20;

It is also possible to control the neoVI PI from within our open source software using APIs that the device supports.&#x20;

If anything is missing or damaged, please contact Intrepid Control Systems for assistance. The contact for your locale can be found at [https://www.intrepidcs.com/worldwide](https://www.intrepidcs.com/worldwide) or refer to Section 7 within this document.

### 2.3. Operational Overview&#x20;

The neoVI PIs operation can broadly be broken down into three categories: vehicle network interfacing, data acquisition, and simulation and scripting.

#### 2.3.1 Vehicle Network Interfacing

Using the provided cables, you can connect the ValueCAN 4-2 to either a bench test setup or a vehicle to monitor live network activity. All channels are monitored simultaneously and are hardware time-stamped.&#x20;

#### 2.3.2. Data Acquisition&#x20;

The neoVI PI enables the acquisition of data from networks with precise control over collection parameters. The data can be captured using the Intrepid APIs.&#x20;

#### 2.3.3. Simulation and Scripting&#x20;

Using Vehicle Spy X, you can define transmit messages with custom data and send them manually or on a schedule of your choosing. You can also write intelligent scripts that implement arbitrary logic and compile them into Raspberry PI that run within the device itself. This functionality allows you to create specialized test scenarios, and to simulate ECUs and gateways.

### 2.4. Summary of Key Features&#x20;

This section includes a summary of the device’s most important design, construction, operational and performance features:

**2.4.1. Construction, Controls and Cabling**

* Temperature range: -30°C to +80°C&#x20;
* Dimensions: 13.60cm by 11.22cm by 3.97cm
* LEDs (user programmable): 10 programmable tri-color LEDs&#x20;
* Power supply: 5-60V operation
* Solid powder-coated aluminum case.&#x20;
* CAN/CAN FD channel status LEDs.&#x20;
* Ability to control CAN/CAN FD termination resistance on both channels

**2.4.2. Performance**

* Support for RPi CM4 variants with EMCC and SDCard for OS storage.&#x20;
* Micro USB interface for RPi OS EMCC update (EMMC CM4 only)&#x20;
* Micro SD Card interface for RPi OS (Non EMMC CM4 only)&#x20;
* Fast wake 70 milliamps
* M2 NVMe 2.0 SSD&#x20;
* Vehicle connectors: 26-pin male HD D-sub&#x20;
* Field-upgradeable flash firmware
* Standalone mode, receive messages, transmit messages, expressions, I/O and transport layers
* 64-bit timestamping to an accuracy of 25 nanoseconds on all networks

**2.4.3. Network Interfaces and Features**

**Network Specifications – CANFD**

* 4x CAN FD / CAN 2.0 channels (Bosch MCAN core) with:
* MCP MCP2562FD PHY
* Compatible with Device Net and CANopen
* Double-buffered CAN transmission
* Software selectable CAN termination
* CCP protocol hardware acceleration&#x20;
* Listen-only mode support&#x20;
* Termination check feature
* &#x20;Error frame transmit support

#### 2.4.4. Simulation&#x20;

Fully-programmable scripting using Raspberry PI&#x20;

#### 2.4.5. PC Interface Support&#x20;

High-speed isolated Ethernet connection protects PC from potential damage.

#### 2.4.6. Advanced Features&#x20;

* Device control by external software using Open source APIs on github/intrepidcs: libicsneo ([https://github.com/intrepidcs/libicsneo](https://github.com/intrepidcs/libicsneo)) for C/C++ and python\_ics for Python [https://github.com/intrepidcs/python\_ics](https://github.com/intrepidcs/python\_ics)

### 2.5. Hardware and Software Requirements

Before you get started make sure you have the following dependencies

* CMake 3.2 or above&#x20;
* GCC 4.7 or above, 4.8+ recommended&#x20;
* libusb-1.0–0-dev&#x20;
* build-essential is recommended
