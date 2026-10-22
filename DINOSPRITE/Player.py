import sys
import pygame
import time

from pygame.sprite import collide_rect

pygame.init()
event = pygame.event.get()
Dino = pygame.image.load("sprite_00.png").convert_alpha()
screen = pygame.display.set_mode((800, 600))

sprite_00 = pygame.image.load("sprite_00.png").convert_alpha()
sprite_01 = pygame.image.load("sprite_01.png").convert_alpha()
sprite_02 = pygame.image.load("sprite_02.png").convert_alpha()
sprite_03 = pygame.image.load("sprite_03.png").convert_alpha()
sprite_04 = pygame.image.load("sprite_04.png").convert_alpha()
sprite_05 = pygame.image.load("sprite_05.png").convert_alpha()
sprite_06 = pygame.image.load("sprite_06.png").convert_alpha()
sprite_07 = pygame.image.load("sprite_07.png").convert_alpha()
sprite_08 = pygame.image.load("sprite_08.png").convert_alpha()
sprite_09 = pygame.image.load("sprite_09.png").convert_alpha()
sprite_10 = pygame.image.load("sprite_10.png").convert_alpha()
sprite_11 = pygame.image.load("sprite_11.png").convert_alpha()
sprite_12 = pygame.image.load("sprite_12.png").convert_alpha()
sprite_13 = pygame.image.load("sprite_13.png").convert_alpha()
sprite_14 = pygame.image.load("sprite_14.png").convert_alpha()
sprite_15 = pygame.image.load("sprite_15.png").convert_alpha()
sprite_16 = pygame.image.load("sprite_16.png").convert_alpha()

dino_sprites = [
    sprite_00, sprite_01, sprite_02, sprite_03, sprite_04,
    sprite_05, sprite_06, sprite_07, sprite_08, sprite_09,
    sprite_10, sprite_11, sprite_12, sprite_13, sprite_14,
    sprite_15, sprite_16
]
current_sprite_index = 0
clock = pygame.time.Clock()
animation_timer = 0

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        animation_timer += 1
        if animation_timer >= 10:
            current_sprite_index = (current_sprite_index + 1) % len(dino_sprites)
            animation_timer = 0

            if event.type == pygame.KEYDOWN:
                dino_sprite_index = 3,4
            elif event.type == pygame.KEYUP:
                dino_sprite_index = 0,1,2,3
            elif event.type == collide_rect(object):
                dino_sprite_index = 5-17
                running = False

    screen.blit(dino_sprites[current_sprite_index], (100, 100))

pygame.display.flip()
clock.tick(60)

