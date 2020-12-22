import tkinter as tk
import time
from .frame import Frame

class ColorSwitchGui():
    UPDATE_FREQUENCY = 0.01

    def __init__(self, env):
        self.env = env
        self.root = tk.Tk()
        self.root.title('Color Switch')
        self.root.bind('<space>', lambda e: env.on_user_input())
        self.root.bind('<p>', lambda e: env.toggle_pause())
        self.frame = Frame(self.root, env)

    def is_open(self):
        try:
            return self.root.winfo_exists() == 1
        except:
            return False

    def run(self):
        self.env.start()
        self.root.update()
        while self.is_open():
            self.env.tick()
            self.frame.update()
            self.root.update()
            time.sleep(ColorSwitchGui.UPDATE_FREQUENCY)
    