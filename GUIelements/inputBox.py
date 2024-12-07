import pygame as pg
from settings import *

#IMPORTANT: THE MAJORITY OF THE CODE FOR THIS DYNAMIC BUTTON WAS COPIED - SEE BIBLIOGRAPHY FOR REFERENCE 
#although some of it has still been altered which is explained in development section 

class InputBox:

    def __init__(self, x, y, w, h, text='Enter task: '):

        #initialsing button attributes
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.update_text_surface()
        self.active = False

    def update_text_surface(self):
        self.txt_surface = pg.font.Font("textures/assets/font.ttf", 20).render(self.text, True, self.color)

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            self.handle_mouse_click(event.pos)
        elif event.type == pg.KEYDOWN:
            self.handle_key_down(event)
    
    #input box is clicked ->  highlighted 
    def handle_mouse_click(self, pos):
        self.active = self.rect.collidepoint(pos)
        self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE


    def handle_key_down(self, event):
        print("hi")
        if self.active:
            if event.key == pg.K_RETURN:
                pass
                #self.text = 'Enter task: '
                
            elif event.key == pg.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
            self.update_text_surface()

    def update(self):
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pg.draw.rect(screen, self.color, self.rect, 2)

