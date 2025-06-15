# Importing Things
from machine import Pin, PWM
from time import sleep

# MD1 Class
class MD1():
    def __init__(self,BIN2,BIN1,AIN1,AIN2,STBY,PWMA,PWMB):
        
        self.bin2 = Pin(BIN2, mode=Pin.OUT, pull=None)
        self.bin1 = Pin(BIN1, mode=Pin.OUT, pull=None)
        self.ain2 = Pin(AIN2, mode=Pin.OUT, pull=None)
        self.ain1 = Pin(AIN1, mode=Pin.OUT, pull=None)
        self.stby = Pin(STBY, mode=Pin.OUT, pull=None)
        self.apwm = PWM(Pin(PWMA),50)
        self.bpwm = PWM(Pin(PWMB),50)
        self.stby.value(1)
        
    def forwardMOT2(self,speed):
        self.ain1.value(1)
        self.ain2.value(0)
        self.apwm.duty(speed)

    def forwardMOT1(self,speed):
        self.bin1.value(1)
        self.bin2.value(0)
        self.bpwm.duty(speed)
        
    def forwardMOT12(self,speed):
        self.forwardMOT1(speed)
        self.forwardMOT2(speed)
        
    def backwardMOT2(self,speed):
        self.ain1.value(0)
        self.ain2.value(1)
        self.apwm.duty(speed)
        
    def backwardMOT1(self,speed):
        self.bin1.value(0)
        self.bin2.value(1)
        self.bpwm.duty(speed)
    
    def backwardMOT12(self, speed):
        self.backwardMOT1(speed)
        self.backwardMOT2(speed)
        
    def brakeMOT12(self):
        
        self.ain1.value(1)
        self.ain2.value(1)        
        self.bin1.value(1)
        self.bin2.value(1)
        self.apwm.duty(0)
        self.bpwm.duty(0)
 
    def stopMOT12(self):
        
        self.ain1.value(0)
        self.ain2.value(0)        
        self.bin1.value(0)
        self.bin2.value(0)
        self.apwm.duty(500)
        self.bpwm.duty(500)
        
    def standbyMOT12(self):
        self.ain1.value(0)
        self.ain2.value(0)        
        self.bin1.value(0)
        self.bin2.value(0)
        self.apwm.duty(500)
        self.bpwm.duty(500)
        self.stby.value(0)
        
# MD2 Class
class MD2():
    def __init__(self,BIN2,BIN1,AIN1,AIN2,STBY,PWMA,PWMB):
        
        self.bin2 = Pin(BIN2, mode=Pin.OUT, pull=None)
        self.bin1 = Pin(BIN1, mode=Pin.OUT, pull=None)
        self.ain2 = Pin(AIN2, mode=Pin.OUT, pull=None)
        self.ain1 = Pin(AIN1, mode=Pin.OUT, pull=None)
        self.stby = Pin(STBY, mode=Pin.OUT, pull=None)
        self.apwm = PWM(Pin(PWMA),50)
        self.bpwm = PWM(Pin(PWMB),50)
        self.stby.value(1)
        
    def forwardMOT4(self,speed):
        self.ain1.value(0)
        self.ain2.value(1)
        self.apwm.duty(speed)

    def forwardMOT3(self,speed):
        self.bin1.value(0)
        self.bin2.value(1)
        self.bpwm.duty(speed)
        
    def forwardMOT34(self,speed):
        self.forwardMOT3(speed)
        self.forwardMOT4(speed)
        
    def backwardMOT4(self,speed):
        self.ain1.value(1)
        self.ain2.value(0)
        self.apwm.duty(speed)
        
    def backwardMOT3(self,speed):
        self.bin1.value(1)
        self.bin2.value(0)
        self.bpwm.duty(speed)
    
    def backwardMOT34(self, speed):
        self.backwardMOT3(speed)
        self.backwardMOT4(speed)
        
    def brakeMOT34(self):
        
        self.ain1.value(1)
        self.ain2.value(1)        
        self.bin1.value(1)
        self.bin2.value(1)
        self.apwm.duty(0)
        self.bpwm.duty(0)
 
    def stopMOT34(self):
        
        self.ain1.value(0)
        self.ain2.value(0)        
        self.bin1.value(0)
        self.bin2.value(0)
        self.apwm.duty(500)
        self.bpwm.duty(500)
        
    def standbyMOT34(self):
        self.ain1.value(0)
        self.ain2.value(0)        
        self.bin1.value(0)
        self.bin2.value(0)
        self.apwm.duty(500)
        self.bpwm.duty(500)
        self.stby.value(0)