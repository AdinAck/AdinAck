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
- **Embedded Systems:** Embedded Rust, Baremetal, ASF4 (Atmel SAM), Arduino
- **Debugging:** Standard hardware debugging practices, using lldb to debug microcontroller through a debugger chip, and on normal C, C++ programs, oscilloscopes, bench power supplies.
- **Soldering:** By hand, reflow (with an oven or sand in a pan)

### **Software Engineering** - *5 years*

- Advanced design and software architecture and OOP Practices, threading, networking (sockets, http servers, etc.), IC drivers / hardware interfaces
- Bluetooth - I have done multiple projects involving an ESP32 embedded on a PCB, running a GATT server accessed by an app made in Swift (another one of my favorite languages)

## Notable Projects

### May 2023 - **stm32f0xx-hal** [GitHub](https://github.com/stm32-rs/stm32f0xx-hal)

As I began my deep dive into microcontroller systems via *Embedded Rust*, I found that some key features were left out of the official HAL for the SMT32F0. I needed complimentary and center-aligned PWM output for FOC motor control applications. The high level PWM interface in the HAL did not support this, so I added this functionality (my pull request was accepted). It was a very fun and successful introduction to Embedded Rust!

### September 2022 / Present - **LEGv8 Simulator** [GitHub](https://github.com/AdinAck/LEGv8-Simulator)

In preparation for a class I took, I created a powerful simulator for the LEG instruction set, providing many useful tools for writing and debugging LEG assembly code. It has full linting capabilities, breakpoints, step over routines, register and memory access indicators / history. I've tried to make the experience of writing assembly as painless as possible.

### June / July 2021 - **FOC Motor Controller** [GitHub](https://github.com/AdinAck/Motor-Controller)

A motor controller capable of running FOC algorithms to drive BLDC motors with high accuracy, speed, and torque.

**Challenges:** Using the Arduino framework on an embedded micro controller, high density PCB design, avoiding interference between power and digital components, ensuring USB cannot be current source when motor is driven, developing Python hardware interface for automated control

## Previous Work

### **ECE 196: Hands on Project, UCSD** - *Instructional Assistant*

September 2022 - Present

- teach PCB design, embedded systems, BLE interaction with iPhone via Swift, Python, etc.

### **Existential Robotics Lab, UCSD** - *Paid Intern*

March 2022 - September 2022

- Got to do some PCB design, learn a bit about SLAM

### **Spreadtrum Communications Inc, Sorrento Valley** - *Paid Intern*

June 2019 - August 2019

- Created software tools for bring-up to simulate their chip and view which parts of the processor were active given the programmed register values.
- Met my electrical engineering mentor, worked on the office motorized chair and learned about general electronics.