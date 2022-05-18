import numpy as np
import pygame
import pygame_utils as pg
import utils as ut
pygame.init()

dt = 1/120
display_framerate = 120
n_circles = 15


positions = ut.random_starts(n_circles)
velocities = [0 for p in positions]

screen, clock = pg.start_display()

while True:
    pg.check_quit()
    positions, velocities = ut.timestep(positions, velocities, dt)
    pg.draw_positions(positions, screen)
    clock.tick(display_framerate)

