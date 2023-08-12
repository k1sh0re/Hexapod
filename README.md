# Hexapod Robot

This documentation provides a brief overview on the design, build and program of an hexapod robot.

## Design
### Body Architecture
The body architecture of any hexapod robot falls into either of the two categories; ones that have a rectangular base with three legs on either side or ones that have a circular / hexagonal base with the legs placed in a radially symmetrical position.

In this project, we have decided to use the later configuration having a circular base as it has better stability, turning abiltiy, and is generally more versatile when it comes to implementing various gaits.

<img src="https://github.com/k1sh0re/Test_repo/assets/109210914/c64da779-f568-4c18-9e2d-f8391b40ec33" width=50% height=50%>

### Leg Structure
The design of the leg decides which gait patterns can be achieved on a hexapod. In general, legs having only 2 DoF, one for the forward and backward motion of the leg and the other to lift the leg up and down is sufficient for the locomotion of an hexapod. But, in this configuration of the legs, the height of the hexapod continously keeps changing throughout its walk cycle. 
Adding a third joint eliminates this dependancy and lets us control the height independant of the walk cycle of our robot. 

<img src="https://github.com/k1sh0re/Test_repo/assets/109210914/fd9bb4c8-5c7c-43b9-a8db-3972321e975b" width=25% height=25%>

### Joints and Actuator positioning
The actuators we used are high torque MG996R servo motors having 180&deg; motion. These motor came with servo mounts which we intended to use as the joints for our hexapod.

The coxa motors are attached to the main body using servo mounts, with the coxa-femur
motors directly coupled to it. The femur and tibia motors are linked using two U-shaped servo mounts. The tibia links were laser-cut parts and were directly attached to the tibia servos.

### Modelling
With the body structure of our hexapod finalized, we proceeded to build a 3d model in Solidworks to get a general idea on how the hexapod would look like once the building process has been finished. All components that needed to be laser cut / 3d printed were also designed during this stage.

<img src="https://github.com/k1sh0re/Test_repo/assets/109210914/2ebc3f88-8633-469d-bb75-58bcef169655" width=25% height=25%>
&emsp;&emsp;&emsp;&emsp;
<img src="https://github.com/k1sh0re/Test_repo/assets/109210914/71037ccc-ab4a-45a5-a0a9-6cb93dc01686" width=25% height=25%>



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

<img src="https://github.com/k1sh0re/Test_repo/assets/109210914/18a70860-a5f2-41cf-996e-cded2be315aa" width=30% height=30%>

### Trajectory Generator

The trajectory followed by each leg follows a fixed path that goes through a series of phases in a repeating sequence: lift-off, swing, touchdown and stance.

<img src="https://github.com/k1sh0re/Test_repo/assets/109210914/93808192-e14e-472b-acc7-05579856b72f" width=30% height=30%>

### Gait Planning 

Various types of gaits can be implemented on an hexapod owing to the stability that the six legs can provide. 
We decided to implement a tripod gait as it provides a perfect balance between speed and stability.


## Results
We were able to achieve basic locomotion in four directions and the code was also written so as to make it easier to upgrade into omni-directional locomotion.

We also tested our robot on how effectively it can climb over obstacles and were able to achieve a maximum climbing height of about 10cm.


<img src="https://github.com/k1sh0re/Test_repo/assets/109210914/63ed234b-58b5-48dc-9710-5eac494498a7" width=35% height=35%>
&emsp;&emsp;&emsp;&emsp;
<img src="https://github.com/k1sh0re/Test_repo/assets/109210914/9bdc7c75-961a-47eb-a748-7cbda18ee4c3" width=35% height=35%>









