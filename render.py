import cv2
from matplotlib import pyplot as plt
import numpy as np


def initialize(width, height, rgb_color=(0, 0, 0)):
    """Create new image(numpy array) filled with certain color in RGB"""
    # Create black blank image
    image = np.zeros((height, width, 3), np.uint8)

    # Since OpenCV uses BGR, convert the color first
    color = tuple(reversed(rgb_color))
    # Fill image with color
    image[:] = color

    return image


def render(settings, units, foods, gen, time):
    window_name = 'Camera'

    fig, ax = plt.subplots()
    fig.set_size_inches(9.6, 5.4)

    plt.xlim([settings['x_min'] + settings['x_min'] * 0.25, settings['x_max'] + settings['x_max'] * 0.25])
    plt.ylim([settings['y_min'] + settings['y_min'] * 0.25, settings['y_max'] + settings['y_max'] * 0.25])

    # Plot units
    for unit in units:
        render_unit(unit.x, unit.y, unit.r, ax)

    # Plot food particles
    for food in foods:
        render_foot(food.x, food.y, ax)

    cv2.imshow(window_name, image)


def render_unit(x, y, theta, ax):

    coordinates = (x, y)
    radius = 20
    color = (255, 0, 0)
    thickness = 2

    image = cv2.circle(image, coordinates, radius, color, thickness)


def render_foot(x1, y1, ax):
    image = cv2.circle(image, center_coordinates, radius, color, thickness)
