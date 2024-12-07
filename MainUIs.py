from GUIelements.button import Button
from settings import *
import pygame as pg 
from pomodoroScreen import preGameScreen

def main_menu(): 
        
        #initialising pygame window attributes 
        pg.init()
        screen = pg.display.set_mode(WIN_RES) 
        pg.display.set_caption('main_menu ') 
        mainBG = pg.image.load("textures/assets/mainmenuBG.png")
        mainBG = pg.transform.scale(mainBG, WIN_RES) 
        running = True

        while running == True: 
            screen.blit(mainBG, (0, 0))
            menuMousePos = pg.mouse.get_pos()
            pg.mouse.set_visible(True)
    
            #main menu text 
            MENU_TEXT = get_font(100).render("MAIN MENU", True, "#FFFFFF")
            MENU_RECT = MENU_TEXT.get_rect(center=(800, 100))
            screen.blit(MENU_TEXT, MENU_RECT)

            #play button 
            PLAY_BUTTON = Button(image=pg.image.load("textures/assets/Play Rect.png"), pos=(800, 250), 
                                text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
            #options buttun 
            OPTIONS_BUTTON = Button(image=pg.image.load("textures/assets/Options Rect.png"), pos=(800, 400), 
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
            #information button 
            INFORMATION_BUTTON = Button(image=pg.image.load("textures/assets/Info Rect.png"), pos=(800, 550), 
                                text_input="INFORMATION", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
            #quit button 
            QUIT_BUTTON = Button(image=pg.image.load("textures/assets/Play Rect.png"), pos=(800, 700), 
                                text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
            
            #checking for button inputs and providing a response if so
            for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON, INFORMATION_BUTTON]:

                #dynamic button colour change when mouse hovering over 
                button.changeColor(menuMousePos)
                button.update(screen)

            #checking for inputs 
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(menuMousePos):

                        #if pomodoro screen return "start" then break out of then menu loop. Pomodoro screen will return "start " when the timer countdown completes. 
                        if preGameScreen(screen) == "start":
                            running = False

                    #if options button pressed -> run options screen 
                    if OPTIONS_BUTTON.checkForInput(menuMousePos):
                        options(screen)
                    
                     #if quit button pressed -> quit pygame screen
                    if QUIT_BUTTON.checkForInput(menuMousePos):
                        pg.QUIT()
                    
                     #if information button pressed -> run information screen 
                    if INFORMATION_BUTTON.checkForInput(menuMousePos):
                        information(screen)
                
                #pressing ESC -> quit pygame screen 
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    pg.QUIT()

            pg.display.update()

def options(screen): 
    running = True

    #controller buttons for sensitivity 
    CGAMESENSE_HIGH = Button(image=pg.image.load("textures/assets/Graphics Rect.png"), pos=(900, 325), 
                            text_input="High", font=get_font(20), base_color="#d7fcd4", hovering_color="White")
    CGAMESENSE_MEDIUM = Button(image=pg.image.load("textures/assets/Graphics Rect.png"), pos=(1050, 325), 
                            text_input="Medium", font=get_font(20), base_color="#d7fcd4", hovering_color="White")
    CGAMESENSE_LOW = Button(image=pg.image.load("textures/assets/Graphics Rect.png"), pos=(1200, 325), 
                            text_input="Low", font=get_font(20), base_color="#d7fcd4", hovering_color="White")
    
    #used for dynamic button highlighting (grouping the buttons that have the same fuction together)
    CONTROLLER_BUTTONSET = [CGAMESENSE_HIGH, CGAMESENSE_MEDIUM, CGAMESENSE_LOW]

    #controller sensitivity
    CGAMESENS_TEXT = get_font(20).render("Controller sensitivity", True, "White")
    CGAMESENSE_RECT = CGAMESENS_TEXT.get_rect(center=(500, 325))
    
    #mouse buttons for sensitivity 
    MGAMESENSE_HIGH = Button(image=pg.image.load("textures/assets/Graphics Rect.png"), pos=(900, 250), 
                            text_input="High", font=get_font(20), base_color="#d7fcd4", hovering_color="White")
    MGAMESENSE_MEDIUM = Button(image=pg.image.load("textures/assets/Graphics Rect.png"), pos=(1050, 250), 
                            text_input="Medium", font=get_font(20), base_color="#d7fcd4", hovering_color="White")
    MGAMESENSE_LOW = Button(image=pg.image.load("textures/assets/Graphics Rect.png"), pos=(1200, 250), 
                            text_input="Low", font=get_font(20), base_color="#d7fcd4", hovering_color="White")
    
    #used for dynamic button highlighting (grouping the buttons that have the same fuction together)
    MOUSE_BUTTONSET = [MGAMESENSE_HIGH, MGAMESENSE_MEDIUM, MGAMESENSE_LOW]
    
    #mouse sensitivity
    MGAMESENS_TEXT = get_font(20).render("Mouse sensitivity", True, "White")
    MGAMESENSE_RECT = MGAMESENS_TEXT.get_rect(center=(500, 250))
    
    #graphical buttons to set graphical presets.
    GRAPHICS_HIGH = Button(image=pg.image.load("textures/assets/Graphics Rect.png"), pos=(900, 175), 
                            text_input="High", font=get_font(20), base_color="#d7fcd4", hovering_color="White")
    GRAPHICS_MEDIUM = Button(image=pg.image.load("textures/assets/Graphics Rect.png"), pos=(1050, 175), 
                            text_input="Medium", font=get_font(20), base_color="#d7fcd4", hovering_color="White")
    GRAPHICS_LOW = Button(image=pg.image.load("textures/assets/Graphics Rect.png"), pos=(1200, 175), 
                            text_input="Low", font=get_font(20), base_color="#d7fcd4", hovering_color="White")
    
    #used for dynamic button highlighting (grouping the buttons that have the same fuction together)
    GRAPHICS_BUTTONSET = [GRAPHICS_HIGH, GRAPHICS_MEDIUM, GRAPHICS_LOW]

    #graphics text
    GRAPHICS_TEXT = get_font(20).render("Graphics settings", True, "White")
    GRAPHICS_RECT = GRAPHICS_TEXT.get_rect(center=(500, 175))
    
    #no buttons have ben selected yet. Three buttons can be selkected at max at the same time as there are three different rows of buttons 
    selectedSet = [None, None, None]
    
    #back button to main menu 
    OPTIONS_BACK = Button(image=None, pos=(120, 860), 
                            text_input="BACK", font=get_font(50), base_color="white", hovering_color="Green")
    #options text
    OPTIONS_TEXT = get_font(45).render("Options Menu", True, "White")
    OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(800, 50))
    
    while running == True: 
        optionsMousePos = pg.mouse.get_pos()
        screen.fill("black")

        #drawing text to screen 
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)
        screen.blit(GRAPHICS_TEXT, GRAPHICS_RECT)
        screen.blit(MGAMESENS_TEXT, MGAMESENSE_RECT)
        screen.blit(CGAMESENS_TEXT, CGAMESENSE_RECT)

        #when a button has been clicked -> highlights bar at bottom. Therefore when mutiple buttons have been clicked -> the unselected buttons must be unhighlighted 
        #if a button has been selected then: 
        if selectedSet:

            #retreiving index position (b) and iterable (a)
            for a, b in enumerate([GRAPHICS_BUTTONSET, MOUSE_BUTTONSET, CONTROLLER_BUTTONSET]):
                #button set includes three items (button1, button2, button3)
                for c in b:
                    #checking which buttons have not been selected and de-highlighting them if they are currently highlighted
                    if c != selectedSet[a]:
                        c.selected = False

        #checking for button input 
        for button in [OPTIONS_BACK, GRAPHICS_HIGH, GRAPHICS_MEDIUM, GRAPHICS_LOW, MGAMESENSE_HIGH, MGAMESENSE_MEDIUM, MGAMESENSE_LOW, CGAMESENSE_HIGH, CGAMESENSE_MEDIUM, CGAMESENSE_LOW]:
                button.changeColor(optionsMousePos)
                button.update(screen)

        #checking for ESC and quiting pygame if so 
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                running = False

            #checking which button has been selected and adding it to the selected set
            if event.type == pg.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(optionsMousePos):
                    running = False 
                if GRAPHICS_HIGH.checkForInput(optionsMousePos):
                    settingsSaver("Graphics:","High")
                    selectedSet[0] = GRAPHICS_HIGH

                if GRAPHICS_MEDIUM.checkForInput(optionsMousePos):
                    settingsSaver("Graphics:","Medium")
                    selectedSet[0] = GRAPHICS_MEDIUM

                if GRAPHICS_LOW.checkForInput(optionsMousePos):
                    settingsSaver("Graphics:","Low")
                    selectedSet[0] = GRAPHICS_LOW

                if MGAMESENSE_HIGH.checkForInput(optionsMousePos):
                    settingsSaver("Mouse Sensitivity:","High")
                    selectedSet[1] = MGAMESENSE_HIGH

                if MGAMESENSE_MEDIUM.checkForInput(optionsMousePos):
                    settingsSaver("Mouse Sensitivity:","Medium")
                    selectedSet[1] = MGAMESENSE_MEDIUM

                if MGAMESENSE_LOW.checkForInput(optionsMousePos):
                    settingsSaver("Mouse Sensitivity:","Low")
                    selectedSet[1] = MGAMESENSE_LOW

                if CGAMESENSE_HIGH.checkForInput(optionsMousePos):
                    settingsSaver("Controller Sensitivity:","High")
                    selectedSet[2] = CGAMESENSE_HIGH

                if CGAMESENSE_MEDIUM.checkForInput(optionsMousePos):
                    settingsSaver("Controller Sensitivity:","Medium")
                    selectedSet[2] = CGAMESENSE_MEDIUM

                if CGAMESENSE_LOW.checkForInput(optionsMousePos):
                    settingsSaver("Controller Sensitivity:","Low")
                    selectedSet[2] = CGAMESENSE_LOW
               
        pg.display.update()
    
def information(screen):
    running = True
    info = """This is a time managment program which seeks to help students manage their schedules and revise more productively.            \n
              It utilises a technique called the pomodoro cycle, This is a time management method which shows that an overall increase      \n
              in productivity can take place if small breaks are used to divide allocated work time evenly. Typically, a timer is set       \n
              for 25 minutes during which, an individual will work/revise. Once 25 minutes has passed, the individual will take a 5-minute  \n
              break where they can relax. This program is used to organise this cycle. Once pressing PLAY from the menu, you can then enter \n
              the task you will try and complete (e.g homework), you will also be prompted to decide how long this task will take as well as\n
              it's perceived difficulty out of 5. A timer will then begin and you can start on your task. Once the timer hits 0,            \n
              congratulations! You can take a break. And during this break you can explore the game.                                  \n
           """
    
    #in the list form 
    info = info.split("\n")

    while running == True: 
        optionsMousePos = pg.mouse.get_pos()
        screen.fill("dark grey")
       
        #Back button to main menu 
        OPTIONS_BACK = Button(image=None, pos=(120, 860), 
                            text_input="BACK", font=get_font(50), base_color="Black", hovering_color="Green")
        
        #options text 
        OPTIONS_TEXT = get_font(45).render("Game information", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(800, 50))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        #this process is used to split the lines of text evenly across the screen 
        for a, b in enumerate(info):
            
            INFORMATION_TEXT = get_font(10).render(f"{b}", True, "Black")
            #depending on the index position relative to the information text list, place the line of text further down the screen so that the text objects do not overlap 
            if a != 0:   INFORMATION_RECT = INFORMATION_TEXT.get_rect(center=(800, (a*12 ) + 200))
            #if statement occurs because first line of text is slightly further back when being blit to the screen 
            elif a == 0:     INFORMATION_RECT = INFORMATION_TEXT.get_rect(center=(869, (a*12 ) + 200))
            
            screen.blit(INFORMATION_TEXT, INFORMATION_RECT)

        #checking for button input 
        for button in [OPTIONS_BACK]:
                button.changeColor(optionsMousePos)
                button.update(screen)

        #checking for ESC input 
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                running = False

            #breaking out of options screen loop back to main menu 
            if event.type == pg.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(optionsMousePos):
                        running = False 

        pg.display.update()
    
#quickly returning the font size 
def get_font(size): 
    return pg.font.Font("textures/assets/font.ttf", size)


#function for saving settings state in "savedSettings.txt"
def settingsSaver(datType, data): 
     
     with open ("textures/DAT/savedSettings.txt", "r") as f: 
         filedata = f.readlines()
        
    #parsing the data 
     for i, line in enumerate(filedata):
        if line.startswith(datType):
            filedata[i] = f"{datType}  {data}\n"
         
     with open ("textures/DAT/savedSettings.txt", "w") as f: 
         f.writelines(filedata)
        