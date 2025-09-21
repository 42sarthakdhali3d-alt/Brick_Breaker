import tkinter as tk
import random
class Ball:
    def __init__(self, canvas, paddle):
        self.canvas = canvas
        self.paddle = paddle
        self.life = 3
        self.id = canvas.create_oval(325, 525, 350, 550, fill="white")
        self.canvas.move(self.id, 245, 100) # starting position
        starts = [-3.5, -3, -2, -1.8, 1.8, 2, 3, 3.5]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -7
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
        self.lives = True
    def hit_paddley(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        #
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
            return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
    # bounce left/right
        if pos[0] <= 0 or pos[2] >= self.canvas_width:
            self.x = -self.x
    # bounce top
        if pos[1] <= 0:
            self.y = -self.y
    # check bottom (game over if ball misses paddle)
        if pos[3] >= self.canvas_height:
            self.canvas.move(self.id, 0, -300)

            self.life -= 1
            if self.life < 1:
                self.canvas.move(self.id, -50000, -300000)
    # bounce off paddle
        if self.hit_paddley(pos):
            self.y = -self.y

