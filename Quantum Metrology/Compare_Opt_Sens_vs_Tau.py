# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 11:16:58 2017

@author: ant
"""


from pylab import *
from qutip import *
import matplotlib.pyplot as plt
import pickle

#########################################################################
# Load and plot data
#########################################################################

filename_list= ["data/data_tau_0.5","data/data_tau_0.6","data/data_tau_0.7","data/data_tau_0.8"
                ,"data/data_tau_0.9","data/data_tau_1.0"]


tau_list = []
t_s_opt_list = []
opt_sens_list = []
sim_t_s_opt_list=[]
sim_opt_sens_list=[]


for filename in filename_list:
    with open(filename, 'rb') as f:
        data = pickle.load(f)

        tau_list.append(data[3])
        t_s_opt_list.append(data[2])
        opt_sens_list.append(data[1])
        sim_t_s_opt_list.append(data[8])
        sim_opt_sens_list.append(data[7])


N = data[4]

f = plt.figure()
plt.plot(tau_list, N * array(tau_list)**2,
     label='Classical (scheme A) ', color='r')

#plt.plot(tau_list, t_s_opt_list, ls='--', marker='x', label='Seperable $t_s^{opt}$')
plt.plot(tau_list, opt_sens_list, ls='--', marker='x', label='Sequential (Scheme B)', color='b')

#plt.plot(tau_list, sim_t_s_opt_list, marker='o', label='Simultaneous $t_s^{opt}$')
plt.plot(tau_list, sim_opt_sens_list, marker='o', label='Simultaneous (Scheme C)', color='g')

#xlabel(r'Run Time $\tau$', fontsize=16)
#ylabel(r'Optimal Sensitivity $(\Delta\phi)^{-2}$', fontsize=16)
#legend(fontsize=12, loc=2, prop={'size': 10})

#plt.ylim(0,10**5)
plt.xlim(0.5,1.0)
plt.show()
f.savefig("foo2.pdf", bbox_inches='tight')
