import pygame
from time import sleep
from sys import exit
from tower import Tower


pygame.init()
pygame.display.set_caption("Ханойские башни")
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

game_done = False
framerate = 30

steps = 0 #количество ходов
disk_amount = 3 #количество колец
towers_midx = [120, 320, 520] # середина каждой башни
pointing_at = 0 #на какой башне стоит указатель
floating = False #взято ли кольцо в руку

#Цвета
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
gold = (239, 229, 51)
blue = (78,162,196) 
grey = (170, 170, 170)
green = (77, 206, 145)

#Функция для создания текста
def blit_text(screen, text, midtop, aa=True, font_name = None, size = None, color=(255,0,0)):
    font = pygame.font.SysFont(font_name, size)     
    font_surface = font.render(text, aa, color)
    font_rect = font_surface.get_rect()
    font_rect.midtop = midtop
    screen.blit(font_surface, font_rect)

def AI_or_not_menu_screen():
    global screen, game_done
    menu_done = False
    options = ["Рекурсивный","Итеративный","Решать самостоятельно"]
    algorithm = 0
    while not menu_done: 
        screen.fill(white)
        blit_text(screen, 'Ханойские башни', (323,122), font_name='sans serif', size=90, color=grey)
        blit_text(screen, 'Ханойские башни', (320,120), font_name='sans serif', size=90, color=gold)
        blit_text(screen, 'Используйте стрелки чтобы выбрать алгоритм:', (320, 220), font_name='sans serif', size=30, color=black)
        blit_text(screen, options[algorithm], (320, 260), font_name='sans serif', size=40, color=blue)
        blit_text(screen, 'Нажмите ENTER чтобы начать играть', (320, 320), font_name='sans_serif', size=30, color=black)
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    menu_done = True
                    game_done = True
                if event.key == pygame.K_RETURN:
                    menu_done = True
                if event.key in [pygame.K_RIGHT, pygame.K_UP]:
                    algorithm += 1
                    if algorithm > len(options) - 1:
                        algorithm = len(options) - 1
                if event.key in [pygame.K_LEFT, pygame.K_DOWN]:
                    algorithm -= 1
                    if algorithm < 0:
                        algorithm = 0
            if event.type == pygame.QUIT:
                menu_done = True
                game_done = True
        pygame.display.flip()
        clock.tick(60)
    return options[algorithm]

#Функция для вывода меню начала игры
def disk_menu_screen(): 
    global screen, disk_amount, game_done
    menu_done = False
    while not menu_done: 
        screen.fill(white)
        blit_text(screen, 'Ханойские башни', (323,122), font_name='sans serif', size=90, color=grey)
        blit_text(screen, 'Ханойские башни', (320,120), font_name='sans serif', size=90, color=gold)
        blit_text(screen, 'Используйте стрелки чтобы выбрать сложность:', (320, 220), font_name='sans serif', size=30, color=black)
        blit_text(screen, str(disk_amount), (320, 260), font_name='sans serif', size=40, color=blue)
        blit_text(screen, 'Нажмите ENTER чтобы начать играть', (320, 320), font_name='sans_serif', size=30, color=black)
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    menu_done = True
                    game_done = True
                if event.key == pygame.K_RETURN:
                    menu_done = True
                if event.key in [pygame.K_RIGHT, pygame.K_UP]:
                    disk_amount += 1
                    if disk_amount > 6:
                        disk_amount = 6
                if event.key in [pygame.K_LEFT, pygame.K_DOWN]:
                    disk_amount -= 1
                    if disk_amount < 1:
                        disk_amount = 1
            if event.type == pygame.QUIT:
                menu_done = True
                game_done = True
        pygame.display.flip()
        clock.tick(60)

#Функция для вывода результатов в конце игры
def game_over(): 
    global screen, steps
    screen.fill(white)
    min_steps = 2**disk_amount-1
    blit_text(screen, 'Победа!', (320, 200), font_name='sans serif', size=72, color=grey)
    blit_text(screen, 'Победа!', (322, 202), font_name='sans serif', size=72, color=gold)
    blit_text(screen, 'Количество ходов: '+str(steps), (320, 360), font_name='mono', size=30, color=black)
    blit_text(screen, 'Минимальное количество ходов: '+str(min_steps), (320, 390), font_name='mono', size=30, color=red)
    if min_steps==steps:
        blit_text(screen, 'Идеальное решение!', (320, 300), font_name='mono', size=26, color=green)
    pygame.display.flip()
    sleep(3) 
    pygame.quit()   
    exit()  

#Функция отрисовки башен
def draw_towers():
    global screen
    for xpos in range(40, 460+1, 200):
        pygame.draw.rect(screen, green, pygame.Rect(xpos, 400, 160 , 20))
        pygame.draw.rect(screen, grey, pygame.Rect(xpos+75, 200, 10, 200))

