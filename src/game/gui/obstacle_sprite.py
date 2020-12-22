import tkinter as tk
from .sprite import Sprite

class ObstacleSprite(Sprite):
    def __init__(self, canvas, env, obstacle):
        super().__init__(canvas, env)
        self.obstacle = obstacle
        self.tag = 'obstacle' + str(obstacle.id)
        self.draw()

    def calculate_coords(self):
        self.x1 = self.translate_x(self.obstacle.x.pos - self.obstacle.radius)
        self.y1 = self.translate_y(self.obstacle.y.pos + self.obstacle.radius)
        self.x2 = self.translate_x(self.obstacle.x.pos + self.obstacle.radius)
        self.y2 = self.translate_y(self.obstacle.y.pos - self.obstacle.radius)
        self.slices = self.obstacle.get_slices()

    def draw(self):
        self.calculate_coords()
        self.ids = [
            self.canvas.create_arc(self.x1, self.y1, self.x2, self.y2, width=self.obstacle.thickness,
                start=_slice['start'], extent=_slice['extent'], outline=_slice['color'], style=tk.ARC, tags=self.tag)
            for _slice in self.slices
        ]

    def erase(self):
        self.canvas.delete(self.tag)

    def update(self):
        self.erase()
        self.draw()
