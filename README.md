# Contact

Adin Ackerman | (760) 626-6570 | adinackerman@gmail.com

# Experience

### **Python** - *3 years*

I'm a total Python nerd. I take pride in making my code readable (in true Python fashion), optimized, and well documented. I've got all the Python tricks up my sleeve!

- Advanced Data Structures
- Sockets
- GUIs
- NumPy, Tensorflow, etc.
- IC Drivers / Hardware Interfaces

### **Electrical Engineering** - *2+ years*

I've designed and tested 6 (and counting) PCBs over the years, and have loved every second of it. I've gained a very diverse range of knowledge and experience from my PCB projects, and have learned most of what I know simply by reading datasheets or application notes for the various ICs I intend to use... in addition to the knowledge gained by solving the many problems I have faced, of course.

- PCB Design
- Embedded Systems
  - Arduino
  - ASF4 (Atmel SAM)
  - RP2040 SDK
- Debugging
- Reflow Soldering (and of course hand held soldering)
- Oscilloscope Usage

# Notable Projects

### July / August 2020 - **Battery Management System** [GitHub](https://github.com/AdinAck/SuperBMS)

Gained invaluable experience tackling the issues faced when designing and building a custom circuit (especially on a PCB)

- Reading datasheets
- Creating software to interface with various ICs
- MOSFETs
- Optoelectronics
- Lithium batteries
- Debugging and resolving complex problems

### May / July 2021 - **Battery Evaluator** [GitHub](https://github.com/AdinAck/Battery-Evaluator)

A device for benchmarking batteries, and creating models for accurately predicting the state of charge of a battery given it's voltage.

Tests include:

- Internal resistance
- Constant current discharge
- Constant power discharge

The challenge for this project was designing a programmable constant current sink, which I have solved by utilizing the on-board DAC of the microcontroller as the non-inverting input to an op-amp driving the MOSFETs that discharge the battery, with the inverting input being the voltage across the current-sense resistors.

### June / July 2021 - **FOC Motor Controller** [GitHub](https://github.com/AdinAck/Motor-Controller)

A motor controller capable of running FOC algorithms to drive BLDC motors with high accuracy, speed, and torque.

One of my coolest projects yet. FOC control is a fairly new and highly advanced method of controlling BLDC motors that I have been interested to learn about for a long time.

Challenges involved in this project:

- Embedding SAMD processor on custom board (like the battery evaluator)
- High density PCB design
- Avoiding interference between power and digital components (solid ground plane)
- Ensuring USB cannot be current source when motor is driven
- Developing Python hardware interface for automated control

### September 2021 / Present - **Educational SCARA Motion Control System** (WIP)

A motor controller capable of running FOC algorithms to drive BLDC motors with high accuracy, speed, and torque.

Using the aforementioned FOC motor controllers, me and a friend created a "robot arm" -- one could call it -- for introducing young engineers into robotics engineering. Thanks to the usage of the FOC Motor Controller, no gears are required since FOC allows for maximum torque at all velocities, in conjunction with very high precision and accuracy.

A professor of ours has given us $500 to continue development of the robot arm, and to set up an educational display for students to easily access. A popular maker space at our university graciously provided us space and resources for our exhibit, and we are very grateful!

We plan on providing 4 deep-dive pathways, Mechanical Engineering, Electrical Engineering, Software, and Machine Learning. Of course, we will explain the fusion of these disciplines, and good practices when it comes to system integration.

# Previous Internships

### **Spreadtrum Communications Inc, Sorrento Valley** - *Electrical Engineering Intern*

June 2019 - August 2019

- Created software tools for bring-up to simulate their chip and view which parts of the processor were active given the programmed register values.
- Met my electrical engineering mentor, worked on the office motorized chair and learned about general electronic theory.

# Education

### **San Dieguito Academy** - *High School*

August 2016 - June 2021

GPA: 4.3

### **UC San Diego** - *B.S. Electrical Engineering*

September 2021 - June 2025

GPA: 4.0

# Portfolio

[GitHub](https://github.com/AdinAck)

[Maker Portfolio for my MIT Application](https://www.youtube.com/watch?v=01xOdK2FQu4)