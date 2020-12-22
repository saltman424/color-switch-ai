from src.game.environment.utils import MotionDimension
from .basic_item import BasicItem

class RotatingItem(BasicItem):
    def __init__(self, x=MotionDimension(), y=MotionDimension(), r=MotionDimension()):
        super().__init__(x, y)
        self.r = r

    def move(self):
        super().move()
        self.r.tick()