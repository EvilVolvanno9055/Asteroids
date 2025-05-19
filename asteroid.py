import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)
        
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        direction = random.uniform(20, 50)
        self.velocity1 = self.velocity.rotate(direction)
        self.velocity2 = self.velocity.rotate(-direction)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        astroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        astroid1.velocity = self.velocity1 * 1.2
        astroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        astroid2.velocity = self.velocity2 * 1.2