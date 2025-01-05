# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    # print("Starting asteroids!")
    # print('Screen width:', SCREEN_WIDTH)
    # print('Screen height:', SCREEN_HEIGHT)
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shoots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Shot.containers = (shoots, updatable, drawable)

    Player.containers = (updatable, drawable)

    player = Player(
        x = SCREEN_WIDTH / 2,
        y = SCREEN_HEIGHT / 2,
    )


    dt = 0
   
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
            
        for update in updatable:
            update.update(dt)

        screen.fill(pygame.Color('black'))

        for draw in drawable:
            draw.draw(screen)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

        
        for asteroid in asteroids:
            for shot in shoots:  
                if asteroid.collides_with(shot):
                    asteroid.kill()
                    shot.kill()

        pygame.display.flip()
        
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

    
if __name__ == "__main__":
    main()
    
