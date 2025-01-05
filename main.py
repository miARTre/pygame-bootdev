# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
    # print("Starting asteroids!")
    # print('Screen width:', SCREEN_WIDTH)
    # print('Screen height:', SCREEN_HEIGHT)
    
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    player = Player(
        x = SCREEN_WIDTH / 2,
        y = SCREEN_HEIGHT / 2,
    )
   

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 

        screen.fill(pygame.Color('black'))      
        player.draw(screen)     
        pygame.display.flip()
        
        # rotate player to the left and right
        player.update(dt)
        
        
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

    

if __name__ == "__main__":
    main()
    
