import numpy as np
from math import cos
from math import radians
from math import sin
from random import uniform


class unit():
    def __init__(self, settings, wih=None, who=None, name=None):

        self.x = uniform(settings['x_min'], settings['x_max'])  # position (x)
        self.y = uniform(settings['y_min'], settings['y_max'])  # position (y)

        self.r = uniform(0, 360)  # orientation   [0, 360]
        self.v = uniform(0, settings['v_max'])  # velocity      [0, v_max]
        self.dv = uniform(-settings['dv_max'], settings['dv_max'])  # dv

        self.d_food = 100  # distance to nearest food
        self.r_food = 0  # orientation to nearest food
        self.fitness = 0  # fitness (food Count)

        self.wih = wih
        self.who = who

        self.name = name

    # Neural network
    def think(self):

        # Simple MLP
        af = lambda x: np.tanh(x)  # activation function
        h1 = af(np.dot(self.wih, self.r_food))  # hidden layer
        out = af(np.dot(self.who, h1))  # output layer

        # Update dv and dr with MLP response
        self.nn_dv = float(out[0])  # [-1, 1]  (accelerate=1, deaccelerate=-1)
        self.nn_dr = float(out[1])  # [-1, 1]  (left=1, right=-1)

    # Update heading
    def update_r(self, settings):
        self.r += self.nn_dr * settings['dr_max'] * settings['dt']
        self.r = self.r % 360

    # Update velocity
    def update_vel(self, settings):
        self.v += self.nn_dv * settings['dv_max'] * settings['dt']
        if self.v < 0: self.v = 0
        if self.v > settings['v_max']: self.v = settings['v_max']

    # Update position
    def update_pos(self, settings):
        dx = self.v * cos(radians(self.r)) * settings['dt']
        dy = self.v * sin(radians(self.r)) * settings['dt']
        self.x += dx
        self.y += dy
