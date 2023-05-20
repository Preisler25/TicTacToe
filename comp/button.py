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

    def draw(self, screen):
        if self.was_set:
            self.surface.fill(self.color)
        screen.blit(self.surface, self.rect)

    def update(self, event, player):
        if self.was_set:
            return
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print(event)
            print(self.rect)
            if self.rect.collidepoint(event.pos):
                self.color = player.color
                self.was_set = True
                print(self.number)
