from random import randrange as rnd, choice
from tkinter import *
import math
import time

root = Tk()
fr = Frame(root)
root.geometry('800x600')
canvas = Canvas(root, bg='white')
canvas.pack(fill=BOTH, expand=1)

colors = ['blue', 'green', 'red', 'brown']


class Ball():
    def __init__(self, balls, x=40, y=450):
        self.x = x
        self.y = y
        self.r = 8
        self.color = choice(colors)
        self.points = 3
        self.id = canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r,
                                     fill=self.color)
        self.live = 30
        self.nature = 1
        self.balls = balls

    def paint(self):
        canvas.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)

    def move(self):
        if self.y <= 500:
            self.vy += 0.17
            self.y += self.vy
            self.x += self.vx
            self.vx *= 0.995
            self.v = (self.vx ** 2 + self.vy ** 2) ** 0.5
            self.an = math.atan(self.vy / self.vx)
            self.paint()
        else:
            if self.vx ** 2 + self.vy ** 2 > 10:
                self.vy = -self.vy * 0.6
                self.vx = self.vx * 0.6
                self.y = 500
            if self.live < 0:
                self.kill()
            else:
                self.live -= 1
        if self.x > 780:
            self.vx = - self.vx / 2
            self.x = 779
        if self.live < 0:
            self.kill()

    def hit_test(self, ob):
        if self.live > 0:
            if abs(ob.x - self.x) <= (self.r + ob.r) and abs(ob.y - self.y) <= (self.r + ob.r):
                return True
            else:
                return False

    def ricochet(self, w):
        self.v = (self.vx ** 2 + self.vy ** 2) ** 0.5
        self.an = math.atan(self.vy / self.vx)

        if self.x == w.x:
            self.x += 1

        if w.x - (self.x + self.vx):
            an_rad = math.atan((w.y - (self.y + self.vy)) / (w.x - (self.x + self.vx)))
            an_res = an_rad - (self.an - an_rad)

            vx2 = 0.8 * self.v * math.cos(an_res)
            vy2 = 0.8 * self.v * math.sin(an_res)
            if self.an > 0 and self.vx < 0 and self.vy < 0 or self.an < 0 and self.vx < 0:
                vx2 = -vx2
                vy2 = -vy2
            self.vx = -vx2
            self.vy = -vy2
            self.move()
            self.points += 1

    def kill(self):
        self.live = 0
        self.balls.pop(self.balls.index(self))
        canvas.delete(self.id)


class Gun():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.on = 1
        self.an = 1
        self.points = 0
        self.id = canvas.create_line(20, 450, 50, 420, width=7, smooth=1)
        self.id_points = canvas.create_text(30, 30, text=self.points, font='28')

        self.balls = []
        self.bullet = 0
        self.targets = []
        self.walls = []

    def fire2_start(self, event):
        self.f2_on = 1

    def stop(self):
        self.f2_on = 0
        self.on = 0

    def fire2_end(self, event):
        self.bullet += 1
        new_ball = Ball(self.balls)
        new_ball.r += 5
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an) / 7
        new_ball.vy = self.f2_power * math.sin(self.an) / 7
        if not rnd(12):
            new_ball.surprize = 1
        self.balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 35

    def targeting(self, event=0):
        if event:
            self.an = math.atan((event.y - 450) / (event.x - 20))
        if self.f2_on:
            canvas.itemconfig(self.id, fill='orange')
        else:
            canvas.itemconfig(self.id, fill='black')
        canvas.coords(self.id, 20, 450, 20 + max(self.f2_power, 20) * math.cos(self.an),
                      450 + max(self.f2_power, 20) * math.sin(self.an))

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canvas.itemconfig(self.id, fill='orange')
        else:
            canvas.itemconfig(self.id, fill='black')


class Target():
    def __init__(self, targets):
        self.points = 1
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 500)
        r = self.r = rnd(10, 40)
        self.live = 1
        self.change_color = 0
        color = self.color = 'red'
        self.id = canvas.create_oval(x - r, y - r, x + r, y + r, fill=self.color)
        self.targets = targets

    def hit(self, points=1):
        self.live -= points
        canvas.itemconfig(self.id, fill='orange')
        self.change_color = 10
        if self.live < 1:
            self.kill()

    def kill(self):
        self.targets.pop(self.targets.index(self))
        canvas.delete(self.id)


g1 = Gun()

while 1:
    balls = g1.balls
    targets = g1.targets
    walls = g1.walls
    g1.on = 1
    for z in range(rnd(2, 4)):
        targets += [Target(targets)]
    for z in range(rnd(1, 5)):
        walls += [Target(walls)]
        walls[-1].x = rnd(200, 600)
        walls[-1].y = rnd(100, 400)
        walls[-1].r = rnd(20, 50)
        canvas.itemconfig(walls[-1].id, fill='gray', width=0)
        canvas.coords(walls[-1].id, walls[-1].x - walls[-1].r, walls[-1].y - walls[-1].r, walls[-1].x + walls[-1].r,
                      walls[-1].y + walls[-1].r)
    canvas.bind('<Button-1>', g1.fire2_start)
    canvas.bind('<ButtonRelease-1>', g1.fire2_end)
    canvas.bind('<Motion>', g1.targeting)
    result = canvas.create_text(400, 300, text='', font="28")
    z = 0.03
    while targets or balls:
        for b in balls:
            b.move()
            for w in walls:
                if b.hit_test(w):
                    b.ricochet(w)
            for t in targets:
                if b.hit_test(t):
                    b.kill()
                    t.hit(b.points)
                    g1.points += 1
                    canvas.itemconfig(g1.id_points, text=g1.points)
        if not targets and g1.on:
            canvas.bind('<Button-1>', '')
            canvas.bind('<ButtonRelease-1>', '')
            g1.stop()
            canvas.itemconfig(result, text='Вы уничтожили все цели за ' + str(g1.bullet) + ' выстрелов')
        for t in targets:
            if t.change_color <= 0:
                canvas.itemconfig(t.id, fill=t.color)
            else:
                t.change_color -= 1
        canvas.update()
        t = 0.008 - (len(balls) - 5) * 0.0001
        t = max(t, 0)
        time.sleep(t)
        g1.targeting()
        g1.power_up()
    canvas.update()
    time.sleep(1)
    canvas.delete(result)
