from GUIelements.button import Button
from GUIelements.inputBox import InputBox
from GUIelements.star import Star
from settings import *
import pygame as pg 

def preGameScreen(screen):
    pg.display.set_caption('Pomodoro') 
    
    pg.mouse.set_visible(True)
    running = True
    

    TASK = InputBox(400, 200, 200, 32)

    #initialising stars 
    stars_group = pg.sprite.Group([Star(900 + i * STAR_SPACING, 395, i + 1) for i in range(5)])
    selected_star = None
    TASKstarted = False

    #start button
    START_BUTTON = Button(image=pg.image.load("textures/assets/Graphics Rect.png"), pos=(1500, 840), 
                              text_input="Start", font=pg.font.Font("textures/assets/font.ttf", 20), base_color="#d7fcd4", hovering_color="White")

    #length header
    LENGTH_HIGH = Button(image=pg.image.load("textures/assets/Graphics Rect.png"), pos=(850, 300), 
                            text_input="45 mins", font=pg.font.Font("textures/assets/font.ttf", 20), base_color="#d7fcd4", hovering_color="White")
    LENGTH_MEDIUM = Button(image=pg.image.load("textures/assets/Graphics Rect.png"), pos=(1000, 300), 
                            text_input="30 mins", font=pg.font.Font("textures/assets/font.ttf", 20), base_color="#d7fcd4", hovering_color="White")
    LENGTH_LOW = Button(image=pg.image.load("textures/assets/Graphics Rect.png"), pos=(1150, 300), 
                            text_input="15 mins", font=pg.font.Font("textures/assets/font.ttf", 20), base_color="#d7fcd4", hovering_color="White")
    
    #length text
    LENGTH_TEXT = pg.font.Font("textures/assets/font.ttf", 20).render("Select task length", True, "#FFFFFF")
    LENGTH_RECT = LENGTH_TEXT.get_rect(center=(580, 300))
    LENGTH_BUTTONSET = [LENGTH_HIGH, LENGTH_MEDIUM, LENGTH_LOW]

    #screen header 
    TASK_TEXT = pg.font.Font("textures/assets/font.ttf", 45).render("Task selection screen:", True, "#FFFFFF")
    TASK_RECT = TASK_TEXT.get_rect(center=(800, 55))
        
    #difficulty header
    DIFFICULTY_TEXT = pg.font.Font("textures/assets/font.ttf", 20).render("Select task difficulty", True, "#FFFFFF")
    DIFFICULTY_RECT = DIFFICULTY_TEXT.get_rect(center=(620, 400))

    #back button to main menu 
    POMODORO_BACK = Button(image=None, pos=(120, 860), 
                            text_input="BACK", font=pg.font.Font("textures/assets/font.ttf", 50), base_color="White", hovering_color="Green")

    #not filling in all field text 
    ERROR_TEXT = pg.font.Font("textures/assets/font.ttf", 20).render("Please fill in all fields!", True, "#FF0000")
    ERROR_RECT = ERROR_TEXT.get_rect(center=(660, 150))
    EXCEPTION = False 

    selectedSet = None

                            
    while running == True:

        screen.fill("BLACK")
        pomoMousepos = pg.mouse.get_pos()

        #this if statement occurs when the TASKstarted variable == True. This occurs once all the task fields have been successfully entered and the user clicks the start button.
        if TASKstarted == True: 

            #studying text
            STUDYING_TEXT = pg.font.Font("textures/assets/font.ttf", 35).render(f"Get to work on your {TASK.text[12:]}!!", True, "#FF0000")
            STUDYING_RECT = STUDYING_TEXT.get_rect(center=(800, 250))

            #resetting the start button to display "restart"
            START_BUTTON = Button(image=pg.image.load("textures/assets/Graphics Rect.png"), pos=(1500, 840), 
                              text_input="Restart", font=pg.font.Font("textures/assets/font.ttf", 20), base_color="#d7fcd4", hovering_color="White")

            #calculating how much time has passed sice the start button has been clikced 
            current_time = pg.time.get_ticks()
            elapsed_time = current_time - start_time
            remaining_seconds = max(0, (target_time - elapsed_time) // 1000)
            remaining_minutes = remaining_seconds // 60
            remaining_seconds %= 60
            
            #timer text 
            TIMER_TEXT = pg.font.Font("textures/assets/font.ttf", 40).render(f"{remaining_minutes} : {remaining_seconds}", True, "#FFFFFF")
            TIMER_RECT = DIFFICULTY_TEXT.get_rect(center=(850, 300))

            screen.blit(TIMER_TEXT, TIMER_RECT)
            screen.blit(STUDYING_TEXT, STUDYING_RECT)

            #checking for button inputs 
            for button in [START_BUTTON, POMODORO_BACK]:
                button.changeColor(pomoMousepos)
                button.update(screen)

            #this breaks out of this while loop and returns "start" back to the main menu screen. When the main menu recieves this, it also exitts and the exploration game is loaded 
            if remaining_minutes == 0 and remaining_seconds == 0:
                return "start"
        
       #occurs before all task inputs have been successfully inputted and before the start button has been clicked 
        else: 
            
            #blitting all text obkjects to screen 
            screen.blit(TASK_TEXT, TASK_RECT)
            screen.blit(DIFFICULTY_TEXT, DIFFICULTY_RECT)
            screen.blit(LENGTH_TEXT, LENGTH_RECT)
            
            stars_group.update()
            stars_group.draw(screen)

            #when the user has not filled in all the fields correctly, this error text appears and prompts them to. 
            if EXCEPTION == True:
                screen.blit(ERROR_TEXT, ERROR_RECT)
            
            #deciding which buttons have and have not been selected andf highlighting them accordingly 
            if selectedSet:
                for i in LENGTH_BUTTONSET:
                    if i != selectedSet:
                        i.selected = False

            #checking for button input 
            for button in [START_BUTTON, LENGTH_HIGH, LENGTH_MEDIUM, LENGTH_LOW, POMODORO_BACK]:
                button.changeColor(pomoMousepos)
                button.update(screen)

            #checking for input box input 
            for inputbox in [TASK]:
                inputbox.update()
                inputbox.draw(screen)

        #exiting the pomodoro screen once the ESC key has been pressed 
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                running = False

            elif event.type == pg.MOUSEBUTTONDOWN:
                if START_BUTTON.checkForInput(pomoMousepos):

                    #input box returns "Enter task: {userinput}" and so this checks that anything has been entered and a button has been selected and star rating has been given. 
                    if TASK.text == 'Enter task: ' or len(TASK.text) < 12 or selectedSet == None or True not in [i.lit for i in stars_group]:
                        TASK = InputBox(400, 200, 200, 32)
                        EXCEPTION = True

                    #if all of the task input fields have been entered then the start button has been clicked, the task countdown can begin 
                    else:
                        TASKstarted = not TASKstarted

                        #used for calculating elapsed time
                        start_time = pg.time.get_ticks()

                        #5 seconds in milliseconds
                        target_time = localTime[1]  
                        elapsed_time = 0

                #associating button clicked and it's corresponding settings profile. 
                elif LENGTH_LOW.checkForInput(pomoMousepos):
                    localTime = LOW_TIMEPROFILE
                    selectedSet = LENGTH_LOW

                elif LENGTH_MEDIUM.checkForInput(pomoMousepos):
                    localTime = MEDIUM_TIMEPROFILE
                    selectedSet = LENGTH_MEDIUM

                elif LENGTH_HIGH.checkForInput(pomoMousepos):
                    localTime = HIGH_TIMEPROFILE
                    selectedSet = LENGTH_HIGH
                
                elif POMODORO_BACK.checkForInput(pomoMousepos):
                    running = False

                #when a star has been selected 
                elif event.button == 1:  
                    for star in stars_group:
                        #if the mouse's position intersects with the star's shape 
                        if star.rect.collidepoint(event.pos):
                            #then select that star 
                            selected_star = star
                            selected_star.toggle_lit(stars_group)

            TASK.handle_event(event)
        
        pg.display.update()