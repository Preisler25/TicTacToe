import pygame


class Button:
    def __init__(self, x, y, width, height):
        self.surface = pygame.Surface((width, height))
        self.rect = self.surface.get_rect(topleft=(x, y))

    def draw(self, screen):
        screen.blit(self.surface, self.rect)


class MapButton(Button):
    def __init__(self, x, y, width, height, number):
        super().__init__(x, y, width, height)
        self.number = number
        self.color = (255, 255, 255)
        self.was_set = False

    def __str__(self) -> str:
        return f"MapButton {self.number}, rect: {self.rect}, color: {self.color}, was_set: {self.was_set}"

    def draw(self, screen, player):
        if self.was_set:
            self.surface.fill(player.color)
            screen.blit(self.surface, self.rect)

        

    def update(self, event, player, screen):
        if self.was_set:
            return
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print(event)
            print(self.rect.collidepoint(event.pos))
            if self.rect.collidepoint(event.pos):
                self.color = player.color
                self.was_set = True
                self.draw(screen)
