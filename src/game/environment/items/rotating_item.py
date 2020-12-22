from src.game.environment.utils import MotionDimension
from .basic_item import BasicItem

class RotatingItem(BasicItem):
    def __init__(self, x=None, y=None, r=None):
        super().__init__(x, y)
        self.r = r if r is not None else MotionDimension()

    def move(self):
        super().move()
        self.r.tick()