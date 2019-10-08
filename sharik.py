from tkinter import *
from random import randrange as rnd, choice
import time

root = Tk()
root.geometry('800x600')
canv = Canvas(root, background="white")
canv.pack(fill=BOTH, expand=1)

colors = ['red','orange','yellow','green','blue']

ball = list()
ball_x = list()
ball_y = list()
ball_v_x = list()
ball_v_y = list()
ball_r = list()
ball_color = list()

ball_ident = 0 
score = 0


def new_ball():
	global x,y,r,ball_ident
	canv.delete(ALL)
	x = rnd(100,700)
	y = rnd(100,500)
	r = rnd(30,50)
	v_x = rnd(-5,5)
	v_y = rnd(-5,5)
	color = choice(colors)
	ball_color.append(color)
	obj_ball = canv.create_oval(x-r,y-r,x+r,y+r,fill = color, width=0)
	ball.append(obj_ball)
	ball_x.append(x)
	ball_y.append(y)
	ball_v_x.append(v_x)
	ball_v_y.append(v_y)
	ball_r.append(r)
	ball_ident += 1
	root.after(1000,new_ball)

def move():
	global ball_ident
	canv.delete(ALL)
	for i in range(0,ball_ident):
		canv.create_oval(ball_x[i]-ball_r[i]+ball_v_x[i],ball_y[i]-ball_r[i]+ball_v_y[i],ball_x[i]+ball_r[i]+ball_v_x[i],ball_y[i]+ball_r[i]+ball_v_y[i],fill = ball_color[i], width=0)
		ball_x[i] += ball_v_x[i]
		ball_y[i] += ball_v_y[i]
		if (ball_x[i]-ball_r[i]<0):
			ball_v_x[i] = rnd(1,5)
		if (ball_x[i]+ball_r[i]>800):
			ball_v_x[i] = rnd(-5,-1)
		if (ball_y[i]-ball_r[i]<0):
			ball_v_y[i] = rnd(1,5)
		if (ball_y[i]+ball_r[i]>600):
			ball_v_y[i] = rnd(-5,-1)
		for j in range(i+1,ball_ident):
			if ((ball_x[j]-ball_x[i])**2 + (ball_y[j]-ball_y[i])**2 <= (ball_r[i]+ball_r[j])**2):
				ball_v_x[i] = -ball_v_x[i]
				ball_v_y[i] = -ball_v_y[i]
				ball_v_x[j] = -ball_v_x[j]
				ball_v_y[j] = -ball_v_y[j]
	root.after(1,move)

def click(event):
	global score, ball_ident
	for i in range(0,ball_ident):
		if ((event.x-ball_x[i])**2 + (event.y-ball_y[i])**2 < ball_r[i]**2):
			score += 10
			del ball_x[i]
			del ball_y[i]
			del ball_r[i]
			del ball_v_x[i]
			del ball_v_y[i]
			del ball_color[i]
			ball_ident = ball_ident-1
			i=i-1
			break
	print(score)

new_ball()
move()
canv.bind('<Button-1>', click)


root.mainloop()


