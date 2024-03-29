import pygame
import math
import random


def calculate_area(points):
    area = 0
    n = len(points)

    for i in range(n):
        j = (i + 1) % n
        area += points[i][0] * points[j][1] - points[j][0] * points[i][1]

    area = abs(area) / 2

    return area


class Ball:
    def __init__(self, speed):
        self.x = 390
        self.y = 20
        self.angle = math.radians(random.randint(0, 360))
        self.speed = speed
        self.lives = 3
        self.k = 0

    def update(self, dt):
        self.x += self.speed * math.cos(self.angle) * dt
        self.y -= self.speed * math.sin(self.angle) * dt

        if self.x < 20 or self.x > width2:
            self.angle = math.radians(180) - self.angle
            self.x = 20 if self.x < 20 else width2
        if self.y < 20 or self.y > height2:
            self.angle = -self.angle
            self.y = 20 if self.y < 20 else height2

        if len(line_points) >= 2:
            for i in range(len(line_points) - 1):
                x1, y1 = line_points[i]
                x2, y2 = line_points[i + 1]
                x3, y3 = self.x, self.y
                if ((y1 < y3 < y2 and abs(x3 - x1 <= 10) or x1 < x3 < x2 and abs(y3 - y1 <= 10)) or
                        (y2 < y3 < y1 and abs(x3 - x1 <= 10) or x2 < x3 < x1 and abs(y3 - y1 <= 10))):
                    self.touch()

    def draw(self, screen):
        screen.fill('black')
        pygame.draw.rect(screen, gray, (10, 10, size2[0], size2[1]))

        pygame.draw.circle(screen, white, (int(self.x), int(self.y)), 10)

        pygame.draw.rect(screen, white, (700, 600, 50, 50), 1)
        pygame.draw.rect(screen, white, (600, 600, 50, 50), 1)
        pygame.draw.rect(screen, white, (450, 600, 100, 50), 1)

        for i in itog_lines:
            if len(i) >= 2:
                pygame.draw.lines(screen, green, False, i, 1)

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

        font = pygame.font.Font(None, 50)
        text = font.render('score: ' + str(score), True, red)
        screen.blit(text, (10, 605))
        pygame.display.flip()

        font = pygame.font.Font(None, 50)
        text = font.render('lives: ' + str(ball.lives), True, red)
        screen.blit(text, (250, 605))
        pygame.display.flip()

    def plus(self, a):
        self.speed += a

    def minus(self, a):
        self.speed -= a

    def touch(self):
        global line_points
        line_points.clear()
        point.x = width2 // 2
        point.y = 10
        line_points.append((point.x, point.y))
        ball.lives -= 1


class Point:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.moves = []

    def move(self, dx, dy):
        if 10 <= self.x + dx <= width2 + 10 and 10 <= self.y + dy <= height2 + 10:
            self.x += dx
            self.y += dy
            if len(line_points) >= 2 and self.moves[-1] == self.moves[-2]:
                line_points[-1] = (self.x, self.y)
            else:
                line_points.append((self.x, self.y))
        else:
            itog_lines.append(line_points)
            line_points.clear()
            global score
            global area
            area += calculate_area(line_points)
            print(area)
            score += round(area / (width2 * height2), 0)


gray = (120, 120, 120)
white = (255, 255, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('xonix')
    size1 = width1, height1 = 800, 700
    screen = pygame.display.set_mode(size1)
    size2 = width2, height2 = 780, 580
    clock = pygame.time.Clock()
    pause = False
    speed = 700
    itog_lines = []
    line_points = [(width1 // 2, 10)]
    itog_lines.append(line_points)
    ball = Ball(speed)
    area = 0
    point = Point(width1 // 2, 10, screen)
    running = True
    score = 0
    uroven = 1
    while running and ball.lives > 0:
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
                    green = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    point.moves.append('+')
                    point.move(-10, 0)
                elif event.key == pygame.K_RIGHT:
                    point.moves.append('+')
                    point.move(10, 0)
                elif event.key == pygame.K_UP:
                    point.moves.append('-')
                    point.move(0, -10)
                elif event.key == pygame.K_DOWN:
                    point.moves.append('-')
                    point.move(0, 10)
        if area / (width2 * height2) * 100 > 40:
            uroven += 1
            area = 0
            if uroven == 2:
                ball2 = Ball(screen)
            if uroven == 3:
                ball3 = Ball(screen)
        if uroven == 1:
            ball.update(dt)
            ball.draw(screen)
        elif uroven == 2:
            ball.update(dt)
            ball.draw(screen)
            ball2.update(dt)
            ball2.draw(screen)
        elif uroven == 3:
            ball.update(dt)
            ball.draw(screen)
            ball2.update(dt)
            ball2.draw(screen)
            ball3.update(dt)
            ball3.draw(screen)
        pygame.draw.circle(screen, yellow, (point.x, point.y), 5)
        pygame.display.flip()
    else:
        f = open('Результаты.txt')
        f.write('Очки:', str(score))
        f.close()
    pygame.quit()