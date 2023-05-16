import pygame


class Screen:
    def __init__(self):
        self.screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
        self.running = True

    def load_image(self, path):
        return pygame.image.load(path)

    def draw(self, rect):
        self.screen.blit(rect, (0, 0))

    def update(self):
        pygame.display.update()

    def quit(self):
        self.running = False
