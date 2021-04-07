
import pygame
import backend.colors as  colors


class OutLiner:
    
    def draw_outline(self, x, y, length, height, window,outline_width = 4,   color = colors.green, border_radius = 10):
        outline = pygame.rect.Rect(x,y, length, height)
        pygame.draw.rect(window,color, outline, outline_width, border_radius)
        
    