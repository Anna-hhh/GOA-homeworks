from turtle import *

# Set up the background
bgcolor("deepskyblue")


# Draw the house

# Main square structure
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

# End of square 

# Draw the door

forward(70)

color("red") 
begin_fill()
left(90)
forward(120)  # Door height
right(90)
forward(60)   # Door width
right(90)
forward(120)
end_fill()

# Draw the triangular roof

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

# Draw the windows


# First window

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

# Second window

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

# Draw the grass

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

# Draw the pathway

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

# end pathway 

# Draw the sun
penup()
goto(-320,300)
pendown()
begin_fill()
color("yellow")
circle(50)
end_fill()

# Draw clouds
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

# Draw the chimney

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

#end of chimneys

# Draw window crossbars
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

# Draw the door handle
penup()
goto(75,70)
pendown()
color("black")
begin_fill()
circle(5)
end_fill()

# Draw sun rays

color("yellow")  # yellow


for angle in range(0, 360, 15):  
    penup()  
    goto(-320, 250)  # Sun center
    setheading(angle)  # Set direction
    forward(50)      # Move outwards
    pendown() 
    forward(30)  # Draw ray
 
#End of sun rays

# Draw a tree

penup()
goto(-200,0)
pendown()

color("chocolate") 

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

# Draw tree foliage

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

# End of needls

end_fill()


hideturtle()


exitonclick()