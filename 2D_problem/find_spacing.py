import numpy as np
import utils as ut
import matplotlib.pyplot as plt

# code to run simulation for each tube number:
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
plt.plot(pitch_array)
plt.show()
'''

# results after running above code twice
pitches1 = np.array([1, 0.8472962292792733, 0.8858005684529696, 0.788039401235061, 0.6097882168942119, 0.6271241355103738, 0.6346860201211674, 0.5685799533317649, 0.501633556390732, 0.4595428383805592, 0.46043602777169446, 0.4533261470767298, 0.4300347206824768, 0.40358427814209075, 0.40496755385876215, 0.38925125981940323, 0.37290811481593755, 0.35940962653865244, 0.360016778088013, 0.3547512444529579, 0.3390257938579308, 0.3345474676572739, 0.31855662298927084, 0.31001530197874255, 0.30360159597143044, 0.3036282584247801, 0.30097550803332396, 0.29169240334269636, 0.2904930496753034])
pitches2 = np.array([1, 0.8488290214657936, 0.885276684556223, 0.7885349145358056, 0.6883824962115559, 0.6277438412705826, 0.6379285267719929, 0.5694090889060596, 0.502401726559791, 0.4765267095640019, 0.4423462000467158, 0.4059417855545664, 0.43084724844749306, 0.4057775275478668, 0.4053857468411857, 0.3903802707236643, 0.3733970727200275, 0.3650598998753926, 0.3673977550879708, 0.35529421000846606, 0.3474510073434195, 0.3357346025816476, 0.3198666966483042, 0.3145986060163928, 0.30885058924360415, 0.30585133650148816, 0.30205492676074064, 0.29091885174244586, 0.2909552913540929])

pitches = 32 * (pitches1 + pitches2) / 2

# inv_pitches = 1/pitches
n = np.arange(1,30)
deg = 4
coeffs = np.polyfit(n, pitches,deg)
scaled_coeffs = 0.064/2 * coeffs
print(scaled_coeffs)
approx_pitch = []
for value in n:
    pitch = 0
    for i in range(deg+1):
        pitch += coeffs[i]*value**(deg-i)
    approx_pitch.append(pitch)

plt.plot(n, pitches)
plt.plot(n,approx_pitch)
plt.ylim(bottom=0)
plt.xlabel('number of tubes')
plt.ylabel('pitch spacing (mm)')
plt.show()
#'''
