import random as rand
from .items import *
from .utils import *

class ColorSwitchEnvironment():
    def __init__(self, width=300, height=500, scroll_speed=-0.75, palette=Palette(), ball=Ball()):
        # Sizing
        self.width = width
        self.height = height
        self.top_edge = height // 2
        self.bottom_edge = self.top_edge - height
        self.right_edge = width // 2
        self.left_edge = self.right_edge - self.width
        self.scroll_speed = scroll_speed
        # State
        self.paused = True
        # Items
        self.palette = palette
        self.ball = ball
        self.start()

    def start(self):
        self.paused = True
        self.ball.color = self.palette.get_random_color()
        self.ball.x.pos = 0
        self.ball.x.vel = 0
        self.ball.y.pos = 0
        self.ball.y.vel = 0
        self.switches = []
        self.ticks_til_next_obstacle = self.get_random_number_of_ticks()
        self.obstacles = []
        self.ticks_til_next_switch = self.ticks_til_next_obstacle + self.get_random_number_of_ticks()
        self.switches = []

    def restart(self):
        self.start()

    def pause(self):
        self.paused = True

    def resume(self):
        self.paused = False

    def toggle_pause(self):
        self.paused = not self.paused

    def tick(self):
        if not self.paused:
            self.ball.move()
            for switch in self.switches:
                switch.move()
            for obstacle in self.obstacles:
                obstacle.move()
            if self.fatal_collision_detected():
                self.restart()
                return
            self.check_for_switch_collision()
            self.check_tick_trackers()
            self.decrement_tick_trackers()
            self.cleanup_passed_items()

    def get_random_number_of_ticks(self, min_ticks=50, max_ticks=250):
        return rand.randint(min_ticks, max_ticks)

    def check_tick_trackers(self):
        if self.ticks_til_next_obstacle == 0:
            self.add_obstacle()
            self.ticks_til_next_obstacle = self.get_random_number_of_ticks()
        if self.ticks_til_next_switch == 0:
            self.add_switch()
            self.ticks_til_next_switch = self.ticks_til_next_obstacle + self.get_random_number_of_ticks()

    def decrement_tick_trackers(self):
        self.ticks_til_next_obstacle -= 1
        self.ticks_til_next_switch -= 1

    def add_obstacle(self):
        self.obstacles.append(Obstacle(self.palette, y=MotionDimension(pos=self.top_edge, vel=self.scroll_speed),
            deg=MotionDimension(vel=-1.5)))

    def add_switch(self):
        self.switches.append(Switch(self.palette, y=MotionDimension(pos=self.top_edge, vel=self.scroll_speed)))

    def is_off_screen(self, item):
        return (
            item.x.pos > self.right_edge or
            item.x.pos < self.left_edge or
            item.y.pos > self.top_edge or
            item.y.pos < self.bottom_edge
        )

    def check_for_switch_collision(self):
        for i, switch in enumerate(self.switches):
            if switch.has_collided_with(self.ball):
                switch.apply_to(self.ball)
                del self.switches[i]

    def fatal_collision_detected(self):
        if self.is_off_screen(self.ball):
            return True
        for obstacle in self.obstacles:
            if obstacle.has_collided_with(self.ball):
                return True
        return False

    def cleanup_passed_items(self):
        if len(self.switches) >= 1 and self.is_off_screen(self.switches[0]):
            del self.switches[0]

    def on_user_input(self):
        self.ball.jump()
        self.paused = False