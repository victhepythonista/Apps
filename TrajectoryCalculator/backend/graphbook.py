
import pygame, os, sys

import backend.standards as standards, backend.colors as colors

from backend.settings import Settings
from backend.util import Util
from backend.outliner import OutLiner
from backend.workout import WorkOut
from backend.helpscreen import HelpScreen
from backend.about import AboutScreen
from backend.datahandler import DataHandler
U = Util()

class GraphBook:
    """
    
    draw a line and its 
    properties
         # a position indicator
         # info bar
         # output data bar
         # """
    def __init__(self):
        # penattributes
        self.pen_color = colors.black
        self.pen_width = 3
        self.background_color = colors.mint_cream
        self.running =True
        self.points = []
        self.cached_points = []
        self.drawing = False  
        self.clock = pygame.time.Clock()
        self.output_font = 20
        self.output_color = colors.steel_blue
        self.data_color = colors.midnightblue
        
        self.commands_color = colors.black
        self.data_bar_background_color = colors.skyblue
        
        self.util  = Util()
        self.line_data = {"line_equation":'',
                            }
                
    def  save_trajectory(self):
        self.running = False
        
        print("\n please enter file name to save directory  or else it will be saved  with a random name\nfind trajectories at Desktop/trajectories")
        name = input("filename   :")
        if self.points != []:
            # we have somthing to save
            
            if name == "":
                # name is  blank
                DataHandler().save_trajectory_points(self.cached_points)
            else:
                DataHandler().save_trajectory_points(self.cached_points, name)
                print(f"file {name}.txt has been saved")
                  
        else:
            print("nothing to save")
            
        self.running = True
                        
    def key_input(self):
        # handle ket inputs 
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_q]:
            # press q to quit app
            pygame.quit()
            self.running = False
        
        elif keys[pygame.K_h]:
            # h for help screen
            HelpScreen().run()
        elif keys[pygame.K_a]:
            AboutScreen().run()   
        elif keys[pygame.K_b]:
            self.running = False
        elif keys[pygame.K_f]:
            self.save_trajectory()
            
        elif keys[pygame.K_s]:
            DataHandler().save_trajectory_points(self.cached_points)
            
    def quit_event(self):
        # anticipate a quit event
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                self.running = False
                sys.exit()
           
            elif ev.type == pygame.MOUSEMOTION and self.drawing == True:
                # mouse down and in motion
                self.points.append(ev.pos)
                
            elif ev.type == pygame.MOUSEBUTTONDOWN:
                # start recording points on mousebutton down
                self.points.append(ev.pos)
                self.points =[]
                self.drawing = True
                
            elif ev.type == pygame.MOUSEBUTTONUP:
                # we now process the stored coordinates
                if len(self.points) >= 2:
                    self.line_data = WorkOut().analyze_straight_line(self.points)
                    self.cached_points = self.points
                    
                
                    self.drawing = False
                
    def draw_data_bar(self, window):
        # that bar at the bottom for 
        # displaying output and stuff
        OutLiner().draw_outline(0, 540, 800, 70, window, outline_width=0, color=self.data_bar_background_color)
      
    def command_help(self, window):
        # display commands just above the data outpus
        U.text_to_gamer('                    h - help        q - quit  f - save trajectory to a named file    s - save trajectory', (25,545), window, self.commands_color, 20)          
    def draw_points(self, window):
        # draw the coordinates only if there are more than two points
        # once again avoiding a big error
        if len(self.points) > 1:
            pygame.draw.lines(window, self.pen_color, False, self.points, self.pen_width)
                     
    def line_equation_bar(self, window):
        # display the line equation of the straight
        #  line between start point and end point
        
        
        line_equation = self.line_data['line_equation']
        curved_equation = 'coming soon'
        U.text_to_gamer(f"equation of start and endpoint line".upper(), (170,560), window, self.output_color, self.output_font)
        U.text_to_gamer(f"{line_equation}", (170,585), window,self.data_color, self.output_font)
    
    def position_bar(self, window):
        # displays the position of the mouse on the screen
        pos = pygame.mouse.get_pos()
        pos = str(pos)
        pos_text_color = colors.green
        
        U.text_to_gamer('MOUSE POS :', (50,560), window, self.output_color,self.output_font) 
        U.text_to_gamer(pos, (50,580), window, self.data_color,self.output_font) 
        #OutLiner().draw_outline(40,550, 150, 50, window, color=colors.skyblue)
    
    
    def display(self):
        pygame.init()
        # display the graphbook 
        window = pygame.display.set_mode(standards.screen_size, pygame.NOFRAME)
        window.fill(self.background_color)
        #window.fill(colors.black)
        pygame.display.set_caption("LineMaster")
        
        # draw the data bar
        self.draw_data_bar(window)
        # get key inputs
        self.key_input()
        
        # display equation of the last line
        self.line_equation_bar(window)
        
        # display command help
        self.command_help(window)        
        # draw points with the mouse
        self.draw_points(window)
        
        # position bar
        self.position_bar(window)
        self.quit_event()
        pygame.display.update()
        self.clock.tick(10)
    
    def run(self):
        while self.running:
            self.display()
            
            
        
        
        
