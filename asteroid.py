import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

        # Draw the asteroid as a circle
    def update(self, dt):
        self.position += self.velocity * dt

    def collides_with(self, other):
        return self.position.distance_to(other.position) <= self.radius + other.radius

    def split(self):
        self.kill()
        # Logic to split the asteroid into smaller pieces
        if self.radius <= ASTEROID_MIN_RADIUS:
            return  # Can't split further
        new_radius = self.radius / 2
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        # Assign random velocities to the new asteroids
        asteroid1.velocity = pygame.Vector2(1, 0).rotate(
            pygame.Vector2().angle_to(self.velocity) + 30) * self.velocity.length()
        asteroid2.velocity = pygame.Vector2(1, 0).rotate(
            pygame.Vector2().angle_to(self.velocity) - 30) * self.velocity.length()
        return [asteroid1, asteroid2]
