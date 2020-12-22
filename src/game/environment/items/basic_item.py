from src.game.environment.utils import MotionDimension

class BasicItem():
    def __init__(self, x=MotionDimension(), y=MotionDimension()):
        self.x = x
        self.y = y

    def move(self):
        self.x.tick()
        self.y.tick()