import random as rand
from .items import *
from .utils import *

class ColorSwitchEnvironment():
    def __init__(self, width=300, height=500, palette=Palette(), ball=Ball()):
        # Sizing
        self.width = width
        self.height = height
        self.top_edge = height // 2
        self.bottom_edge = self.top_edge - height
        self.right_edge = width // 2
        self.left_edge = self.right_edge - self.width
        # State
        self.paused = True
        # Items
        self.palette = palette
        self.ball = ball
        if self.ball.color is None:
            self.ball.color = self.palette.get_random_color()
        self.ticks_til_next_switch = self.get_random_number_of_ticks()
        self.switches = []

    def start(self):
        self.paused = True
        self.ball.color = self.palette.get_random_color()
        self.ball.x.pos = 0
        self.ball.x.vel = 0
        self.ball.y.pos = 0
        self.ball.y.vel = 0

    def restart(self):
        self.start()

    def tick(self):
        if not self.paused:
            self.ball.move()
            for switch in self.switches:
                switch.move()
            if self.collision_detected():
                self.restart()
                return
            self.check_ticks()
            self.decrement_ticks()
            self.cleanup_passed_items()

    def get_random_number_of_ticks(self, min_ticks=20, max_ticks=200):
        return rand.randint(min_ticks, max_ticks)

    def check_ticks(self):
        if self.ticks_til_next_switch == 0:
            self.add_switch()
            self.ticks_til_next_switch = self.get_random_number_of_ticks()

    def decrement_ticks(self):
        self.ticks_til_next_switch -= 1

    def add_switch(self):
        print('Adding switch...')
        self.switches.append(Switch(self.palette))

    def is_off_screen(self, item):
        return (
            item.x.pos >= self.right_edge or
            item.x.pos <= self.left_edge or
            item.y.pos >= self.top_edge or
            item.y.pos <= self.bottom_edge
        )

    def collision_detected(self):
        return self.is_off_screen(self.ball)

    def cleanup_passed_items(self):
        if len(self.switches) >= 1 and self.is_off_screen(self.switches[0]):
            print('Deleting switch...')
            del self.switches[0]

    def on_user_input(self):
        self.ball.jump()
        self.paused = False