from appConst import screen, bg


def game():
    while True:
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
