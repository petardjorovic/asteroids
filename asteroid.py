import pygame
from circleshape import CircleShape
from constants import *
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        random_angle = random.uniform(20,50)
        first_movement = self.velocity.rotate(random_angle)
        second_movement = self.velocity.rotate(-random_angle)
        first_new = Asteroid(self.position.x, self.position.y, new_radius)
        second_new = Asteroid(self.position.x, self.position.y, new_radius)
        first_new.velocity = first_movement * 1.2
        second_new.velocity = second_movement * 1.2