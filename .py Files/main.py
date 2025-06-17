from rover import MD1, MD2, Rover
from time import sleep

# Setup motor drivers
md1 = MD1(32, 33, 12, 2, 21, 16, 17)
md2 = MD2(27, 23, 13, 4, 22, 18, 19)
rover = Rover(md1, md2)

# Move all motors forward at same speed
rover.move_motor(1, "forward", 600)
rover.move_motor(2, "forward", 600)
rover.move_motor(3, "forward", 600)
rover.move_motor(4, "forward", 600)

sleep(10)

# Stop all motors gradually
rover.gradual_stop_all(direction="forward", initial_speed=700)
