import pygame


class Screen:
    def __init__(self):
        self.width = 900
        self.height = 900
        self.screen = pygame.display.set_mode(
            (self.width, self.height))
        self.running = True

    def load_image(self, path):
        return pygame.image.load(path)

    def draw(self, rect):
        self.screen.blit(rect, (0, 0))

    def update(self):
        pygame.display.update()

    def quit(self):
        self.running = False
