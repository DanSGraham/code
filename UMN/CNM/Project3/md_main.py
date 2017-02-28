#Molecular Dynamics Simulation using Lennard-Jones
#By Daniel Graham
import math
from mpl_toolkits.mplot3d import Axes3D
import random
import matplotlib.pyplot as plt
import initialize_coordinates
import numpy as np
import time


def distance(coord1, coord2):
    dist = coord2 - coord1
    dist2 = np.square(dist)
    return np.sqrt(np.sum(dist2))


def pair_correlation_fun(pos_matrix, bin_size=0.05, total_dist=7.0, bulk_density=(1./8.)):
    #A function to determine the pair correlation.
    the_bins = np.array([0.0 for j in range(int(np.ceil(total_dist/bin_size)))])
    b_t = []
    for particle1 in pos_matrix:
        for particle2 in pos_matrix:
            dist_val = distance(particle2, particle1)
            if dist_val > 0 and dist_val < total_dist:
                index_val = int(np.ceil((dist_val) / bin_size)) - 1
                the_bins[index_val] += 1.0

    return the_bins, b_t

def pair_correlation_correction(pair_avg_list, bin_size = 0.05, total_dist=7.0, bulk_density=(1./8.)):

    last_val = 0
    bin_index = []        
    for n in range(len(pair_avg_list)):
        div_value = 4.0 * np.pi * ((n + 1) * bin_size) ** 2. * bin_size
        bin_value = pair_avg_list[n] / (64.0 * div_value * bulk_density)
        pair_avg_list[n] = bin_value
        bin_index.append(last_val + bin_size)
        last_val = bin_index[-1]
    return pair_avg_list, bin_index

def ACCEL(pos_matrix, particle_mass, box_lenx=8.0, box_leny=8.0, box_lenz=8.0):
    po_en = 0.0
    force_matrix = np.zeros_like(pos_matrix)
    for i in range (0, len(pos_matrix) - 1):
        particle_i = pos_matrix[i]
        for j in range(i + 1, len(pos_matrix)):
            particle_j = pos_matrix[j]
            dist = particle_i - particle_j
            dist[0] = dist[0] - round(dist[0]/box_lenx) * box_lenx
            dist[1] = dist[1] - round(dist[1]/box_leny) * box_leny
            dist[2] = dist[2] - round(dist[2]/box_lenz) * box_lenz
            dist2 = dist ** 2
            r2 = sum(dist2)
            r6 = r2 ** 3.0
            r12 = r2 ** 6.0
                        #Check force function to esure correctness
            force_on_pi = ((48./r2) * ((1./r12) - (0.5/r6))) * dist
            force_on_pj = -1.* force_on_pi
            #Equal opposite forces.
            force_matrix[i] += force_on_pi
            force_matrix[j] += force_on_pj
            po_en += 4.0 * ((1./r12) - (1./r6))
    return ((force_matrix/particle_mass), po_en)

def UPDATE(curr_pos, curr_velocity, time_step, box_lenx=8.0, box_leny=8.0, box_lenz=8.0, particle_mass=1):
    curr_acceleration, p_E = ACCEL(curr_pos, particle_mass)
    next_pos = curr_pos + curr_velocity * time_step + (.5 * time_step ** 2.) * curr_acceleration
    for particle in next_pos:
        particle[0] = particle[0] % box_lenx
        particle[1] = particle[1] % box_leny
        particle[2] = particle[2] % box_lenz
        
    next_acceleration, p_E = ACCEL(next_pos, particle_mass)
    next_velocity = curr_velocity + (.5 * time_step * (curr_acceleration + next_acceleration))
    return (next_pos, next_velocity, p_E)

