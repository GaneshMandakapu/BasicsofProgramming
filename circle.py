import turtle
mn = turtle.Screen()
ganesh = turtle.Turtle()
while True:
	ganesh.forward(1)
	ganesh.left(1.15)
	if abs(ganesh.pos()) < 1:
		break
