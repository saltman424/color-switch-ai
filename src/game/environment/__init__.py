from .ball import Ball
from .motion_dimension import MotionDimension

class ColorSwitchEnvironment():
    def __init__(self, width=300, height=500, ball=Ball()):
        self.width = width
        self.height = height
        self.top_edge = height // 2
        self.bottom_edge = self.top_edge - height
        self.right_edge = width // 2
        self.left_edge = self.right_edge - self.width
        self.ball = ball
        self.paused = True

    def start(self):
        self.paused = True
        self.ball.x.pos = 0
        self.ball.x.vel = 0
        self.ball.y.pos = 0
        self.ball.y.vel = 0

    def restart(self):
        self.start()

    def tick(self):
        if not self.paused:
            self.ball.move()
            if self.collision_detected():
                self.restart()

    def collision_detected(self):
        return (
            self.ball.x.pos >= self.right_edge or
            self.ball.x.pos <= self.left_edge or
            self.ball.y.pos >= self.top_edge or
            self.ball.y.pos <= self.bottom_edge
        )

    def on_user_input(self):
        self.ball.jump()
        self.paused = False