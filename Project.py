from tkinter import *
from PIL import Image, ImageTk
import time
import random

# создаём новый объект — окно с игровым полем.
tk = Tk()
tk.title('Game')
# запрещаем менять размеры окна, для этого используем свойство resizable
tk.resizable(0, 0)
# помещаем наше игровое окно выше остальных окон на компьютере, чтобы другие окна не могли его заслонить.
tk.wm_attributes('-topmost', 1)

# Globals
WIDTH = 1200
HEIGHT = 800

# создаём новый холст — 400 на 500 пикселей, где и будем рисовать игру
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
# говорим холсту, что у каждого видимого элемента будут свои отдельные координаты
canvas.pack()
# обновляем окно с холстом
tk.update()


class MapCanvas(object):

    def __init__(self, file_name):
        self.pilImage = Image.open(file_name)
        self.width = self.pilImage.size[0]
        self.height = self.pilImage.size[1]
        self.image = ImageTk.PhotoImage(self.pilImage)
        self.imagesprite = canvas.create_image((-self.width+WIDTH)/2, (-self.height+HEIGHT)/2,
                                               image=self.image, anchor="nw")
        print(self.width, self.height)


class Stickman(object):

    def __init__(self, number_of_sprites, sprites, coord_x, coord_y):




x = MapCanvas("Game.jpg")
tk.mainloop()
