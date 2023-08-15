# Hexapod Robot

This documentation provides a brief overview on the design, build and program of an hexapod robot.

<p align="center">
<img src="https://github.com/k1sh0re/Hexapod/assets/109210914/edf9d46d-bf5b-4091-8bda-bf5ae9aaeb58" width=40% height=40%>
</p>

## Design
### Body Architecture
The body architecture of any hexapod robot falls into either of the two categories; ones that have a rectangular base with three legs on either side or ones that have a circular / hexagonal base with the legs placed in a radially symmetrical position.

In this project, we have decided to use the later configuration having a circular base as it has better stability, turning abiltiy, and is generally more versatile when it comes to implementing various gaits.

<p align="center">
<img src="https://github.com/k1sh0re/Hexapod/assets/109210914/f87b9701-0dbf-4207-b878-81b764568ff0" width=50% height=50%>
</p>

### Leg Structure
The design of the leg decides which gait patterns can be achieved on a hexapod. In general, legs having only 2 DoF, one for the forward and backward motion of the leg and the other to lift the leg up and down is sufficient for the locomotion of an hexapod. But, in this configuration of the legs, the height of the hexapod continously keeps changing throughout its walk cycle. 
Adding a third joint eliminates this dependancy and lets us control the height independant of the walk cycle of our robot. 

<p align="center">
<img src="https://github.com/k1sh0re/Hexapod/assets/109210914/161c9664-27c2-4200-9f5c-cd9f9f229a44" width=25% height=25%>
</p>

### Joints and Actuator positioning
The actuators we used are high torque MG996R servo motors having 180&deg; motion. These motor came with servo mounts which we intended to use as the joints for our hexapod.

The coxa motors are attached to the main body using servo mounts, with the coxa-femur
motors directly coupled to it. The femur and tibia motors are linked using two U-shaped servo mounts. The tibia links were laser-cut parts and were directly attached to the tibia servos.

### Modelling
With the body structure of our hexapod finalized, we proceeded to build a 3d model in Solidworks to get a general idea on how the hexapod would look like once the building process has been finished. All components that needed to be laser cut / 3d printed were also designed during this stage.

<p align="center">
<img src="https://github.com/k1sh0re/Hexapod/assets/109210914/4e9e3346-94ee-4a90-ac64-494e93ca86af" width=35% height=35%>
&emsp;&emsp;&emsp;&emsp;
<img src="https://github.com/k1sh0re/Hexapod/assets/109210914/f382d3a7-7519-40a7-b4da-0ab7d0914267" width=35% height=35%>
</p>

## Build

### Electronic Components
The Microcontroller used for our robot is a Rapberry Pi 3b+ which was chosen due to its fast computational abilities, capable of real time trajectory generation. Additionally, it gives us the flexibility to add more features to our hexapod in the future.

The actuators used are the MG996R servos which have sufficient torque rating.

To run the servos we used two PCA9685 motor drivers, each capable of controlling upto 16 individual servos. These drivers can easily be chained together to control more servos and can be interfaced with a Raspberry Pi using the PCA9685 library provided by Adafruit.

The Raspberry Pi and the servos both run on 5V, this, coupled with the high stall current of the servos meant that we needed a power source having high current output at 5V. 
After going through a lot of options for the power supply, we finalized on an SMPS capable of providing upto 24A at 5V. 

### Chassis 

A major part of the chassis body is made up of servo mounts and the rest of the parts which include the top and bottom circular plates and the tibia joints were laser cut using acrylic sheets.

## Software
The software was divided into modules based on their functionalities for ease of maintenance, ease of error resolving and scalability in the future.

### Leg Kinematics
The link lengths of the leg were assigned to be l1, l2, and l3 and with the use of inverse kinematics, we obtained equations to calculate the joint angles needed to achieve a desired end effector position and orientation.

<p align="center">
<img src="https://github.com/k1sh0re/Hexapod/assets/109210914/97b27011-42a6-4451-b72c-f28c6974bda7" width=30% height=30%>
</p>


### Trajectory Generator

The trajectory followed by each leg follows a fixed path that goes through a series of phases in a repeating sequence: lift-off, swing, touchdown and stance.

<p align="center">
<img src="https://github.com/k1sh0re/Hexapod/assets/109210914/1402d588-8435-4105-a687-28dc82807c49" width=30% height=30%>
</p>

### Gait Planning 

Various types of gaits can be implemented on an hexapod owing to the stability that the six legs can provide. 
We decided to implement a tripod gait as it provides a perfect balance between speed and stability.


## Results
We were able to achieve basic locomotion in four directions and the code was also written so as to make it easier to upgrade into omni-directional locomotion.

We also tested our robot on how effectively it can climb over obstacles and were able to achieve a maximum climbing height of about 10cm.


<p align="center">
<img src="https://github.com/k1sh0re/Hexapod/assets/109210914/9630f76b-f5fd-4829-8fb5-cb3e899db43a" width=35% height=35%>
&emsp;&emsp;&emsp;&emsp;
<img src="https://github.com/k1sh0re/Hexapod/assets/109210914/7e64cb96-ba64-4c51-b7f0-9627a164a1d5" width=35% height=35%>
</p>








