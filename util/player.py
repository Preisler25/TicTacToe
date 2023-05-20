class Player:
    def __init__(self, name, color, score=0):
        self.name = name
        self.color = color
        self.score = score

    def __str__(self) -> str:
        return f"Player {self.name}, color: {self.color}, score: {self.score}"