def MAIN(num_particles, time_step, number_iterations, box_lenx=8.0, box_leny=8.0, box_lenz=8.0, particle_mass=1):
    d_time = time_step
    volume = box_lenx * box_leny * box_lenz
    density = num_particles / volume

    total_E_list = []
    kin_E_list = []
    pot_E_list = []
    avgKin_E_list = []
    pair_corr_list = []
    equilib_kin_E_list = []
    curr_pos_matrix = initialize_coordinates.init_coord(num_particles ,box_lenx)

    acc_matrix = np.zeros_like(curr_pos_matrix)
    vel_matrix = np.zeros_like(curr_pos_matrix)
    #vel_matrix = calc_velocity.calc_vel(number_of_particles, temp)

    (acc_matrix, p_E) = ACCEL(curr_pos_matrix, particle_mass)

    k_E = 0.5 * (np.sum(np.square(vel_matrix)))
    total_E = k_E + p_E
    total_E_list.append(total_E)
    kin_E_list.append(k_E)
    pot_E_list.append(p_E)

    for i in range(number_iterations):
        curr_pos_matrix, vel_matrix, p_E = UPDATE(curr_pos_matrix, vel_matrix, time_step)
        k_E = 0.5 * (np.sum(np.square(vel_matrix)))
        total_E = k_E + p_E
        total_E_list.append(total_E)
        kin_E_list.append(k_E)
        pot_E_list.append(p_E)
        
        if(i * time_step <= 10):
            avgKin_E_list.append(None)
            
        if( i % 1000 == 0):
            print "Percent Complete: ", (i/float(number_iterations)) * 100

        if (i * time_step) > 10:
            equilib_kin_E_list.append(k_E)
            avgKin_E_list.append(np.sum(equilib_kin_E_list) / len(equilib_kin_E_list))
            bin_list, index_list = pair_correlation_fun(curr_pos_matrix)
            pair_corr_list.append(bin_list)


    #Optimize the PC Avg method. Low priority.
    pair_correlation_avg = pair_corr_list[0]

    for i in range(1, len(pair_corr_list)):
        pair_correlation_avg = np.add(pair_correlation_avg, pair_corr_list[i])

    pair_correlation_avg = np.divide(pair_correlation_avg, float(len(pair_corr_list)))

    pair_correlation_avg, index_list = pair_correlation_correction(pair_correlation_avg)

    print "Reduced T:", ((2./(num_particles * 3.)) * avgKin_E_list[-1])
    
    fig0 = plt.plot(index_list, pair_correlation_avg, "-o")
    plt.show()
    
    fig3 = plt.plot(avgKin_E_list, "-o")
    fig4 = plt.plot(total_E_list, "-o")
    fig5 = plt.plot(kin_E_list, "-o")
    fig6 = plt.plot(pot_E_list, "-o")
    plt.xlabel("Time Step")
    plt.ylabel("Energy")
    plt.title("Energy of two particle system")
    plt.show()


def MAIN_TEST():
    time_step = 0.01
    number_iterations = int(10 / 0.01)
    volume = 10.0 * 10.0 * 10.0
    
    total_E_list = []
    kin_E_list = []
    pot_E_list = []

    curr_pos_matrix = np.array([np.array([7.0, 6.0, 0.0]), np.array([3.0, 6.0, 0.0])])
    x1 = [curr_pos_matrix[0][0]]
    x2 = [curr_pos_matrix[1][0]]

    acc_matrix = np.zeros_like(curr_pos_matrix)
    vel_matrix = np.zeros_like(curr_pos_matrix)
    vel_matrix[1][0] = 4.0

    (acc_matrix, p_E) = ACCEL(curr_pos_matrix, 1.0)

    k_E = 0.5 * (np.sum(np.square(vel_matrix)))
    total_E = k_E + p_E
    total_E_list.append(total_E)
    kin_E_list.append(k_E)
    pot_E_list.append(p_E)

    for i in range(number_iterations):
        curr_pos_matrix, vel_matrix, p_E = UPDATE(curr_pos_matrix, vel_matrix, time_step)
        k_E = 0.5 * (np.sum(np.square(vel_matrix)))
        x1.append(curr_pos_matrix[0][0])
        x2.append(curr_pos_matrix[1][0])
        total_E = k_E + p_E
        total_E_list.append(total_E)
        kin_E_list.append(k_E)
        pot_E_list.append(p_E)
				
            
        if( i % 1000 == 0):
            print "Percent Complete: ", (i/float(number_iterations)) * 100
            
    fig1 = plt.plot(x1, "-o")
    fig2 = plt.plot(x2, "-o")
    plt.xlabel("Time Step")
    plt.ylabel("X Position")
    plt.title("Position of Two Particles")
    plt.show()

    fig4 = plt.plot(total_E_list, "-o")
    fig5 = plt.plot(kin_E_list, "-o")
    fig6 = plt.plot(pot_E_list, "-o")
    plt.xlabel("Time Step")
    plt.ylabel("Energy")
    plt.title("Energy of two particle system")
    plt.show()
    
MAIN_TEST()

MAIN(64, 0.005, int(15/0.005)) 
