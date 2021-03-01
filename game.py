import pygame
import sys

pygame.init()
win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.mouse.set_visible(False)

pygame.display.set_caption('Ant Knight Adventures')
pygame.display.set_icon(pygame.image.load("textures/icon.bmp"))

walkRight = [pygame.image.load('textures/Characters/pers_right.png'),  # загрузка спрайтов
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

playerStand = pygame.image.load('textures/Characters/pers_stand.png')

clock = pygame.time.Clock()

x = 1255  # коордитнаты, ширина, высота и скорость персонажа соответственно
y = 675
width = 20
height = 40
speed = 5
balls = []

right, left, up, down, animCount = False, False, False, False, 0  # персонаж стоит

last_move = 'right'  # последнее направление персонажа


def drawingWindow():
    global animCount
    win.blit(background, (0, 0))

    if animCount + 1 >= 60:
        animCount = 0

    if left:  # анимация передвижения
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

    for ball in balls:  # отрисовка мяча
        ball.draw(win)

    pygame.display.update()


def running():  # передвижение персонажа
    global right, left, up, down, animCount, x, y, last_move
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


def throwing():  # бросок мяча
    global x
    for ball in balls:
        if 1615 > ball.x > 0:
            ball.x += ball.vel
        else:
            balls.pop(balls.index(ball))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if last_move == 'right':
            facing = 1
        else:
            facing = -1
        if len(balls) < 1:
            balls.append(ball_throwing(round(x + width // 2), round(y + height // 2), 5, (255, 0, 0),
                                       facing))


def lvl1():  # первый уровень (TRIP 1)
    global x, y, right, left, up, down, animCount, background
    background = pygame.image.load('textures/k1lvl.png')
    run = True
    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        running()

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

        running()

        drawingWindow()
        if x == 10 and y == 800:
            print('Переход на третий уровень!')
            screen_before_lvl3()


def lvl3():
    global x, y, right, left, up, down, animCount, background, last_move
    background = pygame.image.load('textures/k5.png')
    last_move = 'right'
    run = True
    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        running()
        throwing()

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

        running()
        throwing()

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

        running()
        throwing()

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

        running()
        throwing()

        drawingWindow()
        if x == 1000 and y == 5:
            print('Переход на седьмой уровень!')
            screen_before_lvl7()


def lvl7():
    global x, y, right, left, up, down, animCount, background, last_move
    last_move = 'right'
    background = pygame.image.load('textures/paris.png')
    run = True
    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        running()
        throwing()

        drawingWindow()
        if x == 10 and y == 800:
            print('Концовка игры!')
            end_screen()


class ball_throwing:  # класс броска мяча
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 15 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def text_processing(txt_y, txt_x, title, type_font, coord, color):  # обработка текста
    text_coord = coord
    for line in title:
        string_rendered = type_font.render(line, 1, pygame.Color(color))
        intro_rect = string_rendered.get_rect()
        text_coord += txt_y
        intro_rect.top = text_coord
        intro_rect.x = txt_x
        text_coord += intro_rect.height
        win.blit(string_rendered, intro_rect)


def music_player(song):  # проигрывание музыки
    pygame.mixer.music.load(song)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)


def start_screen():  # начальное меню
    music_player('lvl12.wav')
    name_text = ["Ant Knight Adventures"]
    game_quit_text = ["Чтобы закрыть ИГРУ нажмите на escape."]
    win.fill(pygame.Color('black'))
    font0 = pygame.font.Font(None, 100)
    font1 = pygame.font.Font(None, 50)
    font2 = pygame.font.Font(None, 30)
    count = 0
    text_processing(5, 10, name_text, font0, 5, 'red')
    text_processing(830, 20, game_quit_text, font2, 5, 'white')

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


def screen_before_lvl1():  # экран перед первым уровнем. на экране показывается информация и инструкция к уровню
    lvl_text = ["TRIP 1"]
    lvl_task_text = ["Освой управление и войди в дверь."]

    win.fill(pygame.Color('black'))
    font = pygame.font.Font(None, 30)
    font1 = pygame.font.Font(None, 50)
    text_processing(0, 10, lvl_text, font, 50, 'white')
    text_processing(40, 10, lvl_task_text, font, 50, 'white')

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
    lvl_text = ["TRIP 2"]
    lvl_task_text = ["Найди секретную дверь, и мы с тобой отправимся в путешествие!"]

    win.fill(pygame.Color('black'))
    font = pygame.font.Font(None, 30)
    font1 = pygame.font.Font(None, 50)
    text_processing(0, 10, lvl_text, font, 50, 'white')
    text_processing(40, 10, lvl_task_text, font, 50, 'white')

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
    music_player('lvl3.wav')
    lvl_text = ["TRIP 3"]
    lvl_task_text = ['Начинаем путешествие! Первое место - Мечеть "Сердце Чечни" в Грозном!']
    lvl_task_text2 = [
        'У тебя появились новые способности - бросок мяча и левитация! Кроме просмотра, ты можешь играть!']
    lvl_task_text3 = ['Чтобы бросить мяч нажми на "пробел".']
    lvl_task_text4 = ['Теперь в каждом путешествии ты должен находить секретные двери, чтобы пройти дальше.']

    win.fill(pygame.Color('black'))
    font = pygame.font.Font(None, 30)
    font1 = pygame.font.Font(None, 50)
    text_processing(0, 10, lvl_text, font, 50, 'white')
    text_processing(50, 10, lvl_task_text, font, 50, 'white')
    text_processing(90, 10, lvl_task_text2, font, 50, 'white')
    text_processing(130, 10, lvl_task_text3, font, 50, 'white')
    text_processing(170, 10, lvl_task_text4, font, 50, 'white')
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
    music_player('moscow.wav')
    lvl_text = ["TRIP 4"]
    lvl_task_text = ['Теперь мы перемещаемся на "Красную площадь" - главную площадь Москвы!']

    win.fill(pygame.Color('black'))
    font = pygame.font.Font(None, 30)
    font1 = pygame.font.Font(None, 50)
    text_processing(0, 10, lvl_text, font, 50, 'white')
    text_processing(40, 10, lvl_task_text, font, 50, 'white')

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
    music_player('pizan_bash.wav')
    lvl_text = ["TRIP 5"]
    lvl_task_text = ['Пиза - город, в котором находится самая известная колокольная башня в мире - Пизанская башня!']

    win.fill(pygame.Color('black'))
    font = pygame.font.Font(None, 30)
    font1 = pygame.font.Font(None, 50)
    text_processing(0, 10, lvl_text, font, 50, 'white')
    text_processing(40, 10, lvl_task_text, font, 50, 'white')

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
    music_player('london.wav')
    lvl_text = ["TRIP 6"]
    lvl_task_text = ['Биг Бен - знаменитая на весь мир часовая башня в Лондоне!']

    win.fill(pygame.Color('black'))
    font = pygame.font.Font(None, 30)
    font1 = pygame.font.Font(None, 50)
    text_processing(0, 10, lvl_text, font, 50, 'white')
    text_processing(40, 10, lvl_task_text, font, 50, 'white')

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


def screen_before_lvl7():
    music_player('lvl7.wav')
    lvl_text = ["TRIP 7"]
    lvl_task_text = ['И наконец - Эйфелева Башня - самая узнаваемая архитектурная достопримечательность Парижа!']

    win.fill(pygame.Color('black'))
    font = pygame.font.Font(None, 30)
    font1 = pygame.font.Font(None, 50)
    text_processing(0, 10, lvl_text, font, 50, 'white')
    text_processing(40, 10, lvl_task_text, font, 50, 'white')

    count = 0
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    lvl7()
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


def end_screen():  # конечный экран
    name_text = ["Ant Knight Adventures"]
    game_end_text = ["Наше с Вами путешествие закончилось. С Вами было очень интересно! Спасибо!"]
    game_quit_text = ['Нажмите на enter, чтобы запустить игру с начала!']
    win.fill(pygame.Color('black'))
    font0 = pygame.font.Font(None, 100)
    font1 = pygame.font.Font(None, 50)
    font2 = pygame.font.Font(None, 30)
    text_processing(0, 5, name_text, font0, 5, 'red')
    text_processing(100, 5, game_end_text, font1, 5, 'plum4')
    text_processing(830, 20, game_quit_text, font2, 5, 'white')

    count = 0
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
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


start_screen()  # запуск игры начинается с начального меню
pygame.quit()
