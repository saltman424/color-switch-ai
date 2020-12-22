from src.game.environment.utils import MotionDimension
from .basic_item import BasicItem

class Ball(BasicItem):
    def __init__(self, color=None, x=None, y=None, radius=10, jump_vel=8):
        super().__init__(x, y if y is not None else MotionDimension(acc=-0.5, min_vel=-6))
        self.color = color
        self.radius = radius
        self.jump_vel = jump_vel

    def jump(self):
        self.y.vel = self.jump_vel