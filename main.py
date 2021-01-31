import pygame as pg
import random as rnd

FPS = 30

class Window:
    width = 640
    height = 480
    center_x = width/2
    center_y = height/2

pg.init()
screen = pg.display.set_mode((Window.width, Window.height))
clock = pg.time.Clock()

class Button:
    # Конструктор
    def __init__(self, color, x, y, width, height):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def draw(self, screen_):
        pg.draw.rect(screen_, self.color, (self.x, self.y, self.width, self.height))
    
    def is_over(self, mouse_x, mouse_y):
        return self.x <= mouse_x <= self.x + self.width and \
           self.y <= mouse_y <= self.y + self.height
    
    def jumpto(self, x, y):
        self.x = x
        self.y = y
    
RED = (255, 0, 0)
WHITE = (255, 255, 255)

Button.width = 80
Button.height = 30
distance_to_center_x = 30
view_x = Window.center_x - Button.width - distance_to_center_x
view_y = Window.center_y # px

btn_yes = Button(RED, view_x, view_y, Button.width, Button.height)
btn_no = Button(RED, view_x + Button.width + distance_to_center_x*2, \
                view_y, Button.width, Button.height)

running = True
while running:
    clock.tick(FPS)
    screen.fill(WHITE)
    
    list_events = pg.event.get() # Список событий программы
    for event in list_events:
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEMOTION:
            mouse_x, mouse_y = event.pos # Координаты мышки
            if btn_no.is_over(mouse_x, mouse_y): # Результат либо True, либо False
                new_x = rnd.randint(0, Window.width)
                new_y = rnd.randint(0, Window.height)
                btn_no.jumpto(new_x, new_y)

    btn_yes.draw(screen)
    btn_no.draw(screen)
    
    pg.display.update()

pg.quit()