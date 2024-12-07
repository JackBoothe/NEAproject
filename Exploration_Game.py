#importing all the necessary libraries
from settings import *
import moderngl as mgl
import pygame as pg
import sys
from shader_program import ShaderProgram
from scene import Scene
from player import Player
import MainUIs

class VoxelEngine:
    def __init__(self):
        pg.init()

        #setting version of openGL to 3.3
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3) 
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)

        #disable the use of depricated functions
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE) 

        #setting the depth buffer to a size of 24bits
        pg.display.gl_set_attribute(pg.GL_DEPTH_SIZE, 24) 

        #opengl-renderable display + double buffer
        self.SCREEN = pg.display.set_mode(WIN_RES, flags=pg.OPENGL  | pg.DOUBLEBUF) 
        self.ctx = mgl.create_context()

        #Optimisation features + transparency
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.BLEND) 

        #garbage collection of unused objects
        self.ctx.gc_mode = "auto" 

        self.clock = pg.time.Clock()
        self.delta_time = 0
        self.time = 0

        pg.event.set_grab(True)
        pg.mouse.set_visible(False)
        pg.joystick.init()
        
        self.joysticks =  [pg.joystick.Joystick(x) for x in range(pg.joystick.get_count())]

        self.is_running = True
        self.on_init()

    def on_init(self):

        #occurs once when the prgram starts
        self.player = Player(self)
        self.shader_program = ShaderProgram(self)
        self.scene = Scene(self)

    def update(self):

        #occurs every cycle and calls all the other python files
        
        self.player.update()
        self.shader_program.update()
        self.scene.update()
        self.delta_time = self.clock.tick()
        self.time = pg.time.get_ticks() * 0.001

        #understanding the performace speed and setting the current fps of the program to the application caption
        pg.display.set_caption(f"{self.clock.get_fps() :.0f}")

    #called to render objects to pygame display 
    def render(self):   
        self.ctx.clear(color=BG_COLOUR)
        self.scene.render()
        pg.display.flip()

    #exiting the program when "ESC" pressed
    def handle_events(self): 
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.QUIT()
                sys.exit()
            

    #occurs whilst the program is running 
    def run (self):
        while self.is_running:
            self.handle_events()
            self.update()
            self.render()
        pg.quit()
        sys.exit()


MainUIs.main_menu()
if __name__ == "__main__":
    app = VoxelEngine()
    app.run()






