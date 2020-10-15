import pygame
from pygame import gfxdraw


def render(settings, units, foods, gen, time):
    pygame.init()

    screen = pygame.display.set_mode([800, 800])
    pygame.display.set_caption("")

    screen.fill((255, 255, 255))

    # Plot units
    for unit in units:
        render_unit(screen, int((unit.x + 2.1) * 200), int((unit.y + 2.1) * 200), unit.r, unit.alive)

    # Plot food particles
    for food in foods:
        render_foot(screen, int((food.x + 2.1) * 200), int((food.y + 2.1) * 200))

    pygame.display.flip()

#   pygame.quit()
def render_unit(screen, x, y, r, alive):
    if alive:
        draw_circle(screen, x, y, 4, (102, 102, 255), (102, 102, 255))
    else:
        draw_circle(screen, x, y, 4, (0, 0, 0), (50, 50, 50))

def render_foot(screen, x, y):
    draw_circle(screen, x, y, 3, (255, 178, 102), (255, 178, 102))


def draw_circle(surface, x, y, radius, color, color2):
    gfxdraw.aacircle(surface, x, y, radius, color)
    gfxdraw.filled_circle(surface, x, y, radius, color2)
