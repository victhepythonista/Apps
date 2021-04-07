
# controls
    # s - start  drawing lines
    # q - exit app
    # h - help
    
import pygame,os, sys

import backend.colors as colors,backend.standards as standards
from backend.util import Util
from backend.outliner import OutLiner
from backend.graphbook import GraphBook
from backend.about import AboutScreen
from backend.helpscreen import HelpScreen
pygame.init() 
class HomeScreen:
    # the first screen of the app
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.fps =40
        self.dir = os.getcwd()
        self.background_image = pygame.image.load('backend/data/images/homebackground1.jpg')
        self.info_color = colors.green
        self.info_size = 60
    def quit_event(self):
        # anticipate and handle a  quit
        pygame.init
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                
                self.running = False
                pygame.quit()
                sys.exit(0)
                
    def get_user_input(self):
        # get and process user inputs
        
        keys = pygame.key.get_pressed(    )
        if keys[pygame.K_q]:
            pygame.quit()
            self.running = False
        
        elif keys[pygame.K_a]:
            # about screen
            AboutScreen().run()
           
            
     
        elif keys[pygame.K_g]:
             # display the graphbook
            GraphBook().run()
            
        elif keys[pygame.K_h]:
            # open the helpscreen
            HelpScreen().run()
        
            
        
                
    def display_info(self, screen):
        ## display info onto the screen 
        pygame.init()
        U = Util()
        info_x_cood = 200

        data = [
            
            "g - open graphbook   "  ,
                "q - quit    ",
                "h - help"
                
                ]
        y_pos = 200
        spacing = 100
        for d in data:
            U.text_to_gamer(d, (info_x_cood, y_pos), screen, self.info_color, self.info_size)
            y_pos += spacing
        OutLiner().draw_outline(50, 50, 700, 500, screen, color=colors.skyblue3, border_radius=50)
        
    def display(self):
        pygame.init()
        # display the home screen
        window = pygame.display.set_mode(standards.screen_size, pygame.NOFRAME)
        #window.fill(colors.black)
        pygame.display.set_caption("TrajectoryCalculator")
        
        # display background
        window.blit(self.background_image, (0,0))
        
        ## display information
        self.display_info(window)
        
        
        # get user input
        self.get_user_input()
        
       
        self.quit_event()
        self.clock.tick(self.fps)
        pygame.display.update()
        
    def run(self):
        # start the shome screen loop
        while self.running:
            self.display()
