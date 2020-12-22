from src.game.environment.utils import MotionDimension
from .basic_item import BasicItem

class RotatingItem(BasicItem):
    def __init__(self, x=None, y=None, deg=None):
        super().__init__(x, y)
        self.deg = deg if deg is not None else MotionDimension()

    def move(self):
        super().move()
        self.deg.tick()
        while self.deg.pos >= 360:
            self.deg.pos -= 360
        while self.deg.pos < 0:
            self.deg.pos += 360
