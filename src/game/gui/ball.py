import tkinter as tk
from .sprite import Sprite

class Ball(Sprite):
    def __init__(self, canvas, env):
        super().__init__(canvas, env)
        self.tag = 'ball'
        self.draw()

    def set_old_coords(self):
        self.old_x1 = self.x1
        self.old_y1 = self.y1
        self.old_x2 = self.x2
        self.old_y2 = self.y2

    def get_new_coords(self):
        ball = self.env.ball
        self.x1 = self.translate_x(ball.x.pos - ball.radius)
        self.y1 = self.translate_y(ball.y.pos + ball.radius)
        self.x2 = self.translate_x(ball.x.pos + ball.radius)
        self.y2 = self.translate_y(ball.y.pos - ball.radius)

    def update_coords(self):
        self.set_old_coords()
        self.get_new_coords()

    def draw(self):
        self.get_new_coords()
        self.oval = self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill='red', tags=self.tag)

    def erase(self):
        self.canvas.delete(self.tag)

    def update(self):
        self.update_coords()
        x_change = self.x1 - self.old_x1
        y_change = self.y1 - self.old_y1
        self.canvas.move(self.oval, x_change, y_change)
