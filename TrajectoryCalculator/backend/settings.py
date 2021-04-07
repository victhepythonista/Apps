import configparser,os


class Settings():
    def __init__(self):
        self.messages = os.path.join(os.getcwd(),'data/settings/settings.txt')
        self.message_parser = configparser.ConfigParser()
        self.message_parser.read(self.messages)
    def checkfile(self,file):
        try:
            with open(file, 'r') as f:
            
                f.close()
                return True
        except:
            with open(file, 'w') as f:
                f.close()


    def read(self, section, var):
        data = self.message_parser[section][var]
        print(data)
        return data
        
    def write(self, section,var,  data):
        try:
            self.message_parser[section][var] = data
        except:
            self.message_parser.add_section(section)
            self.message_parser[section] = {var:data}
        with open(self.messages, 'w') as f:
            self.message_parser.write(f)
            
    def run(self):
        
        pass
        
        
