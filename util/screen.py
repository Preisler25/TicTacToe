import pygame


class Screen:
    def __init__(self):
        self.width = 1920
        self.height = 1080
        self.screen = pygame.display.set_mode(
            (self.width, self.height), pygame.FULLSCREEN)

    def load_image(self, path):
        return pygame.image.load(path)

    def draw(self, rect):
        self.screen.blit(rect, (0, 0))

    def update(self):
        pygame.display.update()
