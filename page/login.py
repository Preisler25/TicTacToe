import pygame
from appConst import screen, bg


def login():

    running = True
    while running:
        screen.draw(bg)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                screen.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    screen.quit()
        screen.update()

    pygame.quit()
