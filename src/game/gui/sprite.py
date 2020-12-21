class Sprite():
    def __init__(self, canvas, env):
        self.canvas = canvas
        self.env = env

    def translate_x(self, x):
        return -self.env.left_edge + x

    def translate_y(self, y):
        return self.env.top_edge - y

    def draw(self):
        raise NotImplementedError()

    def erase(self):
        raise NotImplementedError()

    def update(self):
        raise NotImplementedError()
