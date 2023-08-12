from math import *
import numpy as np

len1 = 0.16
len2 = 0.15

def fk(t1,t2,t3):
    t1 = t1/180*pi
    t2 = t2/180*pi
    t3 = t3/180*pi
    p1 = len1*cos(t2) + len2*cos(t3-t2)
    x = p1*cos(t1)
    y = p1*sin(t1)
    z = len1*sin(t2) - len2*sin(t3-t2)
    return x,y,z


def ik(x,y,z):
    t1 = (atan2(y,x))*180/pi
    phi1 = atan2(z,(x**2+y**2)**0.5)
    cos_phi = (len1**2 + x**2 + y**2 + z**2 - len2**2)/2/len1/(x**2+y**2+z**2)**0.5
   
    p =[abs((1-cos_phi**2)**0.5), cos_phi]
    phi2 = atan2(p[0],p[1])

    cos_phi = (len2**2 + x**2 + y**2 + z**2 - len1**2)/2/len2/(x**2+y**2+z**2)**0.5
    p =[abs((1-cos_phi**2)**0.5), cos_phi]
    phi3 = atan2(p[0],p[1])

    t2 = (phi1 + phi2)*180/pi
    t3 = (phi2 + phi3)*180/pi
    return int(t1),int(t2),int(t3)