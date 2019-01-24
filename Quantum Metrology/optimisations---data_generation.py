# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 10:46:08 2017

@author: ant
"""


from pylab import *
from qutip import *
from state_evolution import final_state, sim_final_state, sensitivity, sim_sensitivity
import pickle
import timeit

start = timeit.default_timer()

#===============================================================================
# Initialize Parameters
#===============================================================================

N = 11 # numer of spins
chi = 1.0 # squeezing strength
tau_list=[0.5,0.6,0.7,0.8,0.9,1]  # time steps
psi_i = basis(N+1, N) # basis(N+1, N) is the 'all spins down' state

# collective spin operators
Jx=jmat(.5*N,'x')
Jy = jmat(0.5*N, 'y')
M = Jy


#===============================================================================
# Perform optimisation to generate data and save to file in data folder
#===============================================================================

i = 0
time_total = 0

for tau in tau_list:

    i = i + 1

    start = timeit.default_timer()

    dt = tau/100.0
    t_s_list = arange(0.0, tau, dt)

    sensitivity_list = [sensitivity(psi_i, M, N, chi, 0.5*(tau-t_s), t_s,
                        0.5*(tau-t_s), dt) for t_s in t_s_list]

    sim_sensitivity_list = [sim_sensitivity(psi_i, M, N, chi, 0.5*(tau-t_s), t_s,
                        0.5*(tau-t_s), dt) for t_s in t_s_list]

    opt_sensitivity = max(sensitivity_list)
        # the sensitivity, optimised over t_s

    sim_opt_sensitivity = max(sim_sensitivity_list)
        # the sensitivity for the simultaneous scheme, optimised over t_s

    t_s_opt = t_s_list[argmax(sensitivity_list)]
        # the value of t_s that gives the optimal sensivity

    sim_t_s_opt = t_s_list[argmax(sim_sensitivity_list)]
        # the value of t_s that gives the optimal sensivity

    data = [sensitivity_list, opt_sensitivity, t_s_opt, tau, N, t_s_list,
            sim_sensitivity_list, sim_opt_sensitivity, sim_t_s_opt]

    with open('data/data_tau_{}'
              .format(round(tau,5)), 'wb') as f:
        pickle.dump(data, f)

############################################################################
    # print time taken to produce data
    stop = timeit.default_timer()
    interval = stop - start
    time_total = time_total + interval
    print( str('{}/{} done'.format(i, len(tau_list))),
           time_total, str('seconds') )
