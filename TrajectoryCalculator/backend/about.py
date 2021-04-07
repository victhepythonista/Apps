

import pygame, time, os
from backend.util import Util

import backend.colors as colors, backend.standards as standards
U = Util()
# this screen displays help info and commands
class AboutScreen:
    def __init__(self):
        self.running = True
        self.dir = os.getcwd()
        self.background_image = pygame.image.load('backend/data/images/about.png')
        
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
            time.sleep(.5)
    def info(self, window):
    
        pos1 = 100
        spacing = 200
        for h in information:
            U.text_to_gamer(h, (100, pos1 ), window, colors.white, 50)
            pos1 += spacing
            
    def display(self):
        pygame.init()
        window = pygame.display.set_mode(standards.screen_size, pygame.NOFRAME)
        pygame.display.set_caption("About")
        window.blit(self.background_image, (0,0))
     
        # get events
        self.quit_event()
        self.get_user_input()
        
        
        pygame.display.update()
    
    def run(self):
        while self.running:
            self.display()
           