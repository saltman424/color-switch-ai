from src.game.environment.utils import MotionDimension

class BasicItem():
    id = 1

    def __init__(self, x=None, y=None):
        self.x = x if x is not None else MotionDimension()
        self.y = y if y is not None else MotionDimension()
        self.id = BasicItem.id
        BasicItem.id += 1

    def __eq__(self, other):
        return self.id == other.id

    def move(self):
        self.x.tick()
        self.y.tick()