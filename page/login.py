import pygame
from appConst import screen, bg
from comp.button import Button


def login():

    login_btn = Button(100, 100, 100, 100, "Login",
                       (255, 255, 255), pygame.font.Font(None, 50), (0, 0, 0))

    running = True
    while running:
        screen.draw(bg)
        login_btn.draw(screen.screen)

        for event in pygame.event.get():

            login_btn.update(event)

            if event.type == pygame.QUIT:
                running = False
                screen.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    screen.quit()
        screen.update()

    pygame.quit()
