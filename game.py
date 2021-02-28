import pygame
import sys

pygame.init()
win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.mouse.set_visible(False)

pygame.display.set_caption('Ant Knight Adventures')
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
bullets = []

right, left, up, down, animCount = False, False, False, False, 0

last_move = 'right'


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

    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()


def lvl1():
    global x, y, right, left, up, down, animCount, background
    background = pygame.image.load('textures/k1lvl.png')
    run = True
    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        if keys[pygame.K_a] and x > 10:
            x -= speed
            right, left, up, down = False, True, False, False
        elif keys[pygame.K_d] and x < 1590 - width - 5:
            x += speed
            right, left, up, down = True, False, False, False
        elif keys[pygame.K_w] and y > 5:
            y -= speed
            right, left, up, down = False, False, True, False
        elif keys[pygame.K_s] and y < 900 - height - 5:
            y += speed
            right, left, up, down = False, False, False, True
        else:
            right, left, up, down, animCount = False, False, False, False, 0

        drawingWindow()
        if x == 10 and y == 5:
            print('Переход на второй уровень!')
            screen_before_lvl2()


def lvl2():
    global x, y, right, left, up, down, animCount, background
    background = pygame.image.load('textures/k2.png')
    run = True
    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        if keys[pygame.K_a] and x > 10:
            x -= speed
            right, left, up, down = False, True, False, False
            last_move = 'left'
        elif keys[pygame.K_d] and x < 1590 - width - 5:
            x += speed
            right, left, up, down = True, False, False, False
            last_move = 'right'
        elif keys[pygame.K_w] and y > 5:
            y -= speed
            right, left, up, down = False, False, True, False
        elif keys[pygame.K_s] and y < 900 - height - 5:
            y += speed
            right, left, up, down = False, False, False, True
        else:
            right, left, up, down, animCount = False, False, False, False, 0

        drawingWindow()
        if x == 10 and y == 800:
            print('Переход на третий уровень!')
            screen_before_lvl3()


