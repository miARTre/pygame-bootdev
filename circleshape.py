import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius


    # def collision(self, new_circle):
    #     dist = self.position.distance_to(new_circle.position)
    #     r1 = self.radius
    #     r2 = new_circle.radius
    #     col = r1 + r2
        
    #     return dist <= col

    def collides_with(self, other):
        return self.position.distance_to(other.position) <= self.radius + other.radius


    def draw(self, screen):
        pass

    def update(self, dt):
        pass