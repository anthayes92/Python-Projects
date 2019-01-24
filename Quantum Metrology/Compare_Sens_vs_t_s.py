# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 11:03:03 2017

@author: ant
"""

from pylab import *
from qutip import *
import matplotlib.pyplot as plt
import pickle

#########################################################################
# Load and plot data
#########################################################################

filename_list=["data/data_tau_3.0"]

for filename in filename_list:

    with open(filename, 'rb') as f:
        data = pickle.load(f)

    sensitivity_list = data[0]
    opt_sensitivity = data[1]
    t_s_opt = data[2]
    tau = data[3]
    N = data[4]
    t_s_list = data[5]
    sim_sensitivity_list=data[6]
    sim_opt_sensitivity=data[7]
    sim_t_s_opt=data[8]

    title('$S_{{opt}} = {}$, '.format(round(opt_sensitivity,3)) +
          '$t_s^{{opt}} = {}$'.format(t_s_opt))

    f = plt.figure()
    plt.plot(t_s_list, 0.0*t_s_list + N * tau**2,
         label="Classical (scheme A)", ls=':', color='gray')
    plt.plot(t_s_list, sensitivity_list, ls='--', label=r'Sequential (scheme B)')
    plt.plot(t_s_list, sim_sensitivity_list, label=r'Simultaneous (scheme C)' )


    ylabel('Sensitivity $(\Delta\phi)^{-2}$', fontsize=16)
    xlabel(r'Sensing Time $t_s$', fontsize=18)
    legend(fontsize=12, loc=2, prop={'size': 10}, title=r'For $\tau=3$')

    plt.show()
    f.savefig("foo.pdf", bbox_inches='tight')
