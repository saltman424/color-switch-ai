from src.game.environment.utils import MotionDimension
from .basic_item import BasicItem

class Ball(BasicItem):
    def __init__(self, color=None, x=MotionDimension(), y=MotionDimension(acc=-0.5, min_vel=-6), radius=10):
        super().__init__(x, y)
        self.color = color
        self.radius = radius

    def jump(self):
        self.y.vel = 8