import pygame
import math


class Ball:
    def __init__(self, x, y, angle, speed):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed

    def update(self, dt):
        self.x += self.speed * math.cos(math.radians(self.angle)) * dt
        self.y -= self.speed * math.sin(math.radians(self.angle)) * dt

        if self.x < 0 or self.x > width2:
            self.angle = 180 - self.angle
        if self.y < 0 or self.y > height2:
            self.angle = -self.angle

    def draw(self, screen):
        screen.fill('black')
        pygame.draw.rect(screen, 'gray', (10, 10, size2[0], size2[1]))
        pygame.draw.circle(screen, 'white', (int(self.x), int(self.y)), 10)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('xonix')
    size1 = width1, height1 = 800, 600
    screen = pygame.display.set_mode(size1)
    size2 = width2, height2 = 780, 580
    screen.fill('black')
    pygame.draw.rect(screen, 'gray', (10, 10, size2[0], size2[1]))
    running = True
    clock = pygame.time.Clock()
    while running:
        dt = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                ball = Ball(390, 10, 145, 100)
        ball.update(dt)
        ball.draw(screen)
        pygame.display.flip()
    pygame.quit()