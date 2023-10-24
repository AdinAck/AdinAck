# Adin Ackerman

(760) 626-6570 | aiackerman@ucsd.edu | [GitHub](https://github.com/AdinAck) | [2021 Portfolio](https://www.youtube.com/watch?v=g3itfoOmj-A) | [Maker Portfolio for my MIT Application](https://www.youtube.com/watch?v=01xOdK2FQu4)

## About Me

I have been passionate about computers and electronics since a young age. Most of my education is informal, as I spent my days after school learning about electronics and software. I strive for perfection to the best of my ability with all of my projects. I'm not afraid to do things by hand, I build my own tools, take the time to do things *right* and don't compromise performance or architecture in the interest of expediency.

## Education

### **UC San Diego** - *B.S. Electrical Engineering* - 2025

GPA: 3.9

## Experience

### **Electrical Engineering** - *4 years*

- **PCB Design:** Altium/KiCAD, created power supplies, motor control systems, battery management systems
- **Embedded Systems:** Embedded Rust, Baremetal - IC drivers, peripheral interfaces, controls, validation

### **Software Engineering** - *5 years*

- Advanced design, architecture, and OOP practices. I enjoy writing documentation and developing verbose interfaces.
- Bluetooth - I have made my own BLE stacks on the server and client side, created generic frameworks for BLE between embedded devices and personal devices.

## Notable Projects

### May / July 2023 - **Headlights** [GitHub](https://github.com/AdinAck/Onewheel-Headlights)

I created a 100v current-mode SMPS to drive high voltage headlights (that I also made) for my self balancing electric skateboard. I learned a lot about the half-bridge topology, gate driving via bootstrapping, preventing cross-over, making a sufficiently large LC filter, controls, and in software, how to ensure all conditions lead to a failsafe state. I contributed to multiple Embedded Rust projects during this time. I added complementary and center aligned PWM to [stm32f0xx-hal](https://github.com/stm32-rs/stm32f0xx-hal), a procedural macro for generating BLE advertisement data to [nrf-softdevice](https://github.com/embassy-rs/nrf-softdevice), and extended functionality of [heapless](https://github.com/rust-embedded/heapless). I created my own crates (like [embedded-command](https://github.com/AdinAck/embedded-command)) as well.

### September 2022 - **LEGv8 Simulator** [GitHub](https://github.com/AdinAck/LEGv8-Simulator)

In preparation for a class I took, I created a powerful simulator for the LEG instruction set, providing many useful tools for writing and debugging LEG assembly code. It has full linting capabilities, breakpoints, step over routines, register and memory access indicators / history. I've tried to make the experience of writing assembly as painless as possible.

### June / July 2021 - **FOC Motor Controller** [GitHub](https://github.com/AdinAck/Motor-Controller)

A motor controller capable of running FOC algorithms to drive BLDC motors with high accuracy, speed, and torque.

**Challenges:** Using the Arduino framework on an embedded micro controller, high density PCB design, avoiding interference between power and digital components, ensuring USB cannot be current source when motor is driven, developing Python hardware interface for automated control

## Previous Work

### **ECE 196: Hands on Project, UCSD** - *Instructional Assistant*

September 2022 - Present

- teach PCB design, embedded systems, BLE interaction with iPhone via Swift, Python, Rust, etc.

### **Existential Robotics Lab, UCSD** - *Paid Intern*

March 2022 - September 2022

- Got to do some PCB design, learn a bit about SLAM

### **Spreadtrum Communications Inc, Sorrento Valley** - *Paid Intern*

June 2019 - August 2019

- Created software tools for bring-up to simulate their chip and view which parts of the processor were active given the programmed register values.
- Met my electrical engineering mentor, worked on the office motorized chair and learned about general electronics.