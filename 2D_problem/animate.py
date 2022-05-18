import numpy as np
import pygame
import pygame_utils as pg
import utils as ut
pygame.init()

dt = 1/120
display_framerate = 60

# define initial state
list_positions = [[0,0],[0.7,0.1]]
positions = [np.array(p) for p in list_positions]


velocities = [0 for p in positions]

screen, clock = pg.start_display()

while True:
    pg.check_quit()
    positions, velocities = ut.timestep(positions, velocities, dt)

    pg.draw_positions(positions, screen)

    clock.tick(display_framerate)

