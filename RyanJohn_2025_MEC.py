from turtle import *
from math import sqrt
speed(0)

# maximize the turtle graphics window
Screen().getcanvas().winfo_toplevel().state('zoomed')

#to create segments of circles
def seg(length,x,y):
    x1,y1 = pos()
    r=length/sqrt(2)
    seth(towards(x,y)-45)
    circle(r,90)
    seth(towards(x1,y1)-45)
    circle(r,90)
    left(45)

#to create sectors of circles
def sector(radius,extent,colour):
    color(colour)
    begin_fill()
    circle(radius,extent)
    left(90)
    fd(radius)
    left(180-extent)
    fd(radius)
    left(90)
    end_fill()
    circle(radius,extent)

#to create square
def square(side):
    begin_fill()
    for i in range(4):
        fd(side)
        left(90)
    end_fill()

#to create layers of squares
def layer(radius,angle,colour):
    seth(angle)
    color(colour)
    for i in range(24):
        square(150)
        left(135)
        pu()
        circle(radius,15)
        right(135)
        pd()


#START OF POOKALAM

#outline circles
teleport(0,350)
seth(0)
color("#0f6918")
for i in range(48):
    begin_fill()
    circle(7)
    end_fill()
    pu()
    circle(-350,7.5)
    pd()

    
#background circle
teleport(0,-350)
begin_fill()
circle(350)
end_fill()


#1st layer
teleport(0,135)
seth(180)
pu()
circle(135,7.5)
pd()
layer(135,52.5,"#6e3c2a")
    

#2nd layer
teleport(0,135)
layer(135,45,"brown")


#3rd layer
teleport(0,95)
layer(95,45,"#ad705a")


#4th layer
teleport(0,95)
seth(180)
pu()
circle(95,7.5)
pd()
layer(95,52.5,"#de910d")


#spiral sectors
teleport(0,-270)
seth(0)
circle(270)
r=270
for h in range(3):
    for i in range(6):
        for colour in ["#c90c35","orange","yellow"]:
            sector(r,20,colour)
    r=r-20
    pu()
    left(90)
    fd(20)
    rt(90)
    circle(r,5)
    pd()

#white circles in the spiral
teleport(0,-267)
seth(0)
pu()
circle(267,10)
pd()
r=267
color("white")
for h in range(3):
    for i in range(18):
        pu()
        circle(r,20)
        pd()
        begin_fill()
        circle(7)
        end_fill()
    r=r-20
    pu()
    left(90)
    fd(20)
    rt(90)
    circle(r,5)
    pd()


#background for inner pattern
teleport(0,-210)
seth(0)
color("#dea576")
begin_fill()
circle(210)
end_fill()




#inner pattern
teleport(0,210)
color("brown")
begin_fill()
for i in range(12):
    x,y=xcor(),ycor()
    seg(420,-x,-y)
    pu()
    circle(210,15)
    pd()
end_fill()





#yellow circle
teleport(0,-100)
seth(0)
color("yellow")
begin_fill()
circle(100)
end_fill()


#orange design
teleport(100,0)
color("orange")
begin_fill()
for i in range(12):
    seg(100,0,0)
    pu()
    circle(100,30)
    pd()
end_fill()


#green design
teleport(70,0)
color("#0f6918")
begin_fill()
for i in range(12):
    seg(70,0,0)
    pu()
    circle(70,30)
    pd()
end_fill()


#smallest design
teleport(20,0)
pu()
circle(20,30)
pd()
color("red")
begin_fill()
for i in range(12):
    seg(20,0,0)
    pu()
    circle(20,30)
    pd()
end_fill()



#centre
teleport(7,0)
seth(90)
color("white")
begin_fill()
circle(7)
end_fill()

ht()
