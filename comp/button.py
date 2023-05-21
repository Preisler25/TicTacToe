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

    def draw(self, screen):
        if self.was_set:
            self.surface.fill(self.color)
            screen.blit(self.surface, self.rect)

    def update(self, event, player):
        if self.was_set:
            return False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.color = player.color
                self.was_set = True
                print("set")
                return True


class PressButton(Button):
    def __init__(self, x, y, width, height, text, text_color, font, bg_color):
        super().__init__(x, y, width, height)
        self.text = text
        self.text_color = text_color
        self.font = font
        self.bg_color = bg_color
        self.text_surface = self.font.render(self.text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)

    def draw(self, screen):
        self.surface.fill(self.bg_color)
        screen.blit(self.surface, self.rect)
        screen.blit(self.text_surface, self.text_rect)

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False
