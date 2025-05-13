from turtle import *

#we want to paint a house

#step 1: draw a square


speed(90)
width(7)
color("red")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door

forward(70) 
color("brown")
begin_fill()
left(90)
forward(120)    #height of the door
right(90)
forward(60)
right(90)
forward(120)
right(90)
forward(60)
end_fill()
#end of door

#drawing a roof

penup()
goto(200, 200)
pendown()

color("purple")
begin_fill()
right(45)
forward(150)
left(93)
forward(145)
end_fill()

penup()
goto(130, 130)
pendown()

color("cyan")
begin_fill()
left(132)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
end_fill()

penup()
goto(69, 130)
pendown()


begin_fill()
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
end_fill()


exitonclick()