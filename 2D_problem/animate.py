import pygame
import pygame_utils as pg
import utils as ut
pygame.init()

dt = 1/240
display_framerate = 60

length = 1   # gap that particles can move in

# define initial state
positions = [0.1,0.5]
velocities = [0 for p in positions]

screen, clock = pg.start_display()

while True:
    pg.check_quit()
    positions, velocities = ut.timestep(positions, velocities, length, dt)

    pg.draw_positions(positions, screen, length)

    clock.tick(display_framerate)

