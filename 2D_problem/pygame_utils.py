import pygame
import sys

HEIGHT = 800
WIDTH = 1200
box_height = 100

background_colour = (110,170,120)
dot_colour = (90,30,30)
box_colour = (250,250,250)
dot_rad = 30  # radius in pixels


def start_display():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    screen.fill(background_colour)
    return screen, clock

def draw_positions(positions, screen, length):
    # draw rectangle for 'electrons' to bounce inside
    box = (0,(HEIGHT - box_height)/2,WIDTH,box_height)
    pygame.draw.rect(screen, box_colour, box)

    for pos in positions:
        screen_pos = (int(WIDTH * pos/ length), HEIGHT/2)
        pygame.draw.circle(screen, dot_colour, screen_pos, dot_rad)

    pygame.display.update()

def check_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

