import numpy as np

# positions is an array of [x,y] np arrays
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
            qj = 5*q
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
    if rin_mag < 1e-3:
        if rin_mag == 0:
            r = 1e-3*np.array([1,0])
        else:
            r = 1e-3*rin / rin_mag
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

def timestep(positions, velocities, dt, q=3, lamb=10):
    # calculate forces on each particle
    image_positions = find_images(positions)
    forces = find_all_forces(positions, image_positions, velocities, q, lamb) # forces == accel
    # now integrate eqns of motion to find new positions and velocities
    new_positions, new_velocities = run_physics(positions, velocities, forces, dt)
    cleaned_positions, cleaned_vels = check_pos(new_positions, new_velocities)
    return cleaned_positions, cleaned_vels

###########################################################################################
###########################################################################################
