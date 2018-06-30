'''
Choose which of the two programs below you'd like to implement for this final lab:

Use the turtle module which we learned about back in Chapter 4 to create a screensaver-like program of your own design; OR....
Write a hang-cheat program which takes as its input a string of underscores and letters, along with a list of wrong letters that have already been guessed, and then outputs all the words in words.txtPreview the document that could be the unknown word. It should terminate after just one input/output, which means the person using this program would have to start it up again after they had played another turn at hang-python or whatever version of the word-game they were playing.
'''


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
