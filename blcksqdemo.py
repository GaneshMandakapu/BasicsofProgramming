from turtle import *
x = 10
n=4
angle = 360//n
def polygon(n,x):
    for i in range(n):
        fd(x);left(angle)
    #fd(x)
for a in range(50):
    polygon(4,a)
    a=a-1
