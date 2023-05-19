import pygame


class Button:
    def __init__(self, x, y, width, height, text, text_color, font, bg_color):
        self.surface = pygame.Surface((width, height))
        self.surface.fill(bg_color)
        self.rect = self.surface.get_rect(topleft=(x, y))
        self.text = text
        self.text_color = text_color
        self.font = font
        self.bg_color = bg_color
        self.text_surface = self.font.render(self.text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)

    def draw(self, screen):
        screen.blit(self.surface, self.rect)
        screen.blit(self.text_surface, self.text_rect)

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                print("Button clicked")
                return True
        return False
