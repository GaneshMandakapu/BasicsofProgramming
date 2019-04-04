from turtle import *
def blacksq(x):
    #angle=90
    for i in range(x//2):
        fd(x);left(90)
        fd(1);left(90)
        fd(x);right(90)
        fd(1);right(90)
    #penup();down();pendown()
    penup();fd(x);right(90);fd(x);left(90);pendown()

        
def whitesq(y):
    x=10;n=4
    angle = 360//n
    for i in range(n):
        fd(x);left(angle)
    penup();fd(x);pendown()


def drawrow1():
    for a in range(4):
        blacksq(10)	
        whitesq(4)



def drawrow2():
    penup();right(90+90);"""fd(10);right(90)""";pendown()
    for b in range(4):
        whitesq(4)
        blacksq(10)
    

for c in range(4):
    drawrow1()
    penup();left(90);fd(10);left(90);fd(80);pendown()
    drawrow2()
    penup();left(90);fd(10);left(90);fd(80);pendown();
    penup();right(90+90);"""fd(10);right(90)""";pendown()
	
fd(80)
done()
