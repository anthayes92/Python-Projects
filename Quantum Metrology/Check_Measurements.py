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


filename_list= ["data/data_tau_0.5","data/data_tau_1.0","data/data_tau_2.0","data/data_tau_4.0","data/data_tau_8.0"
                 ,"data/data_tau_16.0"]

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

f, ax = plt.subplots()
ax.set_xscale('log', basex=2)
ax.set_yscale('log', basey=10)
plt.semilogy(tau_list, N * array(tau_list)**2,
     label='Classical (scheme A)', color='r')
#plt.plot(tau_list, t_s_opt_list, ls='--', marker='x', label='Seperable $t_s^{opt}$')
ax.plot(tau_list, opt_sens_list, ls='--', marker='x', label='Sequential (scheme B)',color='b')

#plt.plot(tau_list, sim_t_s_opt_list, marker='o', label='Simultaneous $t_s^{opt}$')
ax.plot(tau_list, sim_opt_sens_list, marker='o', label='Simultaneous (scheme C)',color='g')


ax.set_ylim([0, 13000])
ax.set_xlim([0, 16.2])

xlabel(r' Run Time $\tau$', fontsize=18)
ylabel(r' Optimal Sensitvity $(\delta\omega^{opt})^{-2}$', fontsize=18)
legend(fontsize=12, loc=2, prop={'size': 10})

#plt.ylim(0,10**5)
plt.show()
f.savefig("foo2.pdf", bbox_inches='tight')
