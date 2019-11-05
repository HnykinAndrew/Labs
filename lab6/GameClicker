from tkinter import *
from random import randrange as rnd, choice
import time
import math as m

root = Tk()
root.geometry('800x600')
canv = Canvas(root, background="white")
canv.pack(fill=BOTH, expand=1)

colors = ['red', 'orange', 'yellow', 'green', 'blue']

# Balls characteristics
ball_x = list()
ball_y = list()
ball_v_x = list()
ball_v_y = list()
ball_r = list()
ball_color = list()

# lines characteristics
line_x = list()
line_y = list()
line_fi_0 = list()
line_length = list()
line_w_angle = list()
line_v_x = list()
line_v_y = list()
line_width = list()
line_color = list()

# Number of balls, lines
ball_ident = 0
line_ident = 0

# Label score
score = 0
Text = "Score: " + str(score)
label = Label(root, text=Text, font="Arial 14")
label_x = 700
label_y = 550
label.place(x=label_x, y=label_y)


def new_ball():
    # Create ball
    global ball_ident
    x = rnd(100, 700)
    y = rnd(100, 500)
    r = rnd(30, 50)
    k = 0
    if (ball_ident > 11):
        root.after(1000, new_ball)
    else:
        for i in range(0, ball_ident):
            if ((x - ball_x[i])**2 + (y - ball_y[i])**2 <= (r + ball_r[i])**2):
                k = 1
        if (k == 1):
            root.after(0, new_ball)
        else:
            v_x = rnd(-4, 4)
            v_y = rnd(-4, 4)
            color = choice(colors)
            ball_color.append(color)
            ball_x.append(x)
            ball_y.append(y)
            ball_v_x.append(v_x)
            ball_v_y.append(v_y)
            ball_r.append(r)
            ball_ident += 1
            root.after(1000, new_ball)


def new_line():
    # Create line
    global line_ident
    x = rnd(100, 700)
    y = rnd(100, 500)
    fi_0 = rnd(0, 360)
    length = rnd(50, 80)
    w_angle = rnd(-5, 5)
    width = rnd(8, 14)
    v_x = rnd(-4, 4)
    v_y = rnd(-4, 4)
    color = choice(colors)
    if (ball_ident > 15):
        root.after(1000, new_line)
    else:
        line_ident += 1
        line_x.append(x)
        line_y.append(y)
        line_fi_0.append(fi_0)
        line_length.append(length)
        line_w_angle.append(w_angle)
        line_width.append(width)
        line_v_x.append(v_x)
        line_v_y.append(v_y)
        line_color.append(color)
        root.after(1000, new_line)


def move():
    # Move balls and lines
    global ball_ident, line_ident
    canv.delete(ALL)
    for i in range(0, ball_ident):
        canv.create_oval(ball_x[i] - ball_r[i] + ball_v_x[i], ball_y[i] - ball_r[i] + ball_v_y[i],
                         ball_x[i] + ball_r[i] + ball_v_x[i], ball_y[i] + ball_r[i] + ball_v_y[i],
                         fill=ball_color[i], width=0)
        ball_x[i] += ball_v_x[i]
        ball_y[i] += ball_v_y[i]
        if (ball_x[i] - ball_r[i] < 0):
            ball_v_x[i] = rnd(1, 5)
        if (ball_x[i] + ball_r[i] > 800):
            ball_v_x[i] = rnd(-5, -1)
        if (ball_y[i] - ball_r[i] < 0):
            ball_v_y[i] = rnd(1, 5)
        if (ball_y[i] + ball_r[i] > 600):
            ball_v_y[i] = rnd(-5, -1)
        for j in range(i + 1, ball_ident):
            if ((ball_x[j] - ball_x[i])**2 + (ball_y[j] - ball_y[i])
                    ** 2 <= (ball_r[i] + ball_r[j])**2):
                swap = ball_v_x[i]
                ball_v_x[i] = ball_v_x[j]
                ball_v_x[j] = swap
                swap = ball_v_y[i]
                ball_v_y[i] = ball_v_y[j]
                ball_v_y[j] = swap
    for i in range(0, line_ident):
        canv.create_line(line_x[i] - (line_length[i] / 2 * m.cos(line_fi_0[i] * 2 * m.pi / 360)),
                         line_y[i] - (line_length[i] / 2 * m.sin(line_fi_0[i] * 2 * m.pi / 360)),
                         line_x[i] + (line_length[i] / 2 * m.cos(line_fi_0[i] * 2 * m.pi / 360)),
                         line_y[i] + (line_length[i] / 2 * m.sin(line_fi_0[i] * 2 * m.pi / 360)),
                         width=line_width[i], fill=line_color[i])
        line_x[i] += line_v_x[i]
        line_y[i] += line_v_y[i]
        line_fi_0[i] += line_w_angle[i]
        if (line_x[i] - (line_length[i] / 2 * m.cos(line_fi_0[i] * 2 * m.pi / 360)) < 0
                or line_x[i] + (line_length[i] / 2 * m.cos(line_fi_0[i] * 2 * m.pi / 360)) < 0):
            line_v_x[i] = rnd(1, 5)
        if (line_x[i] - (line_length[i] / 2 * m.cos(line_fi_0[i] * 2 * m.pi / 360)) > 800
                or line_x[i] + (line_length[i] / 2 * m.cos(line_fi_0[i] * 2 * m.pi / 360)) > 800):
            line_v_x[i] = rnd(-5, -1)
        if (line_y[i] - (line_length[i] / 2 * m.sin(line_fi_0[i] * 2 * m.pi / 360)) < 0
                or line_y[i] + (line_length[i] / 2 * m.sin(line_fi_0[i] * 2 * m.pi / 360)) < 0):
            line_v_y[i] = rnd(1, 5)
        if (line_y[i] - (line_length[i] / 2 * m.sin(line_fi_0[i] * 2 * m.pi / 360)) > 600
                or line_y[i] + (line_length[i] / 2 * m.sin(line_fi_0[i] * 2 * m.pi / 360)) > 600):
            line_v_y[i] = rnd(-5, -1)
    root.after(10, move)


def click(event):
    # Check clicks
    global score, ball_ident, line_ident, colors, label
    hit = 0
    for i in range(0, ball_ident):
        if ((event.x - ball_x[i])**2 + (event.y - ball_y[i])**2 < ball_r[i]**2):
            hit = 1
            if (ball_color[i] != "red"):
                ball_color[i] = colors[colors.index(ball_color[i]) - 1]
            else:
                score += 10
                del ball_x[i]
                del ball_y[i]
                del ball_r[i]
                del ball_v_x[i]
                del ball_v_y[i]
                del ball_color[i]
                ball_ident = ball_ident-1
                i = i - 1
                break
    if hit == 0:
        score -= 20
    label['text'] = "Score: " + str(score)


def quit(pressed_button):
    # Close program
    global score
    score += 1000
    new_ball()
    results = list()
    with open("Results.txt", "r") as file_data:
        for line in file_data:
            results.append(line.split())
        file_data.close()
    for i in range(0, len(results)-2, 1):
        swap = results[i]
        for j in range(i+1, len(results)-2, 1):
            if results[j][1] < swap[1]:
                swap = results[j]
                results[j] = results[i]
                results[i] = swap
    with open('Results.txt', 'w') as file_data:
        for i in (0, len(results)-1, 1):
            file_data.write(str(results[i][0]) + ' ' + str(results[i][1]) + '\n')
        file_data.close()
    exit(0)


new_ball()
new_line()
move()

canv.bind('<Button-1>', click)
canv.bind("<Escape>", quit)
canv.focus_set()

root.mainloop()
