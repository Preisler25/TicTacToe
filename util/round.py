from comp.button import MapButton
import math
from appConst import screen


class GameRound:
    def __init__(self, player1, player2, game_round, active_player):
        self.player1 = player1
        self.player2 = player2
        self.game_round = game_round
        self.active_player = active_player
        self.map = [MapButton((i % 3) * 300, math.floor(i / 3)
                              * 300, 300, 300, i) for i in range(9)]

    def setingSquer(self, squer, player):
        self.map[squer] = player.color

    def chActivePlayer(self):
        print(self.active_player == self.player1)
        if self.active_player == self.player1:
            self.active_player = self.player2
            print(self.active_player)
        else:
            self.active_player = self.player1

    def checkWin(self):
        pass

    def checkDraw(self):
        pass

    def draw(self):
        for i in self.map:
            i.draw(screen.screen)

    def update(self, event):
        for i in self.map:
            if i.update(event, self.active_player) == True:
                print("True")
                self.chActivePlayer()
