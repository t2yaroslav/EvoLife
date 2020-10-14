import cv2
from matplotlib import pyplot as plt
import numpy as np


def create_blank(width, height, rgb_color=(0, 0, 0)):
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
    image = create_blank(300, 300)

    # Plot units
    for unit in units:
        render_unit(image, unit.x, unit.y, unit.r)

    # Plot food particles
    for food in foods:
        render_foot(image, food.x, food.y)

    cv2.imshow(window_name, image)
    cv2.waitKey(1)


def render_unit(image, x, y, theta):

    coordinates = (int(x), int(y))
    radius = 5
    color = (255, 0, 0)
    thickness = 1

    image = cv2.circle(image, coordinates, radius, color, thickness)


def render_foot(image, x, y):
    coordinates = (int(x), int(y))
    radius = 5
    color = (255, 0, 0)
    thickness = 1
    image = cv2.circle(image, coordinates, radius, color, thickness)
