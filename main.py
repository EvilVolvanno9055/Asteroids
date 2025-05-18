import pygame
from player import Player
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
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
            
    player.update(dt)    
    screen.fill("black")
    
    player.draw(screen)

    

    pygame.display.flip()
    dt = (clock.tick(60) / 1000)
    # print(f"FPS: {clock.get_fps():.1f}, dt: {dt:.4f}")

if __name__ == "__main__":
    main()