import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED

class Player(CircleShape):
    def __init__(self, x, y) -> None:
        super().__init__(x, y, radius=PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface, color: str, pts: list[pygame.Vector2], line_width: int = LINE_WIDTH) -> None:
        pygame.draw.polygon(screen, color, pts, line_width)
    
    def rotate(self, dt: float) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotation += PLAYER_TURN_SPEED * (dt * -1)
        if keys[pygame.K_d]:
            self.rotation += PLAYER_TURN_SPEED * dt