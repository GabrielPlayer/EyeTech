from .parentsMotor import ParentsMotor, PWMOutputDevice
from time import sleep

class Debut(ParentsMotor):
    def __init__(self, vibG: PWMOutputDevice, vibD: PWMOutputDevice) -> None:
        self.MG = vibG
        self.MD = vibD
        self.duree = 0.25

    def long(self) -> None: 
        """tps vibration morse"""
        self.VIBG(1)
        self.VIBD(1)
        sleep(3*self.duree)
        self.VIBG(0) 
        self.VIBD(0)

    def court(self) -> None:
        """tps vibration morse"""
        self.VIBG(1)
        self.VIBD(1)
        sleep(self.duree)
        self.VIBG(0) 
        self.VIBD(0)

    def start(self) -> None:
        """go en morse"""
        self.long()
        self.long()
        self.court()
        sleep(3*self.duree)
        self.long()
        self.long()
        self.long()

if __name__ == "__main__":
    p = ParentsMotor()
    p.setPin()
    Debut(p.MG, p.MD).start()