from .motion_dimension import MotionDimension

class Ball():
    def __init__(self, x=MotionDimension(), y=MotionDimension(acc=-0.5, min_vel=-6), radius=10):
        self.x = x
        self.y = y
        self.radius = radius

    def jump(self):
        self.y.vel = 8

    def move(self):
        self.x.tick()
        self.y.tick()