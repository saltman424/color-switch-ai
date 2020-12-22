import random as rand

class Palette():
    def __init__(self, colors=[ 'red', 'green', 'cyan', 'purple' ]):
        self.colors = colors

    def get_random_color(self, exclude=[]):
        return self.get_random_colors(quantity=1, exclude=exclude)[0]

    def get_random_colors(self, quantity=None, exclude=[]):
        population = [ color for color in self.colors if color not in exclude ]
        return rand.sample(
            population,
            quantity if quantity is not None else len(population)
        )
