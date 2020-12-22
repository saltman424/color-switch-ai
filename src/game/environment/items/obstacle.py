import math
from src.game.environment.utils import MotionDimension
from .rotating_item import RotatingItem

class Obstacle(RotatingItem):
    def __init__(self, palette, x=None, y=None, deg=None, radius=80, thickness=10):
        super().__init__(x, y, deg)
        self.palette = palette
        self.colors = palette.get_random_colors()
        self.radius = radius
        self.thickness = thickness

    def get_slices(self):
        slices = []
        curr_degree = self.deg.pos
        for color in self.colors:
            extent = 360 / len(self.colors)
            slices.append({
                'color': color,
                'start': curr_degree,
                'extent': extent
            })
            curr_degree += extent
            if curr_degree >= 360:
                curr_degree -= 360
        return slices

    def has_collided_with(self, ball):
        x_diff = abs(self.x.pos - ball.x.pos)
        y_diff = abs(self.y.pos - ball.y.pos)
        dist = (x_diff ** 2 + y_diff ** 2) ** (1/2) - ball.radius
        outter_threshold = self.radius - 1 # Buffer
        inner_threshold = self.radius - self.thickness + 1 # Buffer
        if dist < outter_threshold and dist > inner_threshold:
            angle = 90 if x_diff == 0 else math.degrees(math.atan(y_diff / x_diff))
            if self.y.pos < ball.y.pos != self.x.pos < ball.x.pos:
                angle = 180 - angle # Quadrants II and IV use supplementary angles
            if self.y.pos > ball.y.pos:
                angle += 180 # Quadrants III an IV have an additional 180deg
            for _slice in self.get_slices():
                if _slice['color'] != ball.color:
                    angle_max_threshold = _slice['start'] + _slice['extent']
                    angle_min_threshold = _slice['start']
                    comparison_angle = angle + 360 if angle_max_threshold >= 360 else angle
                    if comparison_angle < angle_max_threshold and comparison_angle > angle_min_threshold:
                        return True
        return False
