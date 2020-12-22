import tkinter as tk
from .sprite import Sprite

class SwitchSprite(Sprite):
    def __init__(self, canvas, env, switch):
        super().__init__(canvas, env)
        self.switch = switch
        self.tag = 'switch' + str(switch.id)
        self.draw()

    def calculate_coords(self):
        self.x1 = self.translate_x(self.switch.x.pos - self.switch.radius)
        self.y1 = self.translate_y(self.switch.y.pos + self.switch.radius)
        self.x2 = self.translate_x(self.switch.x.pos + self.switch.radius)
        self.y2 = self.translate_y(self.switch.y.pos - self.switch.radius)

    def draw(self):
        self.calculate_coords()
        self.id = self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill='white', tags=self.tag)

    def erase(self):
        self.canvas.delete(self.id)

    def update(self):
        self.erase()
        self.draw()
