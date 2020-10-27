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
    'units_count': 200,  # number of units
    'food_num': 10,  # number of food particles
    'gens': 50,  # number of generations
    'survivors_count': 0.40,  # selection bias
    'mutate': 0.10,  # mutation rate

    'eating_speed': 0.1,  # eating speedустойчивый
    'eating_speed_max': 0.01,    # stop for eat
    'energy_digress': 0.0001,  # energy digress (permanent)
    'energy_waste': 0.000001,  # energy waste (depends on velocity)

    # Simulation
    'gen_time': 200,  # generation length         (seconds)
    'time_step': 0.04,  # simulation time step      (dt)
    'turn_sped': 1480,  # max rotational speed      (degrees per second)
    'velocity_max': 20,  # max velocity              (units per second)
    'acceleration_max': 0.25,  # max acceleration (+/-)    (units per second^2)

    'border_x_min': 0,  # arena western border
    'border_x_max': 800,  # arena eastern border
    'border_y_min': 0,  # arena southern border
    'border_y_max': 800,  # arena northern border

    'plot': True,  # plot final generation?

    # Neural Net
    'input_nodes': 1,  # number of input nodes
    'hidden_nodes': 10,  # number of hidden nodes
    'output_nodes': 2  # number of output nodes
}


def run(settings):
    # Food
    foods = []
    for i in range(0, settings['food_num']):
        foods.append(food(settings))

    # Unit
    units = []
    for i in range(0, settings['units_count']):
        wih_init = np.random.uniform(-1, 1, (
            settings['hidden_nodes'], settings['input_nodes']))  # mlp weights (input -> hidden)
        who_init = np.random.uniform(-1, 1, (
            settings['output_nodes'], settings['hidden_nodes']))  # mlp weights (hidden -> output)

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
