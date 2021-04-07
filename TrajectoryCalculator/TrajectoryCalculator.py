
from backend.appbackend import AppBackend




class  TrajectoryCalculatorApp:
    def startapp(self):
        AppBackend().display()
        
        
        
if __name__ == '__main__':

    TrajectoryCalculatorApp().startapp()