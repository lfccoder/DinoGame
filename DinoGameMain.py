import pygame
class dino:
    def __init__(self):
        pass

    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    def RunGame(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()