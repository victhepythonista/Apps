import pygame

import backend.standards

from backend.homescreen import HomeScreen
from backend.util import Util 
pygame.init()
class AppBackend:
    def __init__(self):
        self.running =True
        self.clock = pygame.time.Clock()
        self.fps = 60
        
        
    def quit_event(self):
        pygame.init()

    
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            
    
    def display(self):
        while self.running:
            HomeScreen().run()
            
