# Adin Ackerman

### Contact

(760) 626-6570 | adinackerman@gmail.com

### Portfolio

[GitHub](https://github.com/AdinAck) | [2021 Portfolio](https://www.youtube.com/watch?v=g3itfoOmj-A) | [Maker Portfolio for my MIT Application](https://www.youtube.com/watch?v=01xOdK2FQu4)

## About Me

I have been passionate about computers and electronics for many years. Most of my education is informal, as I spent my days after school learning about electronics and computer engineering. I have a deep passion for the interaction between hardware and software, with a focus on "user" experience and education as well. For all of my projects, I take extra time and care to make sure I do everything *right*, I am real stringent about good work being done.

## Experience

### **Electrical Engineering** - *4 years*

I've designed and tested 15 or so PCBs over the years. Through this, I have gained a very diverse range of knowledge and experience from my PCB projects, and have learned most of what I know simply by reading datasheets or application notes for the various ICs I intend to use... in addition to the knowledge gained by solving the many problems I have faced, of course.

- **PCB Design:** Altium/KiCAD, simple digital systems, "high" current design, standard PCB design practices, strive for elegance, redundancy
- **Embedded Systems:** Arduino, ASF4 (Atmel SAM), RP2040, ESP-IDF
- **Debugging:** Standard hardware debugging practices, using lldb to debug microcontroller through a debugger chip, and on normal C, C++ programs, oscilloscopes, bench power supplies, etc.
- **Soldering:** By hand, reflow (with an oven or sand in a pan)

### **Software Engineering** - *5 years*

I'm a total Python nerd. I take pride in making my code readable (in true Python fashion), optimized, and well documented. I've got all the Python tricks up my sleeve!

- Advanced Data Structures and OOP Practices, advanced threading techniques, abstraction layer design, networking (sockets, http servers, etc.), IC Drivers / Hardware Interfaces
- Bluetooth - I have done multiple projects involving an ESP32 embedded on a PCB, running a GATT server accessed by an app made in Swift (another one of my favorite languages)

While I have low level programming experience (C, ARM Assembly), I am still learning and would not consider myself to have mastered these. By the end of this year that may change.

## Notable Projects

### September 2022 / Present - **LEGv8 Simulator** [GitHub](https://github.com/AdinAck/LEGv8-Simulator)

In preparation for a class I am taking this quarter, I created a powerful simulator for the LEG instruction set, providing many useful tools for writing and debugging LEG assembly code. (A side project inspired by this is a compiler from a high level language to  LEG {works OK so far, but more to do})

### September 2021 / Present - **Educational SCARA Motion Control System** (WIP) [Home Page](https://mew463.github.io/SCARA-Arm.html)

Using my custom FOC motor controller (below), a friend and I created a "robot arm" for introducing young engineers into robotics engineering. Thanks to the usage of my custom motor controller, the robot arm is movable by humans, and no gears are required since FOC allows for precise position control. A professor liked our project and happily funded its development. We were even given a designated section of our local maker space.

### June / July 2021 - **FOC Motor Controller** [GitHub](https://github.com/AdinAck/Motor-Controller)

A motor controller capable of running FOC algorithms to drive BLDC motors with high accuracy, speed, and torque.

Challenges involved in this project:

- Using the Arduino framework on an embedded micro controller, high density PCB design, avoiding interference between power and digital components (solid ground plane), ensuring USB cannot be current source when motor is driven, developing Python hardware interface for automated control

### ... and many more [GitHub](https://github.com/adinack)

## Previous Internships

### Existential Robotics Lab, UCSD - *Paid Intern*

March 2022 - September 2022

- Got to do some PCB design, learn a bit about SLAM

### **Spreadtrum Communications Inc, Sorrento Valley** - *Paid Intern*

June 2019 - August 2019

- Created software tools for bring-up to simulate their chip and view which parts of the processor were active given the programmed register values.
- Met my electrical engineering mentor, worked on the office motorized chair and learned about general electronics.

## Education

### **UC San Diego** - *B.S. Electrical Engineering*

September 2021 - June 2025

Sophomore

GPA: 3.9