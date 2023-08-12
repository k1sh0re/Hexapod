from trajectory_generator import trajectory
from home_position import position
from adafruit_servokit import ServoKit
import time

md_1 = ServoKit(channels=16, address=0x40, frequency=50)
md_2 = ServoKit(channels=16, address=0x41, frequency=50)
md_1 = md_1.servo
md_2 = md_2.servo 

position()

count =15
delay = 0.005/freq/2

tr = [0]*6
for i in range(5):
    trajectory(i)
    tr[i] = traj

while count>0:
    for i in range(2*freq):
        md_1[0].angle= 90 + tr[0][i][0] 
        md_1[1].angle = tr[0][i][1]
        md_1[2].angle = tr[0][i][2]
        
        time.sleep(delay)
        
        md_1[4].angle = 90 + tr[1][i][0] 
        md_1[5].angle = tr[1][i][1]
        md_1[6].angle = tr[1][i][2]
        
        time.sleep(delay)
        
        md_1[8].angle = 90 + tr[2][i][0]-15 #bias
        md_1[9].angle = tr[2][i][1]
        md_1[10].angle = tr[2][i][2] 
        
        time.sleep(delay)
        
        md_2[0].angle = 90 + tr[3][i][0]
        md_2[1].angle = tr[3][i][1]
        md_2[2].angle = 180 - tr[3][i][2]
        
        time.sleep(delay)
        
        md_2[4].angle = 90 + tr[4][i][0]
        md_2[5].angle = tr[4][i][1]
        md_2[6].angle = 180 - tr[4][i][2]
        
        time.sleep(delay)
        
        md_2[8].angle = 90 + tr[5][i][0]
        md_2[9].angle = tr[5][i][1]
        md_2[10].angle = 180 - tr[5][i][2]-15 #bias
             
        time.sleep(delay)
    count -= 1


