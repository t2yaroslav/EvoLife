# ---------------------------------------------------------------------------------
#   Yaroslav Krivolapov
#
#   The evolution test  (neural net)
#   2020 Oct.
#
# ---------------------------------------------------------------------------------
import numpy as np
from engine import simulate, evolve
from food import food
from unit import unit

settings = {
    # Evolution
    'pop_size': 200,  # number of organisms
    'food_num': 3,  # number of food particles
    'gens': 50,  # number of generations
    'elitism': 0.20,  # elitism (selection bias)
    'mutate': 0.10,  # mutation rate

    # Simulation
    'gen_time': 100,  # generation length         (seconds)
    'dt': 0.04,  # simulation time step      (dt)
    'dr_max': 720,  # max rotational speed      (degrees per second)
    'v_max': 0.5,  # max velocity              (units per second)
    'dv_max': 0.25,  # max acceleration (+/-)    (units per second^2)

    'x_min': -2.0,  # arena western border
    'x_max': 2.0,  # arena eastern border
    'y_min': -2.0,  # arena southern border
    'y_max': 2.0,  # arena northern border

    'plot': True,  # plot final generation?

    # Neural Net
    'inodes': 1,  # number of input nodes
    'hnodes': 5,  # number of hidden nodes
    'onodes': 2  # number of output nodes
}


def run(settings):

    # Food
    foods = []
    for i in range(0, settings['food_num']):
        foods.append(food(settings))

    # Unit
    units = []
    for i in range(0, settings['pop_size']):
        wih_init = np.random.uniform(-1, 1, (settings['hnodes'], settings['inodes']))  # mlp weights (input -> hidden)
        who_init = np.random.uniform(-1, 1, (settings['onodes'], settings['hnodes']))  # mlp weights (hidden -> output)

        units.append(unit(settings, wih_init, who_init, name='gen[x]-org[' + str(i) + ']'))

    # Main cycle
    for gen in range(0, settings['gens']):

        # Simulate
        units = simulate(settings, units, foods, gen)

        # Evolute
        units, stats = evolve(settings, units, gen)
        print('> GEN:', gen, 'Best:', stats['Best'], 'AVG:', stats['AVG'], 'Worst:', stats['Worst'])

    pass


run(settings)
