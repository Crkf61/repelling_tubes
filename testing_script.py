# testing file, do it for 4 'electrons' in a line

import pygame, sys
import numpy as np

dt = 1/50

length = 1   # gap that particles can move in

q = 1        # charge each particle has
m = 1
lamb = 0.1     # damping on each particle

def find_images(positions):
    # find location of 'image charges'
    image_positions = []
    for particle_position in positions:
        image_left = -particle_position
        image_right = 2 - particle_position
        image_positions.append(image_left)
        image_positions.append(image_right)
    return image_positions

def find_all_forces(positions, image_positions, velocities):
    forces = []
    for i in range(len(positions)):
        # iterate over every particle which isn't itself, and every image
        particle_i_pos = positions[i]   # the main character particle
        qi = 1
        force_i = 0

        # real particles
        for j in range(len(positions)):
            if i != j:                    # don't consider main chr ptcle
                particle_j_pos = positions[j]
                qj = 1
                force = find_repulsion_on_i(particle_i_pos, particle_j_pos, qi, qj)
                force_i += force

        # image particles
        for j in range(len(image_positions)):
            image_j_pos = image_positions[j]
            qj = 1
            force = find_repulsion(particle_i_pos, image_j_pos, qi, qj)
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

def print_output(positions):
    rounded_pos = []
    for pos in positions:
        rounded = int(pos * 100)
        rounded_pos.append(rounded)
    output_str = ""
    for i in range(100):
        if i in rounded_pos:
            output_str += 'O'
        else:
            output_str += '-'
    return output_str
    

def timestep(dt, positions, velocities):
    # calculate forces on each particle
    image_positions = find_images(positions)
    forces = find_all_forces(positions, image_positions)

newline = print_output([0.1,0.2,0.6])
print(newline)
