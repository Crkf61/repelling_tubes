import numpy as np


def find_images(positions, length):
    # find location of 'image charges'
    image_positions = []
    for particle_position in positions:
        image_left = -particle_position
        image_right = 2*length - particle_position
        image_positions.append(image_left)
        image_positions.append(image_right)
    return image_positions

def find_all_forces(positions, image_positions, velocities, q, lamb):
    forces = []
    for i in range(len(positions)):
        # iterate over every particle which isn't itself, and every image
        particle_i_pos = positions[i]   # the main character particle
        qi = q
        force_i = 0

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
            qj = 2*q
            force = find_repulsion_on_i(particle_i_pos, image_j_pos, qi, qj)
            force_i += force

        # damping from velocity
        damping_i = -lamb * velocities[i]
        force_i += damping_i

        forces.append(force_i)
    return forces

def find_repulsion_on_i(pos_i, pos_j, q1, q2):
    rin = pos_i - pos_j
    if np.abs(rin) < 1e-4:
        r = 1e-4
    else:
        r = rin
    r_mag = np.abs(r)
    force = r * q1 * q2 / r_mag**3
    return force

def print_output(positions, width):
    rounded_pos = []
    for i in range(len(positions)):
        pos = positions[i]
        rounded = int(pos * width)
        rounded_pos.append(rounded)
    output_str = "["
    for i in range(width):
        if i in rounded_pos:
            output_str += 'O'
        else:
            output_str += ' '
    output_str += ']'
    return output_str
    
def run_physics(positions, velocities, forces, dt):
    no_particles = len(positions)
    new_poss = []
    new_vels = []
    for i in range(no_particles):
        pos = positions[i]
        vel = velocities[i]
        force = forces[i]
        # use backward euler for stability
        new_vel = vel + force*dt
        new_pos = pos + new_vel*dt
        new_poss.append(new_pos)
        new_vels.append(new_vel)
    return new_poss, new_vels

def check_pos(positions, velocities, length):
    clean_pos = []
    clean_vel = []
    spacing = 0.06
    for i in range(len(positions)):
        pos = positions[i]
        vel = velocities[i]
        if pos < length*spacing:
            new_pos = length*(i+1)*spacing
            new_vel = 0
        elif pos > length*(1 - spacing):
            new_pos = length*(1-(i+1)*spacing)
            new_vel = 0
        else:
            new_pos = pos
            new_vel = vel
        clean_pos.append(new_pos)
        clean_vel.append(new_vel)
    return clean_pos, clean_vel

def timestep(positions, velocities, length, dt, q=1, lamb=10):
    # calculate forces on each particle
    image_positions = find_images(positions, length)
    forces = find_all_forces(positions, image_positions, velocities, q, lamb) # forces == accel
    new_positions, new_velocities = run_physics(positions, velocities, forces, dt)
    cleaned_positions, cleaned_vels = check_pos(new_positions, new_velocities, length)
    return cleaned_positions, cleaned_vels


