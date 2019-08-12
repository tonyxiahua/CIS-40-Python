import turtle
import math
import time

def draw(times, n, length):
    angle = 360.0 / n
    drawline(times, n, length, angle)

def drawline(times, n, length, angle):
    for i in range(n): 
        times.fd(length)
        times.lt(angle)
    
turtle.bgcolor('black')
colors = ['green','yellow','red','purple','blue','orange']

echo = turtle.Turtle()
echo.speed(100000)
sLen = 1
echo.pensize(1)

for i in range(0,720):
    echo.pencolor(colors[i%6])
    draw(echo, 1, sLen)
    echo.forward(i)
    echo.left(59)
    sLen+=1
