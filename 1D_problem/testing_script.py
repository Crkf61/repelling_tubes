import utils as ut
import time

dt = 1/50
display_dt = 1/20

length = 1   # gap that particles can move in
width = 90   # width to draw particles


# define initial state
positions = [0.5,0.55, 0.51, 0.53]
velocities = [0 for p in positions]
ut.print_output(positions, width)

while True:
    time.sleep(display_dt)
    new_poss, new_vels = ut.timestep(positions, velocities, length, dt)
    display = ut.print_output(new_poss, width)
    print(display, end='\r')
    positions = new_poss.copy()
    velocities = new_vels.copy()

    

