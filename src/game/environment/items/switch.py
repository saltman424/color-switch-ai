from src.game.environment.utils import MotionDimension
from .basic_item import BasicItem

class Switch(BasicItem):
    def __init__(self, palette, x=None, y=None, radius=6):
        super().__init__(x, y)
        self.palette = palette
        self.radius = radius

    def has_collided_with(self, ball):
        x_diff = abs(self.x.pos - ball.x.pos)
        y_diff = abs(self.y.pos - ball.y.pos)
        diff_threshold = max(self.radius, ball.radius) / 2
        return x_diff <= diff_threshold and y_diff <= diff_threshold

    def apply_to(self, ball):
        new_color = self.palette.get_random_color(exclude=[ ball.color ])
        ball.color = new_color
