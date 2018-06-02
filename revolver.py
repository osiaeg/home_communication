# revolver
# coding: utf-8

import random 
import turtle 
import math 
from colorama import *

def goto_without_draw(x, y):
	turtle.penup()
	turtle.goto(x, y)
	turtle.pendown()

def paint_circle(color,r):
	turtle.fillcolor(color)
	turtle.begin_fill()
	turtle.circle(r)
	turtle.end_fill()

init()

n = int(input('Введиет число: '))
phi = 360 / 7
r = 68
k = random.randint(0,7)

turtle.speed(0)

goto_without_draw(0,0)
turtle.circle(100)
goto_without_draw(0,200)
paint_circle('red', 5)

for i in range(0,8):
 phi_rad = phi * i * math.pi / 180
 goto_without_draw(math.sin(phi_rad)*r, math.cos(phi_rad)*r + 75)
 turtle.circle(25)

for i in range(k,n+k+1):
	goto_without_draw(math.sin(phi * (i-1) * math.pi / 180)*r, math.cos(phi * (i-1) * math.pi / 180)*r + 75)
	paint_circle('white', 25)
	goto_without_draw(math.sin(phi * i * math.pi / 180)*r, math.cos(phi * i * math.pi / 180)*r + 75)
	paint_circle('yellow', 25)

if i % 7 == 0:
	print (Back.RED + 'You are died!')
else:
	print (Back.GREEN + 'You are the winner!')
	
input()