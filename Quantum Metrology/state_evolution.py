# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 10:37:47 2017

@author: ant
"""

from pylab import *
from qutip import *

#########################################################################
# Functions
#########################################################################

def final_state(psi_i, N, chi, w, t_p, t_s, t_r, dt, c_op_list = []):

    """
    This returns the final state after the echo measurement scheme.

    Input
    -----

    psi_i : the initial state
    N : number of spins
    chi : strength of the squeezing term in the Hamiltonian
    w : the strength of the rotation term in the Hamiltonian
    t_p : the preparation time
    t_r : the readout time
    dt : the numerical time increment

    """

    Jx = jmat(0.5*N, 'x') # Collective spin operators
    Jy = jmat(0.5*N, 'y')
    Jz = jmat(0.5*N, 'z')

    H_s = w * Jy # Sensing Hamiltonian
    H_chi = chi * Jx**2  # Squeezing Hamiltonian

    t_list_p = linspace(0.0, t_p, max(1,int(t_p/dt)))
        # this is the list of times for the prep stage.
        # the number of elements is the maximum of 1 and t_p/dt
    t_list_s = linspace(t_p, t_p + t_s, max(1,int(t_s/dt)))
        # the list of times for the sensing stage
    t_list_r = linspace(t_p + t_s, t_p + t_s + t_r, max(1,int(t_r/dt)))
        # the list of times for the readout stage

    states_p = mesolve(H_chi, psi_i, t_list_p, c_op_list, []).states
        # the list of states during the prep stage
    states_s = mesolve(H_s, states_p[-1], t_list_s, c_op_list, []).states
        # the list of states during the sensing stage
    states_r = mesolve(-H_chi, states_s[-1], t_list_r, c_op_list, []).states
        # the list of states during the readout stage.
        # the last state in this list is the final state

    return states_r[-1] # the "[-1]" index refers to the last entry in the list
                        # it's like counting from right-to-left

def sim_final_state(psi_i, N, chi, w, t_p, t_s, t_r, dt, c_op_list = []):

    """
    This returns the final state after the simultaneous prep-sense-readout.
    """

    Jx = jmat(0.5*N, 'x') # Collective spin operators
    Jy = jmat(0.5*N, 'y')
    Jz = jmat(0.5*N, 'z')

    H_p = (w * Jy) + (chi * Jx**2 ) # Preparation Hamiltonian
    H_s = w * Jy # Sensing Hamiltonian
    H_r = (w * Jy) - (chi * Jx**2 ) # Readout Hamiltonian

    t_list_p = linspace(0.0, t_p, max(1,int(t_p/dt)))
        # this is the list of times for the prep stage.
        # the number of elements is the maximum of 1 and t_p/dt
    t_list_s = linspace(t_p, t_p + t_s, max(1,int(t_s/dt)))
        # the list of times for the sensing stage
    t_list_r = linspace(t_p + t_s, t_p + t_s + t_r, max(1,int(t_r/dt)))
        # the list of times for the readout stage

    sim_states_p = mesolve(H_p, psi_i, t_list_p, c_op_list, []).states
        # the list of states during the prep stage
    sim_states_s = mesolve(H_s, sim_states_p[-1], t_list_s, c_op_list, []).states
        # the list of states during the sensing stage
    sim_states_r = mesolve(H_r, sim_states_s[-1], t_list_r, c_op_list, []).states
        # the list of states during the readout stage.
        # the last state in this list is the final state

    return sim_states_r[-1] # the "[-1]" index refers to the last entry in the list
                        # it's like counting from right-to-left

def sensitivity(psi_i, M, N, chi, t_p, t_s, t_r, dt, dw = 1e-6):

    """
    This returns the sensitivity.

    Input
    -----

    psi_i : the initial state
    M : the observable we'd like to measure at the very end
    N : number of spins
    chi : strength of the squeezing term in the Hamiltonian
    w : the strength of the rotation term in the Hamiltonian
    t_p : the preparation time
    t_r : the readout time
    dt : the numerical time increment
    dw : the 'infinitesimal' increment of w for calculating the derivative
         default is set to 1e-6

    """

    if t_s > 0.1/dw:
        print('Warning: you might need to decrease dw')

    M_plus = expect(M, final_state(psi_i, N, chi, dw, t_p, t_s, t_r, dt))
    M_minus = expect(M, final_state(psi_i, N, chi, -dw, t_p, t_s, t_r, dt))

    dM_dw = (M_plus - M_minus) / (2 * dw)
        # derivative of expecation value of M with respect to w

    Var_M = 0.25 * N
        # variance of M in the final state when w = 0 and t_p = t_r

    return dM_dw**2 / Var_M

def sim_sensitivity(psi_i, M, N, chi, t_p, t_s, t_r, dt, dw = 1e-6):

    """
    This returns the sensitivity for the simultanoues scheme.

    """

    if t_s > 0.1/dw:
        print('Warning: you might need to decrease dw')

    sim_M_plus = expect(M, sim_final_state(psi_i, N, chi, dw, t_p, t_s, t_r, dt))
    sim_M_minus = expect(M, sim_final_state(psi_i, N, chi, -dw, t_p, t_s, t_r, dt))

    sim_dM_dw = (sim_M_plus - sim_M_minus) / (2 * dw)
        # derivative of expecation value of M with respect to w

    Var_M = 0.25 * N
        # variance of M in the final state when w = 0 and t_p = t_r

    return sim_dM_dw**2 / Var_M
