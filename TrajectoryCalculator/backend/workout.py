class WorkOut:
    
    def analyze_straight_line(self, line_coods):
        # analyses a lines coordinates
        # and retunr s its equation , gradient , bla bla
        if len(line_coods) < 2:
            # insufficient points
            pass
        else:
            # we have two points of a line..proceed
            p1 = line_coods[0]
            p2  = line_coods[1]
            
            ch_in_y =  p2[1] - p1[1]
            ch_in_x =  p2[0] -  p1[0]
            
            if ch_in_x == 0:
                # avoiding ZeroDivisionError]
                # :7 men I hate it !!
                ch_in_x = 1
                
            gradient = ch_in_y/ ch_in_x
            
            constant = p2[1] - (gradient * p2[0])
        
            report = f"""
            
            
            line gradient   :   {gradient}
        
            equation        : y = {gradient}x + {constant} 
            """
            
            #print(report)
            report_dict = {'line_equation':f'y = {round(gradient, 2)}x + {round(constant, 2)}',}
            
            return report_dict
            

