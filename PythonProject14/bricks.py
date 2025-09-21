import tkinter as tk
class Brick:
    def __init__(self, canvas, x, y, fill = None):
        self.canvas = canvas
        self.canvas_width = self.canvas.winfo_width()
        self.id = canvas.create_rectangle(x, y, x + 135, y + 25, fill = fill)