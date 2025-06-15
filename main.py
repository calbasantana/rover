# This file contains all the functions and subfunctions necessary to make a 4WD rover move.

# Importing Things
from time import sleep, time
from FourMotors import MD1, MD2
# Declaring Connections

# Motor Drive 1
M1BIN2 = 32;
M1BIN1 = 33;
M1AIN1 = 12; # NEW
M1AIN2 = 2; # NEW
M1STBY = 21;
M1PWMA = 16;
M1PWMB = 17;
# Motor Drive 2
M2BIN2 = 27;
M2BIN1 = 23;
M2AIN1 = 13;
M2AIN2 = 4;
M2STBY = 22;
M2PWMA = 18;
M2PWMB = 19;
# Servo
SERVO = 14;

# Setting Up MD1
MD1 = MD1(M1BIN2, M1BIN1, M1AIN1, M1AIN2, M1STBY, M1PWMA, M1PWMB)
MD2 = MD2(M2BIN2, M2BIN1, M2AIN1, M2AIN2, M2STBY, M2PWMA, M2PWMB)

# Available Functions

# To select the motor drive, use MD1 or MD2, then to specify function, do
# MD1.forwardMOT1(200). Here, forwardMOT1 is the function that moves motor 1 and 200 is
# the speed.

# Note 1: MD1 controls MOT1 and MOT2; MD2 controls MOT3 and MOT4.
# Note 2: To wait between actions, use sleep(10) with input in seconds.
# Note 3: The speed that you can give each motor ranges from 0-1000.
# Note 4: To see all available functions, you can go to the FourMotors file and open it. Don't
# edit it though!

#debugging
# MD1.forwardMOT2(100)
# sleep(0.09)
# MD1.stopMOT12()

# Program 1: Constant Velocity

MD1.forwardMOT1(300)
MD1.forwardMOT2(300)
MD2.forwardMOT3(300)
MD2.forwardMOT4(300)
sleep(10)
MD1.stopMOT12()
MD2.stopMOT34()

# Program 2: Turn

# MD1.backwardMOT1(300)
# MD1.forwardMOT2(300)
# MD2.forwardMOT3(300)
# MD2.backwardMOT4(300)
# sleep(3)
# MD1.stopMOT12()
# MD2.stopMOT34()

# Program 3: Increasing Velocity

# for i in range(100,900, +100):
#     MD1.forwardMOT12(i)
#     MD2.forwardMOT34(i)
#     sleep(0.5)
# MD1.stopMOT12()
# MD2.stopMOT34()

# Program 4: Decreasing Velocity
#for i in range(800,0, -100):
    #MD1.forwardMOT12(i)
    #MD2.forwardMOT34(i)
    #sleep(1)
#MD1.stopMOT12()
#MD2.stopMOT34()

# Program 5: Round-Trip - YOU CREATE