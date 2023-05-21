import pygame
from appConst import screen, bg, game_round
from comp.text_field import ShowActivPlayer
from page.lobby import lobby


def game():

    active_player_tf = ShowActivPlayer(
        screen.width/2-screen.width/16, 0, screen.width/8, screen.height/20, game_round.active_player.name, (255, 255, 255), pygame.font.SysFont("Arial", 30), (0, 0, 0))

    while game_round.game_over == False:
        if game_round.round_over == True:
            lobby()

        screen.draw(bg)
        game_round.draw(screen.screen)
        active_player_tf.update(game_round.active_player.name)
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
