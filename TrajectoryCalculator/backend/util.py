import pygame

class Util:
    def text_to_gamer(self, message, position, window, color, fontsize, font = 'chalkduster'):
        #### _this function  writes  a message to the user
        pygame.font.init()
        mess_obj = pygame.font.SysFont(font, fontsize)
        mess_render = mess_obj.render(message, 20, color)
        window.blit(mess_render, position)
    def string_to_rgb(self, the_string):
        # convert strings with integeras  into 
        # an rgb tuple format
        # eg '200 33 44'   becomes (200,33,44)
        
        to_list = the_string.split()
        int_list = []
        for item in to_list:
            int_list.append(int(item))
        
        integer_tuple = tuple(int_list)
        return integer_tuple
        
        



        
        