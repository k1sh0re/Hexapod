import time 
from adafruit_servokit import ServoKit
from kinematics import ik

x_ini = 0.2
y_ini = 0
z_ini = -0.05

def position():
    t1,t2,t3 = ik(x_ini,y_ini,z_ini)
    servo_id = ServoKit(channels=16, address=0x40, frequency=50)
    servo_id_2 = ServoKit(channels=16, address=0x41, frequency=50)
    servo_id.servo[0].angle = 90+t1
    servo_id.servo[1].angle = t2
    servo_id.servo[2].angle = t3

    time.sleep(0.05)

    servo_id.servo[4].angle = 90+t1
    servo_id.servo[5].angle = t2
    servo_id.servo[6].angle = t3

    time.sleep(0.05)


    servo_id.servo[8].angle = 90- t1-15
    servo_id.servo[9].angle = t2
    servo_id.servo[10].angle = t3 -30

    time.sleep(0.05)

    servo_id_2.servo[8].angle = 90+t1
    servo_id_2.servo[9].angle = t2
    servo_id_2.servo[10].angle = 180-t3 -15 

    time.sleep(0.05)

    servo_id_2.servo[0].angle = 90+t1
    servo_id_2.servo[1].angle = t2
    servo_id_2.servo[2].angle = 180-t3

    time.sleep(0.05)

    servo_id_2.servo[4].angle = 90+ t1
    servo_id_2.servo[5].angle = t2
    servo_id_2.servo[6].angle = 180-t3 

        



