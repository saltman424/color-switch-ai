import tkinter as tk
from .ball import Ball
from .switch import Switch

class Frame(tk.Frame):
    def __init__(self, master, env):
        super().__init__(master)
        self.env = env
        self.pack()
        # Canvas
        self.canvas = tk.Canvas(self, width=self.env.width, height=self.env.height, bg='black')
        self.canvas.pack()
        # Sprites
        self.ball_sprite = Ball(self.canvas, env, env.ball)
        self.switch_sprites = {}

    def update(self):
        # Ball
        self.ball_sprite.update()
        # Switches
        old_switch_keys = set(self.switch_sprites.keys())
        for switch in self.env.switches:
            if switch.id in old_switch_keys:
                old_switch_keys.remove(switch.id)
            if switch.id not in self.switch_sprites:
                self.switch_sprites[switch.id] = Switch(self.canvas, self.env, switch)
            self.switch_sprites[switch.id].update()
        for k in old_switch_keys:
            self.switch_sprites[k].erase()
            del self.switch_sprites[k]
        

