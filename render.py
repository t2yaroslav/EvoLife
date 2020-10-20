import pygame
from pygame import gfxdraw


def render(settings, units, foods, gen, time):
    pygame.init()

    screen = pygame.display.set_mode([800, 800])
    pygame.display.set_caption("")

    screen.fill((255, 255, 255))

    # Plot units
    for unit in units:
        render_unit(screen, int((unit.x + 2.1) * 200), int((unit.y + 2.1) * 200), unit.r, unit.alive, unit.generation)

    # Plot food particles
    for food in foods:
        render_foot(screen, int((food.x + 2.1) * 200), int((food.y + 2.1) * 200), int(food.energy/10))

    pygame.display.flip()


#   pygame.quit()
def render_unit(screen, x, y, r, alive, generation):
    colors = {
        1: (100, 100, 255),
        2: (50, 255, 100),
        3: (50, 255, 255),
        4: (255, 150, 50),
        5: (255, 50, 255)
    }

    try:
        color = colors[generation]
    except KeyError as e:
        color = colors[1]

    if alive:
        draw_circle(screen, x, y, 4, (100, 102, 255), color)
    else:
        draw_circle(screen, x, y, 4, (100, 100, 100), (200, 200, 200))


def render_foot(screen, x, y, radius):
    draw_circle(screen, x, y, radius, (255, 100, 50), (255, 178, 102))


def draw_circle(surface, x, y, radius, color, color2):
    gfxdraw.filled_circle(surface, x, y, radius, color2)
    gfxdraw.aacircle(surface, x, y, radius, color)