#Функция открисовки колец на башнях и кольца в руке
def draw_disks(current_disk = None):
    if not(current_disk is None):
        pygame.draw.rect(screen, blue, current_disk)
    height = 20
    y_pos = 397 - height
    for i in range(disk_amount):
        if(len(towers[0].disks) > i):
            r = get_disk_rect(towers[0].disks[i],towers_midx[0], y_pos)
            pygame.draw.rect(screen, blue, r)
        if(len(towers[1].disks) > i):
            r = get_disk_rect(towers[1].disks[i],towers_midx[1], y_pos)
            pygame.draw.rect(screen, blue, r)
        if(len(towers[2].disks) > i):
            r = get_disk_rect(towers[2].disks[i],towers_midx[2], y_pos)
            pygame.draw.rect(screen, blue, r)
        y_pos -= height+3

def get_disk_rect(disk, x_pos, y_pos):
    r = pygame.Rect(0,0, disk.size * 23, 20)
    r.midtop = (x_pos, y_pos)
    return r
    
#Функция отрисовки указателя
def draw_pointer():
    ptr_points = [(towers_midx[pointing_at]-7 ,440), (towers_midx[pointing_at]+7, 440), (towers_midx[pointing_at], 433)]
    pygame.draw.polygon(screen, red, ptr_points)
    return


def TowerOfHanoi_recursive(n , source, destination, auxiliary):
    global screen, steps
    if n==1:
        destination.add_disk(source.remove_disk())
        steps += 1
        draw_screen()
        sleep(0.5)
        return
    draw_screen()
    sleep(0.5)
    TowerOfHanoi_recursive(n-1, source, auxiliary, destination)
    destination.add_disk(source.remove_disk())
    steps += 1
    draw_screen()
    sleep(0.5)
    TowerOfHanoi_recursive(n-1, auxiliary, destination, source)
    if (n == disk_amount):
        sleep(1)
        game_over()

def TowerOfHanoi_iterative(n, source, auxiliary, destination):
    draw_screen()
    sleep(0.5)
    total_num_of_moves =int(pow(2, n) - 1)
    for i in range(1, total_num_of_moves + 1):
        if (i % 3 == 1):
            moveDisksBetweenTwoPoles(source, destination)
        elif (i % 3 == 2):
            moveDisksBetweenTwoPoles(source, auxiliary)
        elif (i % 3 == 0):
            moveDisksBetweenTwoPoles(auxiliary, destination)
    sleep(1)
    game_over()

def moveDisksBetweenTwoPoles(src, dest):
    global steps
    
    pole1TopDisk = src.remove_disk()
    pole2TopDisk = dest.remove_disk()
 
    if (pole1TopDisk is None):
        src.add_disk(pole2TopDisk)
    elif (pole2TopDisk is None):
        dest.add_disk(pole1TopDisk)  
    elif (pole1TopDisk > pole2TopDisk):
        src.add_disk(pole1TopDisk)
        src.add_disk(pole2TopDisk)
    else:
        dest.add_disk(pole2TopDisk)
        dest.add_disk(pole1TopDisk)
    steps+=1
    draw_screen()
    sleep(0.5)

def draw_screen():
    screen.fill(white)
    draw_towers()
    draw_disks()
    blit_text(screen, 'Количество ходов: '+str(steps), (320, 20), font_name='mono', size=30, color=black)
    pygame.display.flip()

         
disk_menu_screen()
a_tower = Tower(disk_amount, is_start_tower=True)
b_tower = Tower(disk_amount)
c_tower = Tower(disk_amount)
a_tower.fill()
towers = [a_tower, b_tower, c_tower]
current_disk = None
current_disk_rect = None
n =disk_amount
algorithm = AI_or_not_menu_screen()
if (algorithm == "Рекурсивный"):
    TowerOfHanoi_recursive(n, a_tower, b_tower, c_tower)
elif(algorithm == "Итеративный"):
    TowerOfHanoi_iterative(n, a_tower, b_tower, c_tower)
else:
#Основной игровой цикл
    while not game_done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_done = True
                if event.key == pygame.K_RIGHT:
                    pointing_at = (pointing_at+1)%3
                    if floating:
                        #если диск взят в руку
                        current_disk_rect = get_disk_rect(current_disk,towers_midx[pointing_at], 100)
                if event.key == pygame.K_LEFT:
                    pointing_at = (pointing_at-1)%3
                    if floating:
                        #если диск взят в руку
                        current_disk_rect = get_disk_rect(current_disk,towers_midx[pointing_at], 100)
                if event.key == pygame.K_UP and not floating:
                    current_disk = towers[pointing_at].remove_disk()
                    #Если мы взяли кольцо
                    if not(current_disk is None):
                        current_disk_rect = get_disk_rect(current_disk,towers_midx[pointing_at], 100)
                        floating = True
                        break
                if event.key == pygame.K_DOWN and floating:
                    success = towers[pointing_at].add_disk(current_disk)
                    #Если мы успешно положили кольцо
                    if(success):
                        floating = False
                        current_disk = None
                        current_disk_rect = None
                        steps += 1
                        break

        screen.fill(white)
        draw_towers()
        draw_disks(current_disk_rect)
        draw_pointer()
        blit_text(screen, 'Количество ходов: '+str(steps), (320, 20), font_name='mono', size=30, color=black)
        pygame.display.flip()
        if not floating:
            for tower in towers:
                if(tower.check_win()):
                    game_over()
        clock.tick(framerate)