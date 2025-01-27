from turtle import *

#sky 
bgcolor("deepskyblue")


# we making a house (MASSIVE house)

# square
speed(20)
width(6)
color("pink")
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

#end square 

# door (you know what else is massive?)

forward(70)

color("red") 
begin_fill()
left(90)
forward(120)  #door height
right(90)
forward(60)
right(90)
forward(120)
end_fill()

#triangle (roof)

penup()
goto(200,200)
pendown()

color("orange")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#more squares (windows)

#first window

color("yellow")
begin_fill()
penup()
goto(10,170)
pendown()

left(30)
forward(40)

left(90)
forward(50)

left(90)
forward(40)

left(90)
forward(50)
end_fill()

#second window

color("yellow")
begin_fill()
begin_fill()
penup()
goto(190 , 170)
pendown()

forward(50)

left(90)
forward(40)

left(90)
forward(50)

left(90)
forward(40)
end_fill()

#grass 

right(90)

penup()
goto(-1000,0)
pendown()

color("green")
begin_fill()
forward(5000)
right(90)

forward(4000)
right(90)

forward(5000)
right(90)

forward(4000)

end_fill()

#pathway (why am i doing this to myself)

color("gray")
penup()
goto(70 , 0)
pendown()
begin_fill()

right(220)
forward(100)

left(90)
forward(50)

right(90)
forward(100)

left(90)
forward(50)

right(90)
forward(100)

left(90)
forward(50)

right(90)
forward(80)


right(230)
forward(60)

#other way 

left(45)
forward(70)

left(90)
forward(50)

right(90)
forward(100)

left(90)
forward(50)

right(90)
forward(100)

left(90)
forward(50)

right(70)
forward(103)

left(115)
forward(60)
end_fill()

#end pathway (it took soo long)

#sun 
penup()
goto(-320,300)
pendown()
begin_fill()
color("yellow")
circle(50)
end_fill()

#cloud
penup()
goto(-100,250)
pendown()
color("white")
begin_fill()
circle(30)
end_fill()

penup()
goto(-120,290)
pendown()
color("white")
begin_fill()
circle(30)
end_fill()

penup()
goto(-140,230)
pendown()
color("white")
begin_fill()
circle(30)
end_fill()

penup()
goto(-170,270)
pendown()
color("white")
begin_fill()
circle(30)
end_fill()

penup()
goto(-190,240)
pendown()
color("white")
begin_fill()
circle(30)
end_fill()

#idk whats this called
penup()
goto(180, 240)  
setheading(90)  
pendown()

color("orange")  
begin_fill()


forward(50)     
right(90)       
forward(20)    
right(90)       
forward(80)     
right(90)     
forward(20)    

end_fill() 

#end (at this point i have no idea what im doing)

#1st windows cross
penup()
goto(35,170)
pendown()

left(90)
forward(40)

penup()
goto(10,150)
pendown()

left(90)
forward(50)

#2nd windows cross

penup()
goto(165,130)
pendown()

left(90)
forward(40)

penup()
goto(190,150)
pendown()

left(90)
forward(50)

#door handle
penup()
goto(75,70)
pendown()
color("black")
begin_fill()
circle(5)
end_fill()

#sun rays

color("yellow")  # yellow


for angle in range(0, 360, 15):  
    penup()  
    goto(-320, 250)  # center 
    setheading(angle)  # direction
    forward(50)  
    pendown() 
    forward(30)  # length
 

#end sun rays or beams or sxivebi

#nadzvi (forgor in English)

penup()
goto(-200,0)
pendown()

color("chocolate") # CHOCOLATE 

begin_fill()


left(105)

forward(30)
right(180)

left(90)
forward(30)

right(90)
forward(30)

right(90)
forward(30)

right(90)
forward(30)

end_fill()

#green needls things

color("darkgreen")

begin_fill()
left(90)
forward(50)

right(140)
forward(55)

left(140)
forward(30)

right(140)
forward(50)

left(140)
forward(25)

right(130)
forward(60)

# other way

right(95)
forward(60)

right(135)
forward(25)

left(140)
forward(50)

right(140)
forward(30)

left(140)
forward(60)

right(140)
forward(130)

end_fill()

#they told me not to learn programming...

color("black")

penup()
goto(-415,100)
pendown()

right (180)
forward(20)

left(90)
forward(60)

left(90)
forward(20)

left(180)

import turtle as t
import time
import webbrowser
import turtle

t.pensize(5)  
t.color("black")  

# S (they said that its waste of time)
t.penup()
t.setpos(-420, 150) 
t.pendown()
t.forward(3) 
t.backward(3)  
t.circle(-10, -185)  
t.circle(10, -250)  

import turtle as t

# A (they warned me but im still doing it)
t.penup()
t.setpos(-460, 110)  
t.setheading(75) 
t.pendown()
t.forward(45)  
t.setheading(-75) 
t.forward(45)

# A horizontal line (like they would care)
t.penup()
t.setpos(-458, 120)  
t.setheading(0)  
t.pendown()
t.forward(15)  

t.hideturtle()


t.penup()
t.setpos(-457, 100)  
t.pendown()

t.setheading(180)  
t.forward(20)

t.right(90)
t.forward(60)

t.right(90)
t.forward(20)

t.hideturtle()
t.done()

# [ A S ]



webbrowser.open("SOCIAL.MTDV.ME/WATCH?V=TX0J-OU6ZR")

exitonclick()

