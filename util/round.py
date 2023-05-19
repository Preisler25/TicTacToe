from comp.button import MapButton
import math
from appConst import screen


class GameRound:
    def __init__(self, player1, player2, game_round, active_player):
        self.player1 = player1
        self.player2 = player2
        self.game_round = game_round
        self.active_player = active_player
        self.map = [MapButton((i % 3) * (screen.width/3), math.ceil(i/3) * (screen.height/3), screen.width/3, screen.height/3)
                    for i in range(9)]

    def setingSquer(self, squer, player):
        self.map[squer] = player.color

    def chActivePlayer(self):
        if self.active_player == self.player1:
            self.active_player == self.player2
        else:
            self.active_player = self.player1
