import pygame, random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, position, radius, velocity):
        super().__init__(position.x, position.y, radius)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt  # Update position based on velocity
        # Add screen wrapping logic if needed

    def split(self):
        # Logic to split the asteroid into smaller ones
        if self.radius > ASTEROID_MIN_RADIUS * 2:
            random_angle = random.uniform(20, 50)
            vel1 = self.velocity.rotate(random_angle) * 1.2
            vel2 = self.velocity.rotate(-random_angle) * 1.2
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position, new_radius, vel1)
            asteroid2 = Asteroid(self.position, new_radius, vel2)
            self.kill()
            return [asteroid1, asteroid2]  # Return the new asteroids
        else:
            self.kill()
            return []  # No split if radius is too small
        