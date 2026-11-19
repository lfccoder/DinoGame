import pygame


from random import randint

from DinoObstacle import Obstacle

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

    obs_spawn_pos_x = 850
    obs_spawn_pos_y = 142

    world_speed = 10.0
    obs_spawn_min = 35
    obs_spawn_max = 57
    obs_spawn_timer = 0
    obs_spawn_run = randint(obs_spawn_min, obs_spawn_max)
    obstacles = []
    pygame.font.init()
    font = pygame.font.SysFont("Arial", 20)
    scoretext = font.render("Score: 0", True, (255, 255, 255))
    score = 0
    secondtimer = 0


    is_jumping = False
    player_y = 100
    ground_y = 100
    velocity_y = 0.0
    gravity = 0.6
    jump_velocity = -10


    is_crouching = False

    playerhitbox = pygame.Rect(121.5, player_y + 3, 54, 69)

    def RunGame(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not self.is_jumping:
                    self.is_jumping = True
                    self.velocity_y = self.jump_velocity
                if event.key == pygame.K_DOWN:
                    self.is_crouching = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    self.is_crouching = False
            #elif event.type == #zaself.collide_rect(object):
             #   self.dino_sprite_index = 5, 16
              #  running = False

        if self.is_crouching:
            self.dino_sprite_index = 3, 4
        else:
            self.dino_sprite_index = 0, 2

        self.animation_timer += 1
        if self.animation_timer >= 10:
            #self.current_sprite_index = (self.current_sprite_index + 1) % len(self.dino_sprites)
            self.animation_timer = 0
            self.current_sprite_index += 1
            if self.current_sprite_index > self.dino_sprite_index[1]:
                self.current_sprite_index = self.dino_sprite_index[0]

        self.obs_spawn_timer += 1

        if self.obs_spawn_timer >= self.obs_spawn_run:
            ran_obstacle = randint(0,1)
            new_obstacle = None
            if ran_obstacle == 0:
                new_obstacle = Obstacle(self.obs_spawn_pos_x,
                                        self.obs_spawn_pos_y,width = 32, height = 32, screen = self.screen,
                                        speed = self.world_speed,  image = None)

            elif ran_obstacle == 1:
                new_obstacle = Obstacle(self.obs_spawn_pos_x,
                                        self.obs_spawn_pos_y,width = 32, height = 32, screen = self.screen,
                                        speed = self.world_speed, image = None)

            self.obstacles.append(new_obstacle)

            self.obs_spawn_timer = 0
            self.obs_spawn_run = randint(self.obs_spawn_min, self.obs_spawn_max)

        for o in self.obstacles:
            o.posX -= self.world_speed
            if o.posX <= self.world_speed:
                self.obstacles.remove(o)

        if self.is_jumping:
            self.player_y += self.velocity_y

            self.velocity_y += self.gravity

            if self.player_y >= self.ground_y:
                self.player_y = self.ground_y
                self.velocity_y = 0
                self.is_jumping = False

        self.playerhitbox = pygame.Rect(121.5, self.player_y + 3, 54, 69)

        self.score += 1
        self.secondtimer += 1
        if self.secondtimer > 60:
            self.score += 10
            self.secondtimer = 0




        for o in self.obstacles:
            o.update()
            if o.hitbox.colliderect(self.playerhitbox):
                self.score = 0
                self.obstacles.remove(o)



        self.screen.fill((0, 0, 0))
        self.screen.blit(self.dino_sprites[self.current_sprite_index], (100, self.player_y))

        pygame.draw.rect(self.screen, (255,0,0), (121.5, self.player_y+3, 54, 69))
        self.scoretext = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(self.scoretext, (400, 100))
        for o in self.obstacles:
            pygame.draw.rect(self.screen, (255,0,0), (o.posX, o.posY, o.width, o.height))


