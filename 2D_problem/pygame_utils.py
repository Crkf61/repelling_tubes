import numpy as np
import pygame
import sys

SIZE = 800

background_colour = (110,170,120)
dot_colour = (90,30,30)
shell_colour = (250,250,250)
dot_rad = 100  # radius in pixels


def start_display():
    screen = pygame.display.set_mode((SIZE, SIZE))
    clock = pygame.time.Clock()
    screen.fill(background_colour)
    return screen, clock

def draw_positions(positions, screen):
    # draw circle for 'electrons' to bounce inside
    RAD = SIZE/2
    pygame.draw.circle(screen, shell_colour, (RAD, RAD), RAD)

    n_circles = len(positions)
    circle_radius = dot_rad/np.sqrt(n_circles)

    for pos in positions:
        #print(pos)
        pos_from_top_left = np.array([1 + pos[0], 1 - pos[1]])
        #print(pos_from_top_left)
        screen_pos = np.round(RAD * pos_from_top_left)
        #print(screen_pos)
        pygame.draw.circle(screen, dot_colour, screen_pos, circle_radius)

    pygame.display.update()

def check_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

