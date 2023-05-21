from comp.button import MapButton
from appConst import screen
from func.endGameFunc import checkWin, checkDraw
import math


class GameRound:
    def __init__(self, player1, player2, game_round, active_player):
        self.player1 = player1
        self.player2 = player2
        self.game_round = game_round
        self.active_player = active_player
        self.map = [MapButton((i % 3) * screen.width/3, math.floor(i / 3)
                              * screen.height/3, screen.width/3, screen.height/3, i) for i in range(9)]
        self.rounds = 1
        self.round_over = False
        self.game_over = False

    def setingSquer(self, squer, player):
        self.map[squer] = player.color

    def chActivePlayer(self):
        print(self.active_player == self.player1)
        if self.active_player == self.player1:
            self.active_player = self.player2
        else:
            self.active_player = self.player1

    def checkWin(self):
        if checkWin(self.map):
            self.round_over = True

    def checkDraw(self):
        if checkDraw(self.map):
            self.round_over = True

    def draw(self):
        for i in self.map:
            i.draw(screen.screen)

    def update(self, event):
        if self.round_over:
            pass
        for i in self.map:
            if i.update(event, self.active_player) == True:
                print("updated")
                self.checkWin()
                if self.checkDraw:
                    pass
                self.chActivePlayer()
