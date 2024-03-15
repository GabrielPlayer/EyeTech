from .parentsMotor import ParentsMotor
from time import sleep

class Fin (ParentsMotor) :
    def __init__(self, vibG, vibD) -> None:
        super().__init__()
        self.MG = vibG
        self.MD = vibD
        self.duree=0.25

    def long (self): 
        """tps vibration morse"""
        self.VIBG(1)
        self.VIBD(1)
        sleep(3*self.duree)
        self.VIBG(0) 
        self.VIBD(0)

    def court (self):
        """tps vibration morse"""
        self.VIBG(1)
        self.VIBD(1)
        sleep(self.duree)
        self.VIBG(0) 
        self.VIBD(0)

    def start (self):
        """fin en morse"""
        self.court()
        self.court()
        self.long()
        self.court()
        sleep(3*self.duree)
        self.court()
        self.court()
        sleep(3*self.duree)
        self.long()
        self.court()

if __name__ == "__main__":
    Fin().start()