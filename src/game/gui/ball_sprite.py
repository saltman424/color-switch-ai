import tkinter as tk
from .sprite import Sprite

class BallSprite(Sprite):
    def __init__(self, canvas, env, ball):
        super().__init__(canvas, env)
        self.ball = ball
        self.tag = 'ball' + str(ball.id)
        self.draw()

    def calculate_coords(self):
        self.x1 = self.translate_x(self.ball.x.pos - self.ball.radius)
        self.y1 = self.translate_y(self.ball.y.pos + self.ball.radius)
        self.x2 = self.translate_x(self.ball.x.pos + self.ball.radius)
        self.y2 = self.translate_y(self.ball.y.pos - self.ball.radius)

    def draw(self):
        self.calculate_coords()
        self.id = self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill=self.ball.color, tags=self.tag)

    def erase(self):
        self.canvas.delete(self.id)

    def update(self):
        self.erase()
        self.draw()
