import pygame

pygame.init()
win = pygame.display.set_mode((1280, 720))

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

x = 50
y = 50
widht = 20
height = 40
speed = 5

right, left, up, down, animCount = False, False, False, False, 0


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


run = True
while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        right, left, up, down = False, True, False, False
    elif keys[pygame.K_RIGHT] and x < 1280 - widht - 5:
        x += speed
        right, left, up, down = True, False, False, False
    elif keys[pygame.K_UP] and y > 5:
        y -= speed
        right, left, up, down = False, False, True, False
    elif keys[pygame.K_DOWN] and y < 720 - height - 5:
        y += speed
        right, left, up, down = False, False, False, True
    else:
        right, left, up, down, animCount = False, False, False, False, 0

    drawingWindow()

pygame.quit()
