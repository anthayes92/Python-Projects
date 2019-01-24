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

filename_list=["data/data_tau_0.5","data/data_tau_1.0","data/data_tau_2.0","data/data_tau_4.0"]

i=0

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

    i=i+1

    if i==1:
      f = plt.subplot(221)
      plt.plot(t_s_list, 0.0*t_s_list + N * tau**2,
      label="Classical (scheme A) ", ls='--', color='gray')
      plt.plot(t_s_list, sensitivity_list, label=r'Sequential (shceme B)'.format(tau))
      plt.plot(t_s_list, sim_sensitivity_list, label=r'Simultaneous (scheme C)' )
      ylabel('$(\delta\omega)^{-2}$', fontsize=16)
      #f.set_ylim([0, 120])
      #xlabel(r'Sensing time $t_s$', fontsize=18)
      plt.title(r"$\tau=0.5$")
     # legend(fontsize=12, loc=10, prop={'size': 15})


    if i==2:
      f = plt.subplot(222)
      plt.plot(t_s_list, 0.0*t_s_list + N * tau**2,
      label="Classical (scheme A) ", ls='--', color='gray')
      plt.plot(t_s_list, sensitivity_list, label=r'Sequential (shceme B)'.format(tau))
      plt.plot(t_s_list, sim_sensitivity_list, label=r'Simultaneous (scheme C)' )
      #ylabel('$(\Delta\phi)^{-2}$', fontsize=16)
      #f.set_ylim([0, 450])
      #xlabel(r'Sensing time $t_s$', fontsize=18)
      #legend(fontsize=12, loc=2, prop={'size': 8}, title=r'For $\tau=6$')
      plt.title(r"$\tau=1$")

    if i==3:
      f = plt.subplot(223)
      plt.plot(t_s_list, 0.0*t_s_list + N * tau**2,
      label="Classical (scheme A) ", ls='--', color='gray')
      plt.plot(t_s_list, sensitivity_list, label=r'Sequential (shceme B)'.format(tau))
      plt.plot(t_s_list, sim_sensitivity_list, label=r'Simultaneous (scheme C)' )
      ylabel('$(\delta\omega)^{-2}$', fontsize=16)
      #f.set_ylim([0, 450])
      xlabel(r'Sensing time $t$', fontsize=18)
      #legend(fontsize=12, loc=2, prop={'size': 8}, title=r'For $\tau=6$')
      plt.title(r"$\tau=2$")

    if i==4:
      f = plt.subplot(224)
      plt.plot(t_s_list, 0.0*t_s_list + N * tau**2,
      label="Classical (scheme A) ", ls='--', color='gray')
      plt.plot(t_s_list, sensitivity_list, label=r'Sequential (shceme B)'.format(tau))
      plt.plot(t_s_list, sim_sensitivity_list, label=r'Simultaneous (scheme C)' )
      #ylabel('$(\Delta\phi)^{-2}$', fontsize=16)
      #f.set_ylim([0, 450])
      xlabel(r'Sensing time $t$', fontsize=18)
      #legend(fontsize=12, loc=2, prop={'size': 8}, title=r'For $\tau=6$')
      #f.set_xlim([0,1.2])
      plt.title(r"$\tau=4$")




subplots_adjust(hspace=0.3)
plt.show()

f.figure.savefig("foo3.pdf", bbox_inches='tight')
