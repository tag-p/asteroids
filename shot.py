import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, SHOT_RADIUS)
        self.rotation = rotation

    def update(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.velocity = forward * PLAYER_SHOT_SPEED
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
