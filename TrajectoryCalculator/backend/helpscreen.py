

import pygame, time, os

from backend.util import Util
from backend.about import AboutScreen
import backend.colors as colors, backend.standards as standards
U = Util()
# this screen displays help info and commands
class HelpScreen:
    def __init__(self):
        self.dir = os.getcwd()
        self.running = True
        self.background_image = pygame.image.load('backend/data/images/help.png')
        
    def quit_event(self):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                self.running = False
                
                
    def get_user_input(self):
        # get and process user inputs
        
        keys = pygame.key.get_pressed(  )
        if keys[pygame.K_q]:
            pygame.quit()
            self.running = False
        if keys[pygame.K_b]:
            self.running = False
            # we sleep to avoid skipping screens
            time.sleep(.5)
        elif keys[pygame.K_a]:
            AboutScreen().run()
            
    def help_info(self, window):
        helps = [
            
            "draw a line and its details will be calculated for you",
            "thissoftware has been designed for fast  generaration of",
            "trajectories for   mostly game and software development",
            "tweak  the screen size size to suit your figures"
            "b -  previous screen",
            "q - quit         s - settings",
            "h- help      a - about developer",
            
            
        ]
        pos1 = 100
        spacing = 30
        for h in helps:
            U.text_to_gamer(h, (100, pos1 ), window, colors.white, 20)
            pos1 += spacing
            
    def display(self):
        pygame.init()
        window = pygame.display.set_mode(standards.screen_size, pygame.NOFRAME)
        pygame.display.set_caption("help screen")
        
        window.blit(self.background_image, (0,0))
        #display help info
        self.help_info(window)
        
        # get events
        self.quit_event()
        self.get_user_input()
        
        
        pygame.display.update()
    
    def run(self):
        while self.running:
            self.display()
            continue
            
            
      
