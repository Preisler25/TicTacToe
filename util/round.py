class GameRound:
    def __init__(self, player1, player2, game_round, active_player):
        self.player1 = player1
        self.player2 = player2
        self.game_round = game_round
        self.active_player = active_player

    def chActivePlayer(self):
        if self.active_player == self.player1:
            self.active_player == self.player2
        else:
            self.active_player = self.player1
