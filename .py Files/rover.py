from machine import Pin, PWM
from time import sleep

class MD1:
    def __init__(self, BIN2, BIN1, AIN1, AIN2, STBY, PWMA, PWMB):
        self.bin2 = Pin(BIN2, mode=Pin.OUT)
        self.bin1 = Pin(BIN1, mode=Pin.OUT)
        self.ain1 = Pin(AIN1, mode=Pin.OUT)
        self.ain2 = Pin(AIN2, mode=Pin.OUT)
        self.stby = Pin(STBY, mode=Pin.OUT)
        self.apwm = PWM(Pin(PWMA), freq=50)
        self.bpwm = PWM(Pin(PWMB), freq=50)
        self.stby.value(1)

    def forwardMOT1(self, speed):
        self.bin1.value(1)
        self.bin2.value(0)
        self.bpwm.duty(speed)

    def backwardMOT1(self, speed):
        self.bin1.value(0)
        self.bin2.value(1)
        self.bpwm.duty(speed)

    def stopMOT1(self):
        self.bpwm.duty(0)
        self.bin1.value(0)
        self.bin2.value(0)

    def forwardMOT2(self, speed):
        self.ain1.value(1)
        self.ain2.value(0)
        self.apwm.duty(speed)

    def backwardMOT2(self, speed):
        self.ain1.value(0)
        self.ain2.value(1)
        self.apwm.duty(speed)

    def stopMOT2(self):
        self.apwm.duty(0)
        self.ain1.value(0)
        self.ain2.value(0)

class MD2:
    def __init__(self, BIN2, BIN1, AIN1, AIN2, STBY, PWMA, PWMB):
        self.bin2 = Pin(BIN2, mode=Pin.OUT)
        self.bin1 = Pin(BIN1, mode=Pin.OUT)
        self.ain1 = Pin(AIN1, mode=Pin.OUT)
        self.ain2 = Pin(AIN2, mode=Pin.OUT)
        self.stby = Pin(STBY, mode=Pin.OUT)
        self.apwm = PWM(Pin(PWMA), freq=50)
        self.bpwm = PWM(Pin(PWMB), freq=50)
        self.stby.value(1)

    def forwardMOT3(self, speed):
        self.bin1.value(1)
        self.bin2.value(0)
        self.bpwm.duty(speed)

    def backwardMOT3(self, speed):
        self.bin1.value(0)
        self.bin2.value(1)
        self.bpwm.duty(speed)

    def stopMOT3(self):
        self.bpwm.duty(0)
        self.bin1.value(0)
        self.bin2.value(0)

    def forwardMOT4(self, speed):
        self.ain1.value(1)
        self.ain2.value(0)
        self.apwm.duty(speed)

    def backwardMOT4(self, speed):
        self.ain1.value(0)
        self.ain2.value(1)
        self.apwm.duty(speed)

    def stopMOT4(self):
        self.apwm.duty(0)
        self.ain1.value(0)
        self.ain2.value(0)

class Rover:
    def __init__(self, md1, md2):
        self.md1 = md1
        self.md2 = md2
        self.motors = {
            1: {"driver": md1, "forward": md1.forwardMOT1, "backward": md1.backwardMOT1, "stop": md1.stopMOT1},
            2: {"driver": md1, "forward": md1.forwardMOT2, "backward": md1.backwardMOT2, "stop": md1.stopMOT2},
            3: {"driver": md2, "forward": md2.forwardMOT3, "backward": md2.backwardMOT3, "stop": md2.stopMOT3},
            4: {"driver": md2, "forward": md2.forwardMOT4, "backward": md2.backwardMOT4, "stop": md2.stopMOT4},
        }

    def move_motor(self, motor_num, direction, speed, duration=None, stop_type="brake"):
        if motor_num not in self.motors:
            raise ValueError("Invalid motor number")
        
        motor = self.motors[motor_num]
        if direction == "forward":
            motor["forward"](speed)
        elif direction == "backward":
            motor["backward"](speed)
        else:
            raise ValueError("Invalid direction")

        if duration:
            sleep(duration)
            if stop_type == "brake":
                motor["stop"]()
            elif stop_type == "gradual":
                for s in range(speed, 0, -50):
                    motor["forward"](s if direction == "forward" else -s)
                    sleep(0.05)
                motor["stop"]()
                
    def gradual_stop_all(self, direction="forward", initial_speed=700, step=50, delay=0.05):
        speeds = {motor: initial_speed for motor in self.motors}
        while any(speed > 0 for speed in speeds.values()):
            for motor_num, motor in self.motors.items():
                speed = speeds[motor_num]
                if speed > 0:
                    if direction == "forward":
                        motor["forward"](speed)
                    elif direction == "backward":
                        motor["backward"](speed)
                    speeds[motor_num] = max(0, speed - step)
            sleep(delay)
        for motor in self.motors.values():
            motor["stop"]()

