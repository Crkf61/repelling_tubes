import numpy as np
import random

# positions is an array of [x,y] np arrays

def random_starts(n_circles):
    start_positions = []
    for i in range(n_circles):
        radius = 0.9*np.sqrt(random.random()) # up to 0.9, preference for larger numbers
        theta = 2*np.pi*random.random()
        x = radius*np.cos(theta)
        y = radius*np.sin(theta)
        position = np.array([x, y])
        start_positions.append(position)
    return start_positions

def find_images(positions):
    # find location of 'image charges' for unit circle
    image_positions = []
    for particle_pos in positions:
        R = np.linalg.norm(particle_pos)
        x = particle_pos[0]
        y = particle_pos[1]
        if np.abs(R) < 1e-6:
            R = 1e-6
            image = np.array([1,0])/R**2   # needed to ensure effect of image from origin
                                           # particle is negligible
        else:
            image = particle_pos/R**2
        image_positions.append(image)
    return image_positions

def find_all_forces(positions, image_positions, velocities, q, lamb):
    forces = []
    for i in range(len(positions)):
        # iterate over every particle which isn't itself, and every image
        particle_i_pos = positions[i]   # the main character particle
        qi = q
        force_i = np.array([0.,0.])   # 2D array of forve on particle

        # real particles
        for j in range(len(positions)):
            if i != j:                    # don't consider main chr ptcle
                particle_j_pos = positions[j]
                qj = q
                force = find_repulsion_on_i(particle_i_pos, particle_j_pos, qi, qj)
                force_i += force

        # image particles
        for j in range(len(image_positions)):
            image_j_pos = image_positions[j]
            qj = 10*q
            force = find_repulsion_on_i(particle_i_pos, image_j_pos, qi, qj)
            force_i += force

        # damping from velocity
        damping_i = -lamb * velocities[i]
        force_i += damping_i

        forces.append(force_i)
    return forces

def find_repulsion_on_i(pos_i, pos_j, q1, q2):
    rin = pos_i - pos_j  # numpy array
    rin_mag = np.linalg.norm(rin)
    if rin_mag < 3e-2:
        if rin_mag == 0:
            r = 3e-2*np.array([1,0])
        else:
            r = 3e-2*rin / rin_mag
    else:
        r = rin
    r_mag = np.linalg.norm(r)
    force = r * q1 * q2 / r_mag**3 # numpy array
    return force

def run_physics(positions, velocities, forces, dt):
    # integrate eqns of motion
    no_particles = len(positions)
    new_poss = []
    new_vels = []
    for i in range(no_particles):
        pos = positions[i]   # numpy array
        vel = velocities[i]
        force = forces[i]
        # use forward euler
        new_vel = vel + force*dt
        new_pos = pos + new_vel*dt
        new_poss.append(new_pos)
        new_vels.append(new_vel)
    return new_poss, new_vels

def check_pos(positions, velocities):
    clean_pos = []
    clean_vel = []
    spacing = 0.01
    for i in range(len(positions)):
        pos = positions[i]
        vel = velocities[i]
        pos_mag = np.linalg.norm(pos)
        if pos_mag > 1-spacing:
            # put back inside unit circle
            new_pos = (1-2*spacing) * pos / pos_mag
            new_vel = np.array([0,0])
        else:
            new_pos = pos
            new_vel = vel
        clean_pos.append(new_pos)
        clean_vel.append(new_vel)
    return clean_pos, clean_vel

def find_maximum(array):
    maximum = 0
    for value in array:
        abs_value = np.linalg.norm(value)
        if abs_value > maximum:
            maximum = abs_value
    return maximum

def average(array):
    total = 0
    for value in array:
        total += value
    return total / len(array)

def find_pitch(positions):
    length = len(positions)
    if length < 2:
        return 1
    else:
        closest_pitches = []
        
        for i in range(length):
            # for each particle
            closest_distance = 10
            particle_i_pos = positions[i]
            for j in range(length):
                if j != i:
                    # consider each other particle
                    distance = np.linalg.norm(particle_i_pos - positions[j])
                    if distance < closest_distance:
                        closest_distance = distance
            closest_pitches.append(closest_distance)
        # now have full list of closest pitches
        pitch = average(closest_pitches)
        return pitch
        


def timestep(positions, velocities, dt, q0=3, lamb=10):
    n_circles = len(positions)
    q = q0/np.sqrt(np.sqrt(n_circles))
    # calculate forces on each particle
    image_positions = find_images(positions)
    forces = find_all_forces(positions, image_positions, velocities, q, lamb) # forces == accel
    # now integrate eqns of motion to find new positions and velocities
    new_positions, new_velocities = run_physics(positions, velocities, forces, dt)
    cleaned_positions, cleaned_vels = check_pos(new_positions, new_velocities)
    return cleaned_positions, cleaned_vels

###########################################################################################
###########################################################################################
