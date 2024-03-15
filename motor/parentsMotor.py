from gpiozero import PWMOutputDevice

class ParentsMotor :
    def setPin(self):
        self.MG = PWMOutputDevice("GPIO13")
        self.MD = PWMOutputDevice("GPIO19")

    def VIBG (self,value: float) -> None:
        """vibration moteur gauche"""
        self.MG.value = value

    def VIBD (self,value: float) -> None:
        """vibration moteur droit"""
        self.MD.value = value