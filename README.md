# Contact

Adin Ackerman | (760) 626-6570 | adinackerman@gmail.com

# Portfolio

[GitHub](https://github.com/AdinAck)

[2021 Portfolio](https://www.youtube.com/watch?v=g3itfoOmj-A)

[Maker Portfolio for my MIT Application](https://www.youtube.com/watch?v=01xOdK2FQu4)

# About Me

I have been passionate about computers and electronics for many years. Most of my education is informal, as I spent my days after school learning about electronics and computer engineering. I have a deep passion for the interaction between hardware and software, with a focus on "user" experience and education as well. All of my projects are open source, and I try to make it as easy as possible for other engineers to learn from my work. For all of my projects, I take extra time and care to make sure I do everything *right*, I am real stringent about good work being done, doing the best I can to live up to the high standard of experts in the industry.

# Experience

### **Electrical Engineering** - *3 years*

I've designed and tested 15 or so PCBs over the years, and have loved every second of it. I've gained a very diverse range of knowledge and experience from my PCB projects, and have learned most of what I know simply by reading datasheets or application notes for the various ICs I intend to use... in addition to the knowledge gained by solving the many problems I have faced, of course.

- Rapid Prototyping
- PCB Design
  - Altium
  - KiCAD
- Embedded Systems
  - Arduino
  - ASF4 (Atmel SAM)
  - RP2040, Espressif SDK
- Debugging
  - Standard hardware debugging practices
  - Recently began using lldb to debug through a debugger chip, and on normal C, C++ programs
- Reflow Soldering (and of course hand held soldering)
- Oscilloscope Usage

Recently, I have been learning ARM64 assembly for Apple Silicon processors, but it seems to be very similar to ARM32 assembly so far, so I am preparing myself for learning assembly for embedded systems.

### **Computer Science** - *4 years*

I'm a total Python nerd. I take pride in making my code readable (in true Python fashion), optimized, and well documented. I've got all the Python tricks up my sleeve!

- CPython/MicroPython/CircuitPython
- Advanced Data Structures and OOP Practices
- Sockets
- Tkinter
- NumPy, Tensorflow, CoreML, etc.
- IC Drivers / Hardware Interfaces

Through Python, I have become deeply ingrained in the OOP mindset, and I am constantly learning more. Another high level language I enjoy is Swift, there are many Swift projects on my [GitHub](https://github.com/AdinAck) to see.

# Notable Projects

### September 2021 / Present - **Educational SCARA Motion Control System** (WIP)

Using a custom FOC motor controller (below), a friend and I created a "robot arm" -- one could call it -- for introducing young engineers into robotics engineering. Thanks to the usage of my custom motor controller, no gears are required since FOC allows for maximum torque at all\* velocities, in conjunction with very high precision and accuracy.

A professor of ours has given us $500 to continue development of the robot arm, and to set up an educational display for students to easily access. The display will be incorporated into the intro to Electrical Engineering course curriculum. A popular maker space at our university graciously provided us space and resources for our exhibit, and we are very grateful!

We plan on providing 3-4 deep-dive pathways, Mechanical Engineering, Electrical Engineering, Software, and possibly Machine Learning. Of course, we will explain the fusion of these disciplines, and good practices when it comes to system integration.

### June / July 2021 - **FOC Motor Controller** [GitHub](https://github.com/AdinAck/Motor-Controller)

A motor controller capable of running FOC algorithms to drive BLDC motors with high accuracy, speed, and torque.

One of my coolest projects yet. FOC control is a fairly new and highly advanced method of controlling BLDC motors that I have been interested to learn about for a long time.

Challenges involved in this project:

- Using the Arduino framework on an embedded micro controller
- High density PCB design
- Avoiding interference between power and digital components (solid ground plane)
- Ensuring USB cannot be current source when motor is driven
- Developing Python hardware interface for automated control

### May / July 2021 - **Battery Evaluator** [GitHub](https://github.com/AdinAck/Battery-Evaluator)

A device for benchmarking batteries, and creating models for accurately predicting the state of charge of a battery given it's voltage. A very practical tool for determining not only *if* a battery is suitable for you application, but how to incorporate it.

Tests include:

- Internal resistance
- Constant current discharge
- Constant power discharge

The challenge for this project was designing a programmable constant current sink, which I have solved by utilizing the on-board DAC of the microcontroller as the non-inverting input to an op-amp driving the MOSFETs that discharge the battery, with the inverting input being the voltage across the current-sense resistors.

### July / August 2020 - **Battery Management System** [GitHub](https://github.com/AdinAck/SuperBMS)

This was my first PCB project. I gained invaluable experience tackling the issues faced when designing and building a custom circuit (especially on a PCB)

- Reading datasheets
- Creating software to interface with various ICs
- MOSFETs
- Optoelectronics
- Lithium batteries
- Debugging and resolving complex problems

# Previous Internships

### Existential Robotics Lab, UCSD - *Paid Intern*

March 2022 - Present

- The work to be done is rather open ended, but I have settled into handling mostly "behind the scenes" type work, getting the basic drone functions up and running so the grad students have a platform to work their magic.

- I have also been doing PCB work for them, by my own volition.

- Since I have experience with hobby grade quadcopters, I have been surprisingly useful when diagnosing issues, flying the quads, and of course assembling them.

### **Spreadtrum Communications Inc, Sorrento Valley** - *Paid Electrical Engineering Intern*

June 2019 - August 2019

- Created software tools for bring-up to simulate their chip and view which parts of the processor were active given the programmed register values.
- Met my electrical engineering mentor, worked on the office motorized chair and learned about general electronics.

# Education

### **San Dieguito Academy** - *High School*

August 2016 - June 2021

GPA: 4.3

### **UC San Diego** - *B.S. Electrical Engineering*

September 2021 - June 2025

GPA: 3.9