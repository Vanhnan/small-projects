import turtle
import time
import random

#screen
screen = turtle.Screen()
screen.title("KILLER TURTLE")
screen.setup(600,600)
#screen.bgcolor("black")
screen.bgpic("star_wars.gif")
screen.tracer(0)

#border
border = turtle.Turtle()
border.hideturtle()
border.penup()
border.goto(-300,300)#left up corner
border.pendown()
border.goto(300,300)
border.goto(300,-300)
border.goto(-300,-300) 
border.goto(-300,300)

#man 
man = turtle.Turtle()
man.shape("square")
man.color("orange")
man.penup()

#killer turtle
killer = turtle.Turtle()
killer.shape("turtle")
killer.color("red")
killer.penup()
killer.goto(-200,0)


#man control
screen.onkeypress(lambda: man.setheading(90), "8")#up
screen.onkeypress(lambda: man.setheading(270), "2")#down
screen.onkeypress(lambda: man.setheading(180), "4")#left
screen.onkeypress(lambda: man.setheading(0), "6")#right


screen.onkeypress(lambda: man.setheading(220), "1")#left down
screen.onkeypress(lambda: man.setheading(140), "7")#up left
screen.onkeypress(lambda: man.setheading(320), "3")#right down
screen.onkeypress(lambda: man.setheading(40), "9")#up right

screen.listen()

while True:

	screen.update()
	
	#man moving
	man.forward(25)

	#killer turtle moving
	killer.forward(25)
	killer.setheading(killer.towards(man)+random.randint(0,50))

	#collapse
	if man.distance(killer)<20:
		screen.bgcolor("red")
		break

	#border collapse
	if man.xcor()>300 or man.xcor()<-300:
		screen.bgcolor("red")
		break
	if man.ycor()>300 or man.ycor()<-300:
		screen.bgcolor("red")
		break

	time.sleep(0.2)

screen.mainloop()