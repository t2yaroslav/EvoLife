
from random import uniform


class food():
    def __init__(self, settings):
        self.x = uniform(settings['border_x_min'], settings['border_x_max'])
        self.y = uniform(settings['border_y_min'], settings['border_y_max'])
        self.energy = 100

    def respawn(self, settings):
        self.x = uniform(settings['border_x_min'], settings['border_x_max'])
        self.y = uniform(settings['border_y_min'], settings['border_y_max'])
        self.energy = 100
