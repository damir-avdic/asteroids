import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = (updatable)
    Asteroid.containers = (updatable, drawable, asteroids)
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(x,y)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.colliding(shot):
                    asteroid.split()
                    shot.kill()
            if player.colliding(asteroid):
                print("Game over!")
                sys.exit()

        for sprite in drawable:
            sprite.draw(screen)

        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
if __name__ == "__main__":
    main()