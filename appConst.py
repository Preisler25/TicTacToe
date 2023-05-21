from util.screen import Screen
from util.player import Player
from util.round import GameRound

screen = Screen()
bg = screen.load_image("src/lobby_bg.jpeg")

player1 = Player("Player 1", (255, 0, 0))
player2 = Player("Player 2", (0, 255, 0))

game_round = GameRound(player1, player2, 1, player1)
