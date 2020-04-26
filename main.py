import pygame, random

pygame.init()
width = 800
height = 800
black = (0, 0, 0)
white = (255, 255, 255)
win = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
run = True
speed = .001


class Star:
    def __init__(self):
        self.x = random.randint(-width // 2, width // 2)
        self.y = random.randint(-height // 2, height // 2)
        self.z = 1
        self.r = 2
        self.color = white
        self.c = 0
        self.oldx = round(self.x + width // 2)
        self.oldy = round(self.y + height // 2)

    def move(self):
        self.oldx = round(self.x + width // 2)
        self.oldy = round(self.y + height // 2)

        self.z += speed
        self.x *= self.z
        self.y *= self.z

    def draw(self):
        x = round(self.x + width // 2)
        y = round(self.y + height // 2)

        if self.c <= 255:
            self.color = (self.c, self.c, self.c)
            self.c += 15

        pygame.draw.circle(win, self.color, (x, y), self.r)
        pygame.draw.line(win, self.color, (self.oldx, self.oldy), (x, y), self.r * 2)


counter = 0
stars = []
for i in range(800):
    stars.append(Star())

while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if counter >= 10:
        counter = 0
        if keys[pygame.K_UP]:
            speed += .001
        if keys[pygame.K_DOWN]:
            speed -= .001
    counter += 1

    newStars = 0
    win.fill(black)
    for s in stars:
        s.move()
        s.draw()
        if s.x > width or s.x < -width // 2 or s.y > height or s.y < -height // 2:
            stars.remove(s)
            newStars += 1

    for i in range(newStars):
        stars.append(Star())

    pygame.display.flip()
