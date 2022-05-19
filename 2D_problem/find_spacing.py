import numpy as np
import utils as ut
import matplotlib.pyplot as plt
'''

dt = 1/60

#pitch_array = [1] # for n=1, pitch is just radius

def run_iteration_find_pitch(n_circles):

    positions = ut.random_starts(n_circles)
    velocities = [0 for p in positions]

    max_vel = 1
    vel_tolerance = 1e-2
    t = 0
    broken = False

    while t<1 or max_vel > vel_tolerance:
        positions, velocities = ut.timestep(positions, velocities, dt)
        max_vel = ut.find_maximum(velocities)
        t += dt
        #print(t)
        #print(max_vel)
        if t > 30:
            broken = True
            max_vel = 0 # manually breaks loop
            print('broken!!! trying again')

    if broken:
        return run_iteration_find_pitch(n_circles)
    else:
        # now have final positions, so need to find pitch spacing
        pitch = ut.find_pitch(positions)
        return pitch


#pitch_array.append(pitch)

#n_circles = 20
#pitch_spacing = run_iteration_find_pitch(n_circles)
#print('pitch for n = ' + str(n_circles))
#print(pitch_spacing)

pitch_array = [1]
for n_circles in range(2,30):
    pitch_spacing = run_iteration_find_pitch(n_circles)
    print('pitch for n = ' + str(n_circles))
    print(pitch_spacing)
    pitch_array.append(pitch_spacing)

print(pitch_array)
'''

pitches =[1, 0.8472962292792733, 0.8858005684529696, 0.788039401235061, 0.6097882168942119, 0.6271241355103738, 0.6346860201211674, 0.5685799533317649, 0.501633556390732, 0.4595428383805592, 0.46043602777169446, 0.4533261470767298, 0.4300347206824768, 0.40358427814209075, 0.40496755385876215, 0.38925125981940323, 0.37290811481593755, 0.35940962653865244, 0.360016778088013, 0.3547512444529579, 0.3390257938579308, 0.3345474676572739, 0.31855662298927084, 0.31001530197874255, 0.30360159597143044, 0.3036282584247801, 0.30097550803332396, 0.29169240334269636, 0.2904930496753034]

plt.plot(pitches)
plt.show()
