import tkinter as tk
from .sprite import Sprite

class Ball(Sprite):
    def __init__(self, canvas, env):
        super().__init__(canvas, env)
        self.tag = 'switch'
        self.draw()

    def calculate_coords(self):
        ball = self.env.ball
        self.x1 = self.translate_x(ball.x.pos - ball.radius)
        self.y1 = self.translate_y(ball.y.pos + ball.radius)
        self.x2 = self.translate_x(ball.x.pos + ball.radius)
        self.y2 = self.translate_y(ball.y.pos - ball.radius)

    def draw(self):
        self.calculate_coords()
        self.id = self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill=self.env.ball.color, tags=self.tag)

    def erase(self):
        self.canvas.delete(self.id)

    def update(self):
        self.erase()
        self.draw()
