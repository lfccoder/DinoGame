import pygame
from DinoGameMain import dino
import sys
pygame.init()
g = dino()

running = True
while running:
    pygame.display.flip()

    g.RunGame()

    g.clock.tick(60)


    # 4. Clean up
pygame.quit()
sys.exit()

