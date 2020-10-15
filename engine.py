from collections import defaultdict
import operator
from math import atan2
from math import degrees
from math import floor
from math import sqrt
from random import randint
from random import random
from random import sample
from random import uniform

from render import render
from unit import unit


def dist(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def calc_heading(org, food):
    d_x = food.x - org.x
    d_y = food.y - org.y
    theta_d = degrees(atan2(d_y, d_x)) - org.r
    if abs(theta_d) > 180: theta_d += 360
    return theta_d / 180


def evolve(settings, units_old, gen):
    elitism_num = int(floor(settings['elitism'] * settings['pop_size']))
    new_orgs = settings['pop_size'] - elitism_num

    # Get stats from current generation
    stats = defaultdict(int)
    for org in units_old:
        if org.fitness > stats['Best'] or stats['Best'] == 0:
            stats['Best'] = org.fitness

        if org.fitness < stats['Worst'] or stats['Worst'] == 0:
            stats['Worst'] = org.fitness

        stats['Sum'] += org.fitness
        stats['Count'] += 1

    stats['Avg'] = stats['Sum'] / stats['Count']

    # Elitism (keep Best performing units)
    orgs_sorted = sorted(units_old, key=operator.attrgetter('fitness'), reverse=True)
    units_new = []
    for i in range(0, elitism_num):
        units_new.append(
            unit(settings, wih=orgs_sorted[i].wih, who=orgs_sorted[i].who, name=orgs_sorted[i].name))

    # Generate new units
    for w in range(0, new_orgs):

        # Selection (truncation selection)
        canidates = range(0, elitism_num)
        random_index = sample(canidates, 2)
        org_1 = orgs_sorted[random_index[0]]
        org_2 = orgs_sorted[random_index[1]]

        # Crossover
        crossover_weight = random()
        wih_new = (crossover_weight * org_1.wih) + ((1 - crossover_weight) * org_2.wih)
        who_new = (crossover_weight * org_1.who) + ((1 - crossover_weight) * org_2.who)

        # Mutation
        mutate = random()
        if mutate <= settings['mutate']:

            # Pick which weight matrix to mutate
            mat_pick = randint(0, 1)

            # Mutate: wih weights
            if mat_pick == 0:
                index_row = randint(0, settings['hnodes'] - 1)
                wih_new[index_row] = wih_new[index_row] * uniform(0.9, 1.1)
                if wih_new[index_row] > 1: wih_new[index_row] = 1
                if wih_new[index_row] < -1: wih_new[index_row] = -1

            # Mutate: who weights
            if mat_pick == 1:
                index_row = randint(0, settings['onodes'] - 1)
                index_col = randint(0, settings['hnodes'] - 1)
                who_new[index_row][index_col] = who_new[index_row][index_col] * uniform(0.9, 1.1)
                if who_new[index_row][index_col] > 1: who_new[index_row][index_col] = 1
                if who_new[index_row][index_col] < -1: who_new[index_row][index_col] = -1

        units_new.append(
            unit(settings, wih=wih_new, who=who_new, name='gen[' + str(gen) + ']-org[' + str(w) + ']'))

    return units_new, stats


def simulate(settings, units, foods, gen):
    total_time_steps = int(settings['gen_time'] / settings['dt'])

    # Cycle through each time step
    for t_step in range(0, total_time_steps, 1):

        # Plot simulation frame
        if settings['plot'] == True:  # and gen == settings['gens'] - 1:
            render(settings, units, foods, gen, t_step)

        # Update fitness function
        for food in foods:
            for org in units:
                food_org_dist = dist(org.x, org.y, food.x, food.y)

                # Spend of energy/fitness (depends to speed)
                org.fitness = org.fitness - (org.velocity + org.velocity) / 30
                if org.fitness <= 0:
                    org.velocity = 0
                    org.alive = False

                # Update fitness function
                if food_org_dist <= 0.075:
                    org.fitness += food.energy
                    food.respawn(settings)

                # Reset distance and heading to nearest food source
                org.d_food = 100
                org.r_food = 0

        # Calculate heading to nearest food source
        for food in foods:
            for org in units:

                # Calculate distance to selected food particle
                food_org_dist = dist(org.x, org.y, food.x, food.y)

                # Determine if this is the closest food particle
                if food_org_dist < org.d_food:
                    org.d_food = food_org_dist
                    org.r_food = calc_heading(org, food)

        # Get unit response
        for org in units:
            if org.alive: org.think()

        # Update units position and velocity
        for org in units:
            if org.alive:
                org.update_r(settings)
                org.update_vel(settings)
                org.update_pos(settings)

    return units
