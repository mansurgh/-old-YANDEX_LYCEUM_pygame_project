import pygame
import sys

pygame.init()
win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

pygame.display.set_caption('Рыцарь')
pygame.display.set_icon(pygame.image.load("textures/icon.bmp"))

walkRight = [pygame.image.load('textures/Characters/pers_right.png'),
             pygame.image.load('textures/Characters/pers_right2.png'),
             pygame.image.load('textures/Characters/pers_right3.png')]
walkLeft = [pygame.image.load('textures/Characters/pers_left.png'),
            pygame.image.load('textures/Characters/pers_left2.png'),
            pygame.image.load('textures/Characters/pers_left3.png')]
walkUp = [pygame.image.load('textures/Characters/pers_up.png'),
          pygame.image.load('textures/Characters/pers_up2.png'),
          pygame.image.load('textures/Characters/pers_up3.png')]
walkDown = [pygame.image.load('textures/Characters/pers_down.png'),
            pygame.image.load('textures/Characters/pers_stand.png'),
            pygame.image.load('textures/Characters/pers_down2.png')]

background = pygame.image.load('textures/first_karta.png')
playerStand = pygame.image.load('textures/Characters/pers_stand.png')

clock = pygame.time.Clock()

x = 1255
y = 675
width = 20
height = 40
speed = 5

right, left, up, down, animCount = False, False, False, False, 0

font = pygame.font.SysFont(None, 20)


def drawingWindow():
    global animCount
    win.blit(background, (0, 0))

    if animCount + 1 >= 60:
        animCount = 0

    if left:
        win.blit(walkLeft[animCount % 3], (x, y))
        animCount += 1
    elif right:
        win.blit(walkRight[animCount % 3], (x, y))
        animCount += 1
    elif up:
        win.blit(walkUp[animCount % 3], (x, y))
        animCount += 1
    elif down:
        win.blit(walkDown[animCount % 3], (x, y))
        animCount += 1
    else:
        win.blit(playerStand, (x, y))

    pygame.display.update()


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False


def main_menu():
    while True:

        win.fill((0, 0, 0))
        draw_text('main menu', font, (255, 255, 255), win, 20, 20)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(50, 100, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                drawingWindow()
        pygame.draw.rect(win, (255, 0, 0), button_1)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(30)


def lvl1():
    global x, y, right, left, up, down, animCount, background
    background = pygame.image.load('textures/first_karta.png')
    run = True
    while run:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        if keys[pygame.K_LEFT] and x > 10:
            x -= speed
            right, left, up, down = False, True, False, False
        elif keys[pygame.K_RIGHT] and x < 1590 - width - 5:
            x += speed
            right, left, up, down = True, False, False, False
        elif keys[pygame.K_UP] and y > 5:
            y -= speed
            right, left, up, down = False, False, True, False
        elif keys[pygame.K_DOWN] and y < 900 - height - 5:
            y += speed
            right, left, up, down = False, False, False, True
        else:
            right, left, up, down, animCount = False, False, False, False, 0

        # main_menu()
        drawingWindow()
        if x == 15 and y == 5:
            print('yes')
            lvl2()


def lvl2():
    global x, y, right, left, up, down, animCount, background
    background = pygame.image.load('textures/karta2.png')
    run = True
    while run:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        if keys[pygame.K_LEFT] and x > 10:
            x -= speed
            right, left, up, down = False, True, False, False
        elif keys[pygame.K_RIGHT] and x < 1590 - width - 5:
            x += speed
            right, left, up, down = True, False, False, False
        elif keys[pygame.K_UP] and y > 5:
            y -= speed
            right, left, up, down = False, False, True, False
        elif keys[pygame.K_DOWN] and y < 900 - height - 5:
            y += speed
            right, left, up, down = False, False, False, True
        else:
            right, left, up, down, animCount = False, False, False, False, 0

        # main_menu()
        drawingWindow()


lvl1()
pygame.quit()
