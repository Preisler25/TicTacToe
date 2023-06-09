import pygame
from appConst import screen, bg, game_round
from comp.button import PressButton


def lobby():
    lobby = True

    new_game_button = PressButton(screen.width/2-screen.width/10, screen.height/2-screen.height/20,
                                  screen.width/5, screen.height/10, "New Game", (255, 255, 255), pygame.font.SysFont("Arial", 30), (0, 0, 0))

    quit_button = PressButton(screen.width/2-screen.width/10, screen.height/2+screen.height/20,
                              screen.width/5, screen.height/10, "Quit", (255, 255, 255), pygame.font.SysFont("Arial", 30), (0, 0, 0))

    while lobby:
        screen.draw(bg)
        new_game_button.draw(screen.screen)
        quit_button.draw(screen.screen)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if new_game_button.rect.collidepoint(event.pos):
                    game_round.rounds += 1
                    game_round.reset(screen)
                    lobby = False
                if quit_button.rect.collidepoint(event.pos):
                    game_round.game_over = True
                    lobby = False
            if event.type == pygame.QUIT:
                lobby = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    lobby = False
        screen.update()
    print("lobby over")
