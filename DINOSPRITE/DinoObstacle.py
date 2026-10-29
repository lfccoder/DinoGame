import pygame

class Obstacle(pygame.sprite.Sprite):
    width = 32
    height = 32
    posX = 0
    posY = 0
    speed = 0
    screen = None
    image = None

    def __init__(self, posX,posY,width,height,screen, image,speed):
        super().__init__()
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
        self.speed = speed
        self.screen = screen
        self.image = image


