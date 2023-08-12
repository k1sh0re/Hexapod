from math import *
import numpy as np
import time 
from kinematics import ik

#Setting up the starting position
x_ini = 0.12
y_ini = 0
z_ini = -0.10

# Step height and length
d_max = 0.08
h_max = 0.15

freq = 50
traj = []

#These angles provide the phase that each leg should move in for motion in forward direction.

th_angles = [0,4*pi/3,2*pi/3,0,4*pi/3,2*pi/3]

def trajectory(leg_id):
    global traj
    theta = th_angles[leg_id]
    
    if leg_id in [0,2,4]:
        phase = 1
    elif leg_id in [1,3,5]:
        phase = 0
    
    traj = []
    x = x_ini
    z = z_ini
    y = y_ini
    k = pi/d_max
    d = 0
    for i in range(freq):
        
        
        x = x + d_max*cos(theta)/freq
        y = y + d_max*sin(theta)/freq
        d = d + phase*d_max/freq
        z = z_ini + h_max*sin(d*k)
        traj.append([x,y,z])
        #print(d)
        
    for i in range(freq):
        
        x = x - d_max*cos(theta)/freq
        y = y - d_max*sin(theta)/freq
        d = d + (1-phase)*d_max/freq
        z = z_ini + h_max*sin(d*k)
        traj.append([x,y,z])
    
    for i in range(2*freq):
        x,y,z = traj[i][0],traj[i][1],traj[i][2]
        traj[i][0],traj[i][1],traj[i][2] = ik(x,y,z)
           



        
    
    
    
        