def lvl3():
    global x, y, right, left, up, down, animCount, background, last_move
    last_move = 'right'
    background = pygame.image.load('textures/k5.png')
    run = True
    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for bullet in bullets:
            if 1615 > bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            if last_move == 'right':
                facing = 1
            else:
                facing = -1
            if len(bullets) < 1:
                bullets.append(gun(round(x + width // 2), round(y + height // 2), 5, (255, 0, 0),
                                   facing))
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        if keys[pygame.K_a] and x > 10:
            x -= speed
            right, left, up, down = False, True, False, False
            last_move = 'left'
        elif keys[pygame.K_d] and x < 1590 - width - 5:
            x += speed
            right, left, up, down = True, False, False, False
            last_move = 'right'
        elif keys[pygame.K_w] and y > 5:
            y -= speed
            right, left, up, down = False, False, True, False
        elif keys[pygame.K_s] and y < 900 - height - 5:
            y += speed
            right, left, up, down = False, False, False, True
        else:
            right, left, up, down, animCount = False, False, False, False, 0

        drawingWindow()
        if x == 10 and y == 5:
            print('Переход на четвёртый уровень!')
            screen_before_lvl4()


def lvl4():
    global x, y, right, left, up, down, animCount, background, last_move
    last_move = 'right'
    background = pygame.image.load('textures/red_sq.png')
    run = True
    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for bullet in bullets:
            if 1615 > bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            if last_move == 'right':
                facing = 1
            else:
                facing = -1
            if len(bullets) < 1:
                bullets.append(gun(round(x + width // 2), round(y + height // 2), 5, (255, 0, 0),
                                   facing))
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        if keys[pygame.K_a] and x > 10:
            x -= speed
            right, left, up, down = False, True, False, False
            last_move = 'left'
        elif keys[pygame.K_d] and x < 1590 - width - 5:
            x += speed
            right, left, up, down = True, False, False, False
            last_move = 'right'
        elif keys[pygame.K_w] and y > 5:
            y -= speed
            right, left, up, down = False, False, True, False
        elif keys[pygame.K_s] and y < 900 - height - 5:
            y += speed
            right, left, up, down = False, False, False, True
        else:
            right, left, up, down, animCount = False, False, False, False, 0

        drawingWindow()
        if x == 10 and y == 800:
            print('Переход на пятый уровень!')
            screen_before_lvl5()


def lvl5():
    global x, y, right, left, up, down, animCount, background, last_move
    last_move = 'right'
    background = pygame.image.load('textures/pizanskaya.png')
    run = True
    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for bullet in bullets:
            if 1615 > bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            if last_move == 'right':
                facing = 1
            else:
                facing = -1
            if len(bullets) < 1:
                bullets.append(gun(round(x + width // 2), round(y + height // 2), 5, (255, 0, 0),
                                   facing))
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        if keys[pygame.K_a] and x > 10:
            x -= speed
            right, left, up, down = False, True, False, False
            last_move = 'left'
        elif keys[pygame.K_d] and x < 1590 - width - 5:
            x += speed
            right, left, up, down = True, False, False, False
            last_move = 'right'
        elif keys[pygame.K_w] and y > 5:
            y -= speed
            right, left, up, down = False, False, True, False
        elif keys[pygame.K_s] and y < 900 - height - 5:
            y += speed
            right, left, up, down = False, False, False, True
        else:
            right, left, up, down, animCount = False, False, False, False, 0

        drawingWindow()
        if x == 100 and y == 5:
            print('Переход на шестой уровень!')
            screen_before_lvl6()


def lvl6():
    global x, y, right, left, up, down, animCount, background, last_move
    last_move = 'right'
    background = pygame.image.load('textures/bb.png')
    run = True
    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for bullet in bullets:
            if 1615 > bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            if last_move == 'right':
                facing = 1
            else:
                facing = -1
            if len(bullets) < 1:
                bullets.append(gun(round(x + width // 2), round(y + height // 2), 5, (255, 0, 0),
                                   facing))
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        if keys[pygame.K_a] and x > 10:
            x -= speed
            right, left, up, down = False, True, False, False
            last_move = 'left'
        elif keys[pygame.K_d] and x < 1590 - width - 5:
            x += speed
            right, left, up, down = True, False, False, False
            last_move = 'right'
        elif keys[pygame.K_w] and y > 5:
            y -= speed
            right, left, up, down = False, False, True, False
        elif keys[pygame.K_s] and y < 900 - height - 5:
            y += speed
            right, left, up, down = False, False, False, True
        else:
            right, left, up, down, animCount = False, False, False, False, 0

        drawingWindow()


class gun:
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 15 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def start_screen():
    name_text = ["Ant Knight Adventures"]
    game_quit_text = ["Чтобы закрыть ИГРУ нажмите на escape."]
    win.fill(pygame.Color('black'))
    font0 = pygame.font.Font(None, 100)
    font1 = pygame.font.Font(None, 50)
    font2 = pygame.font.Font(None, 30)
    text_coord = 5
    count = 0
    for line in name_text:
        string_rendered = font0.render(line, 1, pygame.Color('red'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 5
        text_coord += intro_rect.height
        win.blit(string_rendered, intro_rect)
    for line in game_quit_text:
        string_rendered = font2.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 780
        intro_rect.top = text_coord
        intro_rect.x = 20
        text_coord += intro_rect.height
        win.blit(string_rendered, intro_rect)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print('Первый уровень!')
                    screen_before_lvl1()
        if count == 0:
            win.blit(font1.render("PRESS ENTER", True, pygame.Color('black')), [1240, 800])
            win.blit(font1.render("TO START PLAYING", True, pygame.Color('black')), [1210, 830])
            count = 1
        else:
            win.blit(font1.render("PRESS ENTER", True, pygame.Color('white')), [1240, 800])
            win.blit(font1.render("TO START PLAYING", True, pygame.Color('white')), [1210, 830])
            count = 0
        pygame.display.flip()
        clock.tick(1)


def screen_before_lvl1():
    lvl1_text = ["TRIP 1"]
    lvl1_task_text = ["Освой управление и войди в дверь."]

    win.fill(pygame.Color('black'))
    font = pygame.font.Font(None, 30)
    font1 = pygame.font.Font(None, 50)
    text_coord = 50
    for line in lvl1_text:
        string_rendered1 = font.render(line, 1, pygame.Color('white'))
        intro_rect1 = string_rendered1.get_rect()
        text_coord += 10
        intro_rect1.top = text_coord
        intro_rect1.x = 10
        text_coord += intro_rect1.height
        win.blit(string_rendered1, intro_rect1)
    for line in lvl1_task_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 20
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        win.blit(string_rendered, intro_rect)

    count = 0
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    lvl1()
        if count == 0:
            win.blit(font1.render("PRESS ENTER", True, pygame.Color('black')), [1240, 800])
            win.blit(font1.render("TO START PLAYING", True, pygame.Color('black')), [1210, 830])
            count = 1
        else:
            win.blit(font1.render("PRESS ENTER", True, pygame.Color('white')), [1240, 800])
            win.blit(font1.render("TO START PLAYING", True, pygame.Color('white')), [1210, 830])
            count = 0
        pygame.display.flip()
        clock.tick(1)


def screen_before_lvl2():
    lvl1_text = ["TRIP 2"]
    lvl1_task_text = ["Найди секретную дверь, и мы с тобой отправимся в путешествие!"]

    win.fill(pygame.Color('black'))
    font = pygame.font.Font(None, 30)
    font1 = pygame.font.Font(None, 50)
    text_coord = 50
    for line in lvl1_text:
        string_rendered1 = font.render(line, 1, pygame.Color('white'))
        intro_rect1 = string_rendered1.get_rect()
        text_coord += 10
        intro_rect1.top = text_coord
        intro_rect1.x = 10
        text_coord += intro_rect1.height
        win.blit(string_rendered1, intro_rect1)
    for line in lvl1_task_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 20
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        win.blit(string_rendered, intro_rect)

    count = 0
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    lvl2()
        if count == 0:
            win.blit(font1.render("PRESS ENTER", True, pygame.Color('black')), [1240, 800])
            win.blit(font1.render("TO START PLAYING", True, pygame.Color('black')), [1210, 830])
            count = 1
        else:
            win.blit(font1.render("PRESS ENTER", True, pygame.Color('white')), [1240, 800])
            win.blit(font1.render("TO START PLAYING", True, pygame.Color('white')), [1210, 830])
            count = 0
        pygame.display.flip()
        clock.tick(1)


def screen_before_lvl3():
    lvl1_text = ["TRIP 3"]
    lvl1_task_text = ['Начинаем путешествие! Первое место - Мечеть "Сердце Чечни" в Грозном!']
    lvl_task_text2 = ['У тебя появилась новая способность - бросок мяча! Кроме просмотра, ты можешь играть!']
    lvl_task_text3 = ['Чтобы бросить мяч нажми на "пробел".']

    win.fill(pygame.Color('black'))
    font = pygame.font.Font(None, 30)
    font1 = pygame.font.Font(None, 50)
    text_coord = 50
    for line in lvl1_text:
        string_rendered1 = font.render(line, 1, pygame.Color('white'))
        intro_rect1 = string_rendered1.get_rect()
        text_coord += 10
        intro_rect1.top = text_coord
        intro_rect1.x = 10
        text_coord += intro_rect1.height
        win.blit(string_rendered1, intro_rect1)
    for line in lvl1_task_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 20
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        win.blit(string_rendered, intro_rect)
    for line in lvl_task_text2:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 30
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        win.blit(string_rendered, intro_rect)
    for line in lvl_task_text3:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 40
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        win.blit(string_rendered, intro_rect)
    count = 0
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    lvl3()
        if count == 0:
            win.blit(font1.render("PRESS ENTER", True, pygame.Color('black')), [1240, 800])
            win.blit(font1.render("TO START PLAYING", True, pygame.Color('black')), [1210, 830])
            count = 1
        else:
            win.blit(font1.render("PRESS ENTER", True, pygame.Color('white')), [1240, 800])
            win.blit(font1.render("TO START PLAYING", True, pygame.Color('white')), [1210, 830])
            count = 0
        pygame.display.flip()
        clock.tick(1)


def screen_before_lvl4():
    lvl1_text = ["TRIP 4"]
    lvl1_task_text = ['Теперь мы перемещаемся на "Красную площадь" - главную площадь Москвы!']

    win.fill(pygame.Color('black'))
    font = pygame.font.Font(None, 30)
    font1 = pygame.font.Font(None, 50)
    text_coord = 50
    for line in lvl1_text:
        string_rendered1 = font.render(line, 1, pygame.Color('white'))
        intro_rect1 = string_rendered1.get_rect()
        text_coord += 10
        intro_rect1.top = text_coord
        intro_rect1.x = 10
        text_coord += intro_rect1.height
        win.blit(string_rendered1, intro_rect1)
    for line in lvl1_task_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 20
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        win.blit(string_rendered, intro_rect)

    count = 0
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    lvl4()
        if count == 0:
            win.blit(font1.render("PRESS ENTER", True, pygame.Color('black')), [1240, 800])
            win.blit(font1.render("TO START PLAYING", True, pygame.Color('black')), [1210, 830])
            count = 1
        else:
            win.blit(font1.render("PRESS ENTER", True, pygame.Color('white')), [1240, 800])
            win.blit(font1.render("TO START PLAYING", True, pygame.Color('white')), [1210, 830])
            count = 0
        pygame.display.flip()
        clock.tick(1)


def screen_before_lvl5():
    lvl1_text = ["TRIP 5"]
    lvl1_task_text = ['Пиза - город, в котором находится самая известная колокольная башня в мире - Пизанская башня!']

    win.fill(pygame.Color('black'))
    font = pygame.font.Font(None, 30)
    font1 = pygame.font.Font(None, 50)
    text_coord = 50
    for line in lvl1_text:
        string_rendered1 = font.render(line, 1, pygame.Color('white'))
        intro_rect1 = string_rendered1.get_rect()
        text_coord += 10
        intro_rect1.top = text_coord
        intro_rect1.x = 10
        text_coord += intro_rect1.height
        win.blit(string_rendered1, intro_rect1)
    for line in lvl1_task_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 20
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        win.blit(string_rendered, intro_rect)

    count = 0
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    lvl5()
        if count == 0:
            win.blit(font1.render("PRESS ENTER", True, pygame.Color('black')), [1240, 800])
            win.blit(font1.render("TO START PLAYING", True, pygame.Color('black')), [1210, 830])
            count = 1
        else:
            win.blit(font1.render("PRESS ENTER", True, pygame.Color('white')), [1240, 800])
            win.blit(font1.render("TO START PLAYING", True, pygame.Color('white')), [1210, 830])
            count = 0
        pygame.display.flip()
        clock.tick(1)


def screen_before_lvl6():
    lvl1_text = ["TRIP 6"]
    lvl1_task_text = ['Биг Бен - знаменитая на весь мир часовая башня в Лондоне!']

    win.fill(pygame.Color('black'))
    font = pygame.font.Font(None, 30)
    font1 = pygame.font.Font(None, 50)
    text_coord = 50
    for line in lvl1_text:
        string_rendered1 = font.render(line, 1, pygame.Color('white'))
        intro_rect1 = string_rendered1.get_rect()
        text_coord += 10
        intro_rect1.top = text_coord
        intro_rect1.x = 10
        text_coord += intro_rect1.height
        win.blit(string_rendered1, intro_rect1)
    for line in lvl1_task_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 20
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        win.blit(string_rendered, intro_rect)

    count = 0
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    lvl6()
        if count == 0:
            win.blit(font1.render("PRESS ENTER", True, pygame.Color('black')), [1240, 800])
            win.blit(font1.render("TO START PLAYING", True, pygame.Color('black')), [1210, 830])
            count = 1
        else:
            win.blit(font1.render("PRESS ENTER", True, pygame.Color('white')), [1240, 800])
            win.blit(font1.render("TO START PLAYING", True, pygame.Color('white')), [1210, 830])
            count = 0
        pygame.display.flip()
        clock.tick(1)


start_screen()
pygame.quit()
