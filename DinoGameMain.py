import pygame
class dino:
    def __init__(self):
        pass


    dino_sprite_index = 0,0

    spritefolder ="DinoGame/DINOSPRITE/"
    screen = pygame.display.set_mode((800, 600))
    Dino = pygame.image.load(spritefolder + "sprite_00.png").convert_alpha()
    sprite_00 = pygame.image.load(spritefolder+"sprite_00.png").convert_alpha()
    sprite_01 = pygame.image.load(spritefolder+"sprite_01.png").convert_alpha()
    sprite_02 = pygame.image.load(spritefolder+"sprite_02.png").convert_alpha()
    sprite_03 = pygame.image.load(spritefolder+"sprite_03.png").convert_alpha()
    sprite_04 = pygame.image.load(spritefolder+"sprite_04.png").convert_alpha()
    sprite_05 = pygame.image.load(spritefolder+"sprite_05.png").convert_alpha()
    sprite_06 = pygame.image.load(spritefolder+"sprite_06.png").convert_alpha()
    sprite_07 = pygame.image.load(spritefolder+"sprite_07.png").convert_alpha()
    sprite_08 = pygame.image.load(spritefolder+"sprite_08.png").convert_alpha()
    sprite_09 = pygame.image.load(spritefolder+"sprite_09.png").convert_alpha()
    sprite_10 = pygame.image.load(spritefolder+"sprite_10.png").convert_alpha()
    sprite_11 = pygame.image.load(spritefolder+"sprite_11.png").convert_alpha()
    sprite_12 = pygame.image.load(spritefolder+"sprite_12.png").convert_alpha()
    sprite_13 = pygame.image.load(spritefolder+"sprite_13.png").convert_alpha()
    sprite_14 = pygame.image.load(spritefolder+"sprite_14.png").convert_alpha()
    sprite_15 = pygame.image.load(spritefolder+"sprite_15.png").convert_alpha()
    sprite_16 = pygame.image.load(spritefolder+"sprite_16.png").convert_alpha()

    dino_sprites = [
        sprite_00, sprite_01, sprite_02, sprite_03, sprite_04,
        sprite_05, sprite_06, sprite_07, sprite_08, sprite_09,
        sprite_10, sprite_11, sprite_12, sprite_13, sprite_14,
        sprite_15, sprite_16
    ]
    current_sprite_index = 0
    clock = pygame.time.Clock()
    animation_timer = 0

    def RunGame(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                self.dino_sprite_index = 3, 4
            elif event.type == pygame.KEYUP:
                self.dino_sprite_index = 0, 2
            #elif event.type == #zaself.collide_rect(object):
             #   self.dino_sprite_index = 5, 16
              #  running = False
            else:
                self.dino_sprite_index = 0, 3

        self.animation_timer += 1
        if self.animation_timer >= 10:
            self.current_sprite_index = (self.current_sprite_index + 1) % len(self.dino_sprites)
            self.animation_timer = 0

            self.current_sprite_index += 1
            if self.current_sprite_index > self.dino_sprite_index[1]:
                self.current_sprite_index = self.dino_sprite_index[0]

        self.screen.fill((0, 0, 0))
        self.screen.blit(self.dino_sprites[self.current_sprite_index], (100, 100))







