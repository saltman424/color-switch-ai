import tkinter as tk
from .ball_sprite import BallSprite
from .obstacle_sprite import ObstacleSprite
from .switch_sprite import SwitchSprite

class Frame(tk.Frame):
    def __init__(self, master, env):
        super().__init__(master)
        self.env = env
        self.pack()
        # Canvas
        self.canvas = tk.Canvas(self, width=self.env.width, height=self.env.height, bg='black')
        self.canvas.pack()
        # Sprites
        self.ball_sprite = BallSprite(self.canvas, env, env.ball)
        self.obstacle_sprites = {}
        self.switch_sprites = {}

    def update(self):
        # Ball
        self.ball_sprite.update()
        # Obstacles
        self.update_sprite_dict(ObstacleSprite, self.obstacle_sprites, self.env.obstacles)
        # Switches
        old_switch_keys = set(self.switch_sprites.keys())
        for switch in self.env.switches:
            if switch.id in old_switch_keys:
                old_switch_keys.remove(switch.id)
            if switch.id not in self.switch_sprites:
                self.switch_sprites[switch.id] = SwitchSprite(self.canvas, self.env, switch)
            self.switch_sprites[switch.id].update()
        for k in old_switch_keys:
            self.switch_sprites[k].erase()
            del self.switch_sprites[k]

    def update_sprite_dict(self, sprite_constructor, sprite_dict, item_list):
        old_keys = set(sprite_dict.keys())
        for item in item_list:
            if item.id in old_keys:
                old_keys.remove(item.id)
            if item.id not in sprite_dict:
                sprite_dict[item.id] = sprite_constructor(self.canvas, self.env, item)
            sprite_dict[item.id].update()
        for k in old_keys:
            sprite_dict[k].erase()
            del sprite_dict[k]
        

