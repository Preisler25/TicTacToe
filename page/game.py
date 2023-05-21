import pygame
from appConst import screen, bg
from comp.text_field import ShowActivPlayer
from appConst import game_round


def game():

    active_player_tf = ShowActivPlayer(
        screen.width/2-screen.width/20, 0, screen.width/10, screen.height/20, game_round.active_player.name, (255, 255, 255), pygame.font.SysFont("Arial", 30), (0, 0, 0))

    while game_round.game_over == False:
        screen.draw(bg)
        game_round.draw()
        active_player_tf.draw(screen.screen)

        for event in pygame.event.get():
            game_round.update(event)
            if event.type == pygame.QUIT:
                game_round.game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_round.game_over = True
        screen.update()

    print("Game Over")
