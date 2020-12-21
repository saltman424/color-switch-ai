import tkinter as tk
from .ball import Ball

class Frame(tk.Frame):
    def __init__(self, master, env):
        super().__init__(master)
        self.env = env
        self.pack()

        # Canvas
        self.canvas = tk.Canvas(self, width=self.env.width, height=self.env.height, bg='black')
        self.canvas.pack()

        # Sprites
        self.ball = Ball(self.canvas, env)

    def update(self):
        self.ball.update()
