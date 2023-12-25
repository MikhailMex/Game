import pygame
import math
import random


class Ball:
    def __init__(self, speed):
        self.x = 390
        self.y = 20
        self.angle = random.randint(0, 360)
        self.speed = speed
        self.speed1 = speed

    def update(self, dt):
        self.x += self.speed * math.cos(math.radians(self.angle)) * dt
        self.y -= self.speed * math.sin(math.radians(self.angle)) * dt

        if self.x < 20 or self.x > width2:
            self.angle = 180 - self.angle
        if self.y < 20 or self.y > height2:
            self.angle = -self.angle

    def draw(self, screen):
        screen.fill('black')
        pygame.draw.rect(screen, gray, (10, 10, size2[0], size2[1]))
        pygame.draw.circle(screen, white, (int(self.x), int(self.y)), 10)
        pygame.draw.rect(screen, white, (700, 600, 50, 50), 1)
        pygame.draw.rect(screen, white, (600, 600, 50, 50), 1)
        pygame.draw.rect(screen, white, (450, 600, 100, 50), 1)

        font = pygame.font.Font(None, 100)
        text = font.render('>', True, red)
        screen.blit(text, (705, 585))

        font = pygame.font.Font(None, 100)
        text = font.render('<', True, red)
        screen.blit(text, (605, 585))

        font = pygame.font.Font(None, 50)
        text = font.render('color', True, red)
        screen.blit(text, (460, 605))
        pygame.display.flip()

    def plus(self, a):
        self.speed += a

    def minus(self, a):
        self.speed -= a


gray = (120, 120, 120)
white = (255, 255, 255)
red = (255, 0, 0)


def change_color():
    pass


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('xonix')
    size1 = width1, height1 = 800, 700
    screen = pygame.display.set_mode(size1)
    size2 = width2, height2 = 780, 580
    running = True
    clock = pygame.time.Clock()
    pause = False
    speed = 1000
    ball = Ball(speed)
    while running:
        dt = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if 700 < x < 750 and 600 < y < 650:
                    ball.plus(100)
                if 600 < x < 650 and 600 < y < 650:
                    ball.minus(100)
                if 450 < x < 550 and 600 < y < 650:
                    gray = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                    red = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                    white = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        ball.update(dt)
        ball.draw(screen)

    pygame.quit()