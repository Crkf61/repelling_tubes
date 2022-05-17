import pygame, sys

dt = 1/50
Dsh = 64  # mm

def create_tube():



def step_physics(dt):
    return 0


pygame.init()
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((217,217,217))
    step_physics(dt)
    pygame.display.update()
    clock.tick(120)  # limits fps to 120
