from tkinter import *
from random import randint
from ball import Ball
from bricks import Brick

class Pad:
    def __init__(self, canvas):
        self.canvas = canvas
        self.canvas_width = self.canvas.winfo_width()
        self.id = canvas.create_rectangle(555, 660, 735, 680, fill = "lightGreen")
        self.xp = 0
        self.canvas.bind_all("<Key>", self.mpad)
    def draw(self):

        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.xp = 0
        elif pos[2] >= self.canvas_width:
            self.xp = 0
    def mpad(self ,event):
        pos = self.canvas.coords(self.id)
        if event.keysym == "a":
            print("Moving left!")
            if pos[0] <= 0:
                self.xp = 0
            else:
                self.xp = -40
        elif event.keysym == "d":
            print("Moving right!")
            if pos[2] >= self.canvas_width:
                self.xp = 0
            else:
                self.xp = 40
        self.canvas.move(self.id, self.xp, 0)

def create_bricks(canvas):
    bricks = []
    y = 60

    COLOR_HEALTH = {"purple": 4, "red": 3, "orange": 2, "cyan": 1}
    HEALTH_COLOR = {v: k for k, v in COLOR_HEALTH.items()}
    color = ["cyan", "orange", "red", "purple"]

    for row in range(0, 7):
        x = 30
        for c in range(8):
            colo = randint(0, 3)
            brick = Brick(canvas, x, y, fill = color[colo])  # Assuming Brick accepts fill color
            brick.health = COLOR_HEALTH[color[colo]]
            bricks.append(brick)
            x += 155
        y += 45

    return bricks, HEALTH_COLOR

class Master:
    def __init__(self, canvas):
        self.canvas = canvas
        self.canvas_width = self.canvas.winfo_width()
        self.id = canvas.create_rectangle(580, 20, 730, 50, fill="white")
        self.xp = 0

def hit_brick(canvas, ball, bricks, HEALTH_COLOR):
    balc = canvas.coords(ball.id)
    overlapping = canvas.find_overlapping(*balc)

    for brick in bricks:
        if brick.id in overlapping:
            brick.health -= 1
            if brick.health > 0:
                brick.canvas.itemconfig(brick.id, fill = HEALTH_COLOR[brick.health])
            else:
                canvas.delete(brick.id)
                bricks.remove(brick)

            ball.y = -ball.y
            break  # only handle one collision per frame

window = Tk()
window.title("Break_Breaker")
canvas = Canvas(window, width = 1280, height = 700, bg = "black")
canvas.pack()

window.update()
pad = Pad(canvas)
ball = Ball(canvas, pad)
master = Master(canvas)
bricks, HEALTH_COLOR = create_bricks(canvas)
life = 3

while not ball.hit_bottom:

    pad.draw()
    ball.draw()
    hit_brick(canvas, ball, bricks, HEALTH_COLOR)
    window.update_idletasks()
    window.update()
    window.after(2)

window.mainloop()