from camera import Camera
from settings import *

#inheriting from the superclass "Camera"
class Player(Camera):
    def __init__(self, app, position=PLAYER_POS, yaw=-90, pitch=0):
        

        #initialising pygame joysticks 
        pg.joystick.init()

        #collecting all current joysticks
        self.joysticks = [pg.joystick.Joystick(x) for x in range(pg.joystick.get_count())]
        self.mouseSens, self.controllerSens = self.profile_retreiver()

        #if any joysticks exist then initialise controller functionality 
        if self.joysticks:
            self.controller = controller = self.joysticks[0]
            self.controller.init()

        #inheriting all the attributes and methods from the camera class 
        super().__init__(position, yaw, pitch)

    def update(self):

        #update the keyboard in
        self.keyboard_control()
        self.mouse_control()

        #handling the event that no joysticks have been plugged in as to not throw an error 
        if self.joysticks:
            self.controller_control()

        super().update()

    #controls the camera movement
    def mouse_control(self):

        #return instances of mouse movement 
        mouse_dx, mouse_dy = pg.mouse.get_rel()

        #if mouse direction -> corresponding movement direction 
        if mouse_dx:
            self.rotate_yaw(delta_x=mouse_dx * self.mouseSens)
        if mouse_dy:
            self.rotate_pitch(delta_y=mouse_dy * self.mouseSens)

    #returns the mouse sensitivity and controller sensitivity written in the file "savedSettings" and their corresponding prfile settings saved in "settings.py"
    def profile_retreiver(self):
        with open ("textures/DAT/savedSettings.txt", "r") as f: 
            filedata = f.read()

        #parsing data
        mouseProfile = filedata[filedata.find("Mo") + 19: filedata.find("Co")].strip()
        controllerProfile = filedata[filedata.find("Co") + 25:].strip()

        if mouseProfile == "Low":   mouseProfile = LOW_MGAMESENSE
        elif mouseProfile == "Medium":   mouseProfile = MEDIUM_MGAMESENSE
        elif mouseProfile == "High":   mouseProfile = HIGH_MGAMESENSE

        if controllerProfile == "Low":   controllerProfile = LOW_CGAMESENSE
        elif controllerProfile == "Medium":   controllerProfile = MEDIUM_CGAMESENSE
        elif controllerProfile == "High":   controllerProfile = HIGH_CGAMESENSE

        return mouseProfile, controllerProfile
        
    #controls the player movement 
    def keyboard_control(self):

        #returns instances of keys being pressed 
        key_state = pg.key.get_pressed()

        #calculating velocity 
        vel = PLAYER_SPEED * self.app.delta_time

        #if mouse key -> corresponding movement direction
        if key_state[pg.K_w]:
            self.move_forwards(vel)
        if key_state[pg.K_s]:
            self.move_back(vel)
        if key_state[pg.K_d]:
            self.move_right(vel)
        if key_state[pg.K_a]:
            self.move_left(vel)
        if key_state[pg.K_q]:
            self.move_up(vel)
        if key_state[pg.K_e]:
            self.move_down(vel)

    #controller movement 
    def controller_control(self):
         
         #calculating velocity 
         vel = PLAYER_SPEED * self.app.delta_time

         #returning corresponding joystick axis instances of movement 
         x_axis_movement = self.controller.get_axis(0)
         y_axis_movement = self.controller.get_axis(1)
         x_axis_look_around = self.controller.get_axis(2)
         y_axis_look_around = self.controller.get_axis(3)

         #determine the direction based on the axes values
         if abs(x_axis_movement) > 0.1 or abs(y_axis_movement) > 0.1:
            if x_axis_movement > 0:
                self.move_right(vel)

            elif x_axis_movement< 0:
                 self.move_left(vel)

            if y_axis_movement > 0:
                 self.move_down(vel)
                 
            elif y_axis_movement < 0:
                 self.move_up(vel)

        #determine the direction based on the axes values
         if abs(x_axis_look_around) > 0.1 or abs(y_axis_look_around) > 0.1:
            if x_axis_look_around:
                self.rotate_yaw(delta_x=x_axis_look_around * self.controllerSens)

            if y_axis_look_around:
                self.rotate_pitch(delta_y=y_axis_look_around * self.controllerSens)
        
