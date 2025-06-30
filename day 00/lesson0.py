from turtle import *

#we want to paint a house

#step 1: draw a square
width(7)
speed(30)
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door
forward(70)
left(90)

forward(120) #height ofthe door
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

color('black')
left(30)
forward(20)

color('brown')
left(90)
forward(45)
right(90)
forward(60)
right(90)
forward(45)
color('black')
right(90)
forward(80)
right(90)
forward(200)
right(90)

forward(20)
right(90)
color('brown')
forward(45)
left(90)
forward(60)
left(90)
forward(45)

color('black')
left(90)
forward(65)

penup()
goto(-100, -100)
pendown()
color('white')

exitonclick()