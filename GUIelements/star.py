import pygame as pg
from settings import * 

class Star(pg.sprite.Sprite):
    def __init__(self, x, y, rating):
        super().__init__()

        #defining attributes
        self.rating = rating
        self.original_image = pg.Surface((STAR_SIZE, STAR_SIZE), pg.SRCALPHA)

        #star shpae in pygame 
        pg.draw.polygon(self.original_image, STAR_COLOR, [(25, 0), (31, 19), (50, 19), (36, 31), (42, 50), (25, 38), (8, 50), (14, 31), (0, 19), (19, 19)])
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(center=(x, y))
        self.lit = False

    def toggle_lit(self, stars_group):
        #reset all stars to unlit 
        for star in stars_group:
            star.lit = False
            star.image = star.original_image.copy()

        #toggle selected star and stars to its left
        for s in stars_group:
            #so if a star's rating is less than the selected star then this means it is to the left and should be highlighted 
            if s.rating <= self.rating:
                s.lit = True
                pg.draw.polygon(s.image, LIT_STAR_COLOR, [(25, 0), (31, 19), (50, 19), (36, 31), (42, 50), (25, 38), (8, 50), (14, 31), (0, 19), (19, 19)])

   
