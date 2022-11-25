# Adin Ackerman

(760) 626-6570 | aiackerman@ucsd.edu | [GitHub](https://github.com/AdinAck) | [2021 Portfolio](https://www.youtube.com/watch?v=g3itfoOmj-A) | [Maker Portfolio for my MIT Application](https://www.youtube.com/watch?v=01xOdK2FQu4)

## About Me

I have been passionate about computers and electronics for many years. Most of my education is informal, as I spent my days after school learning about electronics and computer engineering. I have a deep passion for the interaction between hardware and software, with a focus on user experience and education as well. In a nutshell, I am very detail oriented.

## Education

### **UC San Diego** - *B.S. Electrical Engineering* - 2025

GPA: 3.9

## Experience

### **Electrical Engineering** - *4 years*

- **PCB Design:** Altium/KiCAD, roughly 15 PCBs designed and assembled, embedded microcontrollers, motor control systems, battery management systems
- **Embedded Systems:** Arduino, ASF4 (Atmel SAM), RP2040, ESP-IDF
- **Debugging:** Standard hardware debugging practices, using lldb to debug microcontroller through a debugger chip, and on normal C, C++ programs, oscilloscopes, bench power supplies.
- **Soldering:** By hand, reflow (with an oven or sand in a pan)

### **Software Engineering** - *5 years*

- Advanced data structures and OOP Practices, threading, networking (sockets, http servers, etc.), IC drivers / hardware interfaces
- Bluetooth - I have done multiple projects involving an ESP32 embedded on a PCB, running a GATT server accessed by an app made in Swift (another one of my favorite languages)

## Notable Projects

### September 2022 / Present - **LEGv8 Simulator** [GitHub](https://github.com/AdinAck/LEGv8-Simulator)

In preparation for a class I am taking this quarter, I created a powerful simulator for the LEG instruction set, providing many useful tools for writing and debugging LEG assembly code. It has full linting capabilities, breakpoints, step over routines, register and memory access indicators / history. I've tried to make the experience of writing assembly as painless as possible.

### September 2021 / Present - **Educational SCARA Motion Control System** (WIP) [Home Page](https://mew463.github.io/SCARA-Arm.html)

Using my custom FOC motor controller (below), a friend and I created a "robot arm" for introducing young engineers into robotics engineering. Thanks to the usage of my custom motor controller, the robot arm is movable by humans, and no gears are required since FOC allows for precise position control. A professor liked our project and happily funded its development. We were even given a designated section of our local maker space.

### June / July 2021 - **FOC Motor Controller** [GitHub](https://github.com/AdinAck/Motor-Controller)

A motor controller capable of running FOC algorithms to drive BLDC motors with high accuracy, speed, and torque.

Challenges involved in this project:

- Using the Arduino framework on an embedded micro controller, high density PCB design, avoiding interference between power and digital components, ensuring USB cannot be current source when motor is driven, developing Python hardware interface for automated control

## Previous Internships

### **Existential Robotics Lab, UCSD** - *Paid Intern*

March 2022 - September 2022

- Got to do some PCB design, learn a bit about SLAM

### **Spreadtrum Communications Inc, Sorrento Valley** - *Paid Intern*

June 2019 - August 2019

- Created software tools for bring-up to simulate their chip and view which parts of the processor were active given the programmed register values.
- Met my electrical engineering mentor, worked on the office motorized chair and learned about general electronics.