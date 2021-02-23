import os
import sys
import pygame

pygame.init()
win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Путь рыцаря")
pygame.display.set_icon(pygame.image.load("textures/icon.bmp"))
FPS = 30
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()


def terminate():
    pygame.quit()
    sys.exit()


def load_image(name, color_key=None):
    fullname = os.path.join('textures', name)
    if not os.path.isfile(fullname):
        print(f'Файл с изображением \'{fullname}\' не найден')
        sys.exit()
    image = pygame.image.load(fullname)

    if color_key:
        image = image.convert()
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


def load_level(filename):
    filename = "" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    max_width = max(map(len, level_map))

    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('road_not_up', x, y)
            elif level[y][x] == 'g':
                Tile('road_up_left', x, y)
            elif level[y][x] == 'r':
                Tile('road_up_right', x, y)
            elif level[y][x] == 'l':
                Tile('road_left', x, y)
            elif level[y][x] == 'd':
                Tile('road_left_down', x, y)
            elif level[y][x] == 'u':
                Tile('road_right_down', x, y)
            elif level[y][x] == 'x':
                Tile('road_x', x, y)
            elif level[y][x] == '=':
                Tile('road=', x, y)
            elif level[y][x] == '#':
                Tile('block', x, y)
            elif level[y][x] == '0':
                Tile('nothing', x, y)
            elif level[y][x] == '@':
                Tile('road_not_up', x, y)
                new_player = Player(x, y)
    return new_player, x, y


tile_images = {
    'block': load_image('Objects/block.png'),
    'road=': load_image('Objects/road=.png'),
    'road]': load_image('Objects/road].png'),
    'road_all': load_image('Objects/road_all.png'),
    'road_left': load_image('Objects/road_left.png'),
    'road_left_down': load_image('Objects/road_left_down.png'),
    'road_not_down': load_image('Objects/road_not_down.png'),
    'road_not_up': load_image('Objects/road_not_up.png'),
    'road_right_down': load_image('Objects/road_right_down.png'),
    'road_up_left': load_image('Objects/road_up_left.png'),
    'road_up_right': load_image('Objects/road_up_right.png'),
    'road_x': load_image('Objects/road_x.png'),
    'road[': load_image('Objects/roaf[.png'),
    'nothing': load_image('Objects/nothing.png')
}
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

right, left, up, down, animCount = 0, 0, 0, 0, 0

playerStand = pygame.image.load('textures/Characters/pers_stand.png')

tile_width = tile_height = 50

font = pygame.font.SysFont(None, 20)


def move_hero(hero, movement):
    x, y = hero.pos
    if movement == "up":
        if y > 0 and level[y - 1][x] != '#' and y > 0 and level[y - 1][x] != '0':
            hero.move(x, y - 1)
    elif movement == "down":
        if y < level_y - 1 and level[y + 1][x] != '#' and y < level_y - 1 and level[y + 1][x] != '0':
            hero.move(x, y + 1)
    elif movement == "left":
        if x > 0 and level[y][x - 1] != '#' and x > 0 and level[y][x - 1] != '0':
            hero.move(x - 1, y)
    elif movement == "right":
        if x < level_x - 1 and level[y][x + 1] != '#' and x < level_x - 1 and level[y][x + 1] != '0':
            hero.move(x + 1, y)


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = playerStand
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)
        self.pos = pos_x, pos_y

    def move(self, x, y):
        self.pos = (x, y)
        self.rect = self.image.get_rect().move(
            tile_width * self.pos[0] + 15, tile_height * self.pos[1] + 5)


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
                tiles_group.draw(win)
                player_group.draw(win)
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


if __name__ == '__main__':
    player = None
    level = load_level('textures/level1.txt')
    player, level_x, level_y = generate_level(level)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                terminate()
            if keys[pygame.K_RIGHT]:
                move_hero(player, 'right')
                right, left, up, down = True, False, False, False
            elif keys[pygame.K_LEFT]:
                move_hero(player, 'left')
                right, left, up, down = False, True, False, False
            elif keys[pygame.K_UP]:
                move_hero(player, 'up')
                right, left, up, down = False, False, True, False
            elif keys[pygame.K_DOWN]:
                move_hero(player, 'down')
                right, left, up, down = False, False, False, True
            else:
                right, left, up, down = False, False, False, False
                animCount = 0
            win.fill(pygame.Color('white'))
        # main_menu()
        tiles_group.draw(win)
        player_group.draw(win)
        pygame.display.flip()
        clock.tick(FPS)
