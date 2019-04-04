from turtle import *


def blacksq(x):
    #angle=90
	
    for i in range(x//2):
        fd(x);left(90)
        fd(1);left(90)
        fd(x);right(90)
        fd(1);right(90)
blacksq(100)
