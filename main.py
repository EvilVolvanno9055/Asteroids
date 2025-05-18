import pygame
from player import Player
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
Player.containers = (updatable, drawable)

asteroids = pygame.sprite.Group()
Asteroid.containers = (asteroids, updatable, drawable)

AsteroidField.containers = (updatable)
asteroid_field = AsteroidField()

x = SCREEN_WIDTH / 2
y = SCREEN_HEIGHT / 2
player = Player(x, y)

clock = pygame.time.Clock()
dt = 0
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



running = True


while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    updatable.update(dt)
    for draw_item in drawable:
        draw_item.draw(screen)    

    

    pygame.display.flip()
    dt = (clock.tick(60) / 1000)
    # print(f"FPS: {clock.get_fps():.1f}, dt: {dt:.4f}")

if __name__ == "__main__":
    main()