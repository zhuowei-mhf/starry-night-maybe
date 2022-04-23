import turtle as t
from random import randint, random
 

def drawstar(points, size, col, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    anale = 180 - (180/ points)
    t.color(col)
    t.begin_fill()
    for i in range(points):
        t.forward(size)
        t.right(anale)
    t.end_fill()

def drawplanet(col, size , x ,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(col)
    t.begin_fill()
    t.circle(size)
    t.end_fill()
    

#main

t.Screen().bgcolor('black')

while True:
    ranpts = randint(2,7) * 2 +1
    ransize = randint(10,90)
    ransize2 = randint(10,30)
    rancol=(random(),random(), random())
    rancol2=(random(),random(), random())
    ranx = randint(-350, 300)
    ranx2 = randint(-350, 300)
    rany = randint(-250, 250)
    rany2 = randint(-250, 250)
    t.speed('fastest')

    drawstar(ranpts,ransize,rancol,ranx,rany)
    drawplanet(rancol2, ransize2, ranx2, rany2)
