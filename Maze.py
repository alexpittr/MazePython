import pygame
import time
pygame.init()
screen = pygame.display.set_mode((1024,768))
done = False
x = 85
y = 110
a = 920
b = 110
z = 475
k = 550
ts1 = time.time()
ts2 = time.time()
tol1 = 0
tol2 = 0
clock = pygame.time.Clock()
def lvl1():
    screen.fill((225, 225, 225))
    global x,y,a,b,ts1,ts2,tol1,tol2
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y += 3
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3
    if pressed[pygame.K_w]: b -= 3
    if pressed[pygame.K_s]: b += 3
    if pressed[pygame.K_d]: a += 3
    if pressed[pygame.K_a]: a -= 3
    Image1 = pygame.image.load("images.jpg").convert()
    pl1 = Image1.get_rect()
    pl1.center = (x, y)
    screen.blit(Image1, pl1)
    Image2 = pygame.image.load("saliba.jpg").convert()
    pl2 = Image1.get_rect()
    pl2.center = (a, b)
    screen.blit(Image2, pl2)
    w1 = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(-15, 0, 45, 700))
    w2 = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(30, 0, 1024, 50))
    w3 = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(1000, 0, 45, 700))
    w4 = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 700, 1024, 70))
    w5 = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(150, 35, 45, 500))
    w6 = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(325, 200, 45, 500))
    w7 = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(825, 35, 45, 500))
    w8 = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(650, 200, 45, 500))
    w9 = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(415, 70, 200, 60))
    fl = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(z, k, 60, 60))

    if pl1.colliderect(w1) or pl1.colliderect(w2) or pl1.colliderect(w3) or pl1.colliderect(w4) or pl1.colliderect(
            w5) or pl1.colliderect(w6) or pl1.colliderect(w7) or pl1.colliderect(w8) or pl1.colliderect(w9):
        if pressed[pygame.K_UP]: y += 4
        if pressed[pygame.K_DOWN]: y -= 4
        if pressed[pygame.K_LEFT]: x += 4
        if pressed[pygame.K_RIGHT]: x -= 4

    if pl2.colliderect(w1) or pl2.colliderect(w2) or pl2.colliderect(w3) or pl2.colliderect(w4) or pl2.colliderect(
            w5) or pl2.colliderect(w6) or pl2.colliderect(w7) or pl2.colliderect(w8) or pl2.colliderect(w9):
        if pressed[pygame.K_w]: b += 4
        if pressed[pygame.K_s]: b -= 4
        if pressed[pygame.K_d]: a -= 4
        if pressed[pygame.K_a]: a += 4

    if pl1.colliderect(fl):
        x = 70
        y = 70
        te1 = time.time()
        tol1 = round(te1 - ts1, 2)
        ts1 = time.time()

    if pl2.colliderect(fl):
        a = 900
        b = 70
        te2 = time.time()
        tol2 = round(te2 - ts2, 2)
        ts2 = time.time()

    Font1 = pygame.font.SysFont("ariel", 20, True, True)
    Time1 = Font1.render("Time for pl1:" + str(tol1), True, (0, 0, 0))
    screen.blit(Time1, (100, 650))

    Font2 = pygame.font.SysFont("ariel", 20, True, True)
    Time2 = Font2.render("Time for pl2:" + str(tol2), True, (0, 0, 0))
    screen.blit(Time2, (817, 650))

    Font = pygame.font.SysFont("ariel", 50, True, True)
    Title = Font.render("Maze 1v1", True, (0, 0, 255))
    screen.blit(Title, (30, 0))

    Start1 = Font.render("pl1", True, (0, 0, 0))
    screen.blit(Start1, (70, 130))

    Start2 = Font.render("pl2", True, (0, 0, 0))
    screen.blit(Start2, (900, 130))

    Finish = Font.render("finish line", True, (0, 0, 0))
    screen.blit(Finish, (415, 625))

def lvl2():
    screen.fill((225, 225, 225))
    global x,y,a,b,ts1,ts2,tol1,tol2
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y += 3
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3
    if pressed[pygame.K_w]: b -= 3
    if pressed[pygame.K_s]: b += 3
    if pressed[pygame.K_d]: a += 3
    if pressed[pygame.K_a]: a -= 3
    Image1 = pygame.image.load("images.jpg").convert()
    pl1 = Image1.get_rect()
    pl1.center = (x, y)
    screen.blit(Image1, pl1)
    Image2 = pygame.image.load("saliba.jpg").convert()
    pl2 = Image1.get_rect()
    pl2.center = (a, b)
    screen.blit(Image2, pl2)
    w1 = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(-15, 0, 45, 700))
    w2 = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(30, 0, 1024, 50))
    w3 = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(1000, 0, 45, 700))
    w4 = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 700, 1024, 70))
    w5 = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(30, 195, 350, 60))
    w6 = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(125, 350, 350, 60))
    w7 = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(200, 350, 60, 275))
    w8 = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, 0, 0))
    w9 = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(475, -50, 60, 555))
    w10 = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, 0, 0))
    fl = pygame.draw.rect(screen, (50,50, 50), pygame.Rect(z, k, 60, 60))

    if pl1.colliderect(w1) or pl1.colliderect(w2) or pl1.colliderect(w3) or pl1.colliderect(w4) or pl1.colliderect(
            w5) or pl1.colliderect(w6) or pl1.colliderect(w7) or pl1.colliderect(w8) or pl1.colliderect(w9):
        if pressed[pygame.K_UP]: y += 4
        if pressed[pygame.K_DOWN]: y -= 4
        if pressed[pygame.K_LEFT]: x += 4
        if pressed[pygame.K_RIGHT]: x -= 4

    if pl2.colliderect(w1) or pl2.colliderect(w2) or pl2.colliderect(w3) or pl2.colliderect(w4) or pl2.colliderect(
            w5) or pl2.colliderect(w6) or pl2.colliderect(w7) or pl2.colliderect(w8) or pl2.colliderect(w9):
        if pressed[pygame.K_w]: b += 4
        if pressed[pygame.K_s]: b -= 4
        if pressed[pygame.K_d]: a -= 4
        if pressed[pygame.K_a]: a += 4

    if pl1.colliderect(fl):
        x = 70
        y = 70
        te1 = time.time()
        tol1 = round(te1 - ts1, 2)
        ts1 = time.time()

    if pl2.colliderect(fl):
        a = 900
        b = 70
        te2 = time.time()
        tol2 = round(te2 - ts2, 2)
        ts2 = time.time()

    Font1 = pygame.font.SysFont("ariel", 20, True, True)
    Time1 = Font1.render("Time for pl1:" + str(tol1), True, (0, 0, 0))
    screen.blit(Time1, (100, 650))

    Font2 = pygame.font.SysFont("ariel", 20, True, True)
    Time2 = Font2.render("Time for pl2:" + str(tol2), True, (0, 0, 0))
    screen.blit(Time2, (817, 650))

    Font = pygame.font.SysFont("ariel", 50, True, True)
    Title = Font.render("Maze 1v1", True, (0, 0, 255))
    screen.blit(Title, (30, 0))

    Start1 = Font.render("pl1", True, (0, 0, 0))
    screen.blit(Start1, (70, 130))

    Start2 = Font.render("pl2", True, (0, 0, 0))
    screen.blit(Start2, (900, 130))

    Finish = Font.render("finish line", True, (0, 0, 0))
    screen.blit(Finish, (415, 625))



while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    lvl1()
    pygame.display.flip()
    clock.tick(60)
