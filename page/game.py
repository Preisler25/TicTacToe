import pygame
from appConst import screen, bg
from comp.text_field import ShowActivPlayer
from util.round import GameRound
from util.player import Player


def game():

    player1 = Player("Player 1", (255, 0, 0))
    player2 = Player("Player 2", (0, 255, 0))

    game_round = GameRound(player1, player2, 1, player1)

    active_player_tf = ShowActivPlayer(
        screen.width/2-screen.width/20, 0, screen.width/10, screen.height/20, game_round.active_player.name, (255, 255, 255), pygame.font.SysFont("Arial", 30), (0, 0, 0))

    running = True
    while running:
        screen.draw(bg)
        active_player_tf.draw(screen.screen)

        for event in pygame.event.get():
            game_round.update(event)
            if event.type == pygame.QUIT:
                running = False
                screen.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    screen.quit()
        screen.update()

    pygame.quit()
