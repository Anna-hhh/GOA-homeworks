
from turtle import *


setup(width=1250, height=725) # screen size to match the background image


# background color and image
bgcolor("#cbfcf4")
bgpic("c:/Users/Dell/OneDrive/Desktop/GOA-homeworks/Level 06/Homework/mountain.gif" )


# turtle speed and width
speed(0)  # max speed
width(4)


# drawbridge
color("#964B00" , "#B5651d") # line color  #964B00 ,  fill color  #B5651d
penup()
goto(-80,-359)
pendown()
begin_fill()
left(80)
forward(200)
right(80)
forward(100)
right(80)
forward(200)
right(100)
forward(166)
end_fill()

right(99)
forward(200)

# gate
color("#b5651d")
begin_fill()
left(9)
forward(150)

for _ in range(35):
    right(5)
    forward(4.4)
right(5)
forward(148)
right(90)
forward(100)
end_fill()

# outline for the gate
pensize(10)
right(100)
color("#964B00")
left(9)
forward(150)

for _ in range(35):
    right(5)
    forward(4.4)
right(5)
forward(148)
right(90)
forward(100)

pensize(3) 

right(179)
forward(50)
left(90)
forward(200)

right(180)
forward(200)
left(90)
forward(55)

# towers
pensize(5)
color("slate gray","gray" )
begin_fill()
forward(50)
left(90)
forward(250)  # size
right(45)
for _ in range(30):
    right(3)
    forward(4)
right(45)
forward(250) # size
right(45)
for _ in range(30):
    left(-3)
    forward(4)
end_fill()

color("slate gray","#B5651d" )
begin_fill()
right(45)
forward(300) 
right(45)
for _ in range(30):
    right(3)
    forward(4)
right(45)
forward(50)
right(135)
for _ in range(30):
    left(3)
    forward(4)
end_fill()

right(135)
forward(65)

# 
color("#Ffd343")
begin_fill()
left(30)
forward(30)
right(95)
forward(15)
right(55)
forward(38)

left(40)
forward(15)

left(86)
forward(25)
right(95)
forward(25)
right(95)
forward(25)

left(75)
forward(15)

left(55)
forward(30)
right(55)
forward(15)
right(88)
forward(32.5)
right(120)
for _ in range(30):
    left(2.9)
    forward(4)
end_fill()












# keep window open and close on click
exitonclick()