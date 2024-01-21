import pygame
import math
import random


class Ball:
    def __init__(self, speed):
        self.x = 390
        self.y = 20
        self.angle = math.radians(random.randint(0, 360))
        self.speed = speed
        self.speed1 = speed

    def update(self, dt):
        self.x += self.speed * math.cos(self.angle) * dt
        self.y -= self.speed * math.sin(self.angle) * dt

        if self.x < 20 or self.x > width2:
            self.angle = 180 - self.angle
        if self.y < 20 or self.y > height2:
            self.angle = -self.angle

        for i in range(len(line_points) - 1):
            x1, y1 = line_points[i]
            x2, y2 = line_points[i + 1]
            distance = abs((y2 - y1) * self.x - (x2 - x1) * self.y + x2 * y1 - x1 * y2) / math.sqrt(
                (y2 - y1) ** 2 + (x2 - x1) ** 2)
            if distance <= 10:
                self.angle = math.pi - self.angle

    def draw(self, screen):
        screen.fill('black')
        pygame.draw.rect(screen, gray, (10, 10, size2[0], size2[1]))

        pygame.draw.circle(screen, white, (int(self.x), int(self.y)), 10)

        pygame.draw.rect(screen, white, (700, 600, 50, 50), 1)
        pygame.draw.rect(screen, white, (600, 600, 50, 50), 1)
        pygame.draw.rect(screen, white, (450, 600, 100, 50), 1)
        for i in itog_lines:
            if len(i) >= 2:
                pygame.draw.lines(screen, blue, False, i, 1)

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


class Point:    
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen

    def move(self, dx, dy):
        if 10 <= self.x + dx <= width2 + 10 and 10 <= self.y + dy <= height2 + 10:
            self.x += dx
            self.y += dy
            line_points.append((self.x, self.y))
            if self.x == 10 or self.y == 10 or self.x == width2 + 10 or self.y == height2 + 10:
                itog_lines.append(line_points)
                line_points.clear()


gray = (120, 120, 120)
white = (255, 255, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('xonix')
    size1 = width1, height1 = 800, 700
    screen = pygame.display.set_mode(size1)
    size2 = width2, height2 = 780, 580
    clock = pygame.time.Clock()
    pause = False
    speed = 1000
    itog_lines = []
    line_points = [(width1 // 2, 0)]
    itog_lines.append(line_points)
    ball = Ball(speed)
    point = Point(width1 // 2, 10, screen)
    running = True
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
                    yellow = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                    blue = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    point.move(-10, 0)
                elif event.key == pygame.K_RIGHT:
                    point.move(10, 0)
                elif event.key == pygame.K_UP:
                    point.move(0, -10)
                elif event.key == pygame.K_DOWN:
                    point.move(0, 10)
        ball.update(dt)
        ball.draw(screen)
        pygame.draw.circle(screen, yellow, (point.x, point.y), 5)
        pygame.display.flip()
    pygame.quit()