import pygame
from appConst import screen, bg
from comp.text_field import ShowActivPlayer


def game():

    active_player_tf = ShowActivPlayer(
        screen.width/2-screen.width/20, 0, screen.width/10, screen.height/20, "Player 1", (255, 255, 255), pygame.font.SysFont("Arial", 30), (0, 0, 0))

    running = True
    while running:
        screen.draw(bg)
        active_player_tf.draw(screen.screen)

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
