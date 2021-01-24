import pygame as pg

FPS = 30

pg.init()
screen = pg.display.set_mode((640, 480))
clock = pg.time.Clock()

class Button:
    # Конструктор
    def __init__(self, color, x, y, width, height):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def draw(self, screen):
        pg.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
    
    def is_over(self):
        pass
    def jumpto(self):
        pass
    
RED = (255, 0, 0)
WHITE = (255, 255, 255)
btn_yes = Button(RED, 10, 10, 100, 30)
btn_no = Button(RED, 160, 10, 100, 30)

running = True
while running:
    clock.tick(FPS)
    
    screen.fill(WHITE)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    btn_yes.draw(screen)
    btn_no.draw(screen)
    
    pg.display.update()
pg.quit()