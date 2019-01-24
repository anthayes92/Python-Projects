# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 12:23:16 2018

@author: ant
"""
import matplotlib.gridspec as gridspec
import pickle
import numpy as np
from pylab import *

import pandas as pd
import seaborn as sns

import itertools

#==============================================================================
# Load in cleaned BMI data
#==============================================================================

# retrieve cleaned 8a data
fileObj1=open("bmi_8a.pkl", 'rb')
eight_a= pickle.load(fileObj1)

# split into male and female
u8a_m = eight_a[0]  # dictionaries indexed by "Healthy", "Obese","Over","Under"
u8a_f = eight_a[1]


# retrieve cleaned cleaned EU data
fileObj2=open("eu_bmi_m.pkl", 'rb')
eu_m= pickle.load(fileObj2)

fileObj3=open("eu_bmi_f.pkl", 'rb')
eu_f= pickle.load(fileObj3)


# labels of countries with most bouldering data (i.e countries in which bouldering is most popular)
country_list_8a = ["ESP", "ITA", "SWE", "POL", "FRA", "DEU", "GBR", "NOR", "AUT"]
country_list = ["ES ", "IT ", "SE ", "PL ", "FR ", "DE ", "UK ", "NO ", "AT "]

#print u8a_m, u8a_f, eu_m, eu_f

#==============================================================================
# Plot results
#==============================================================================

colors = itertools.cycle(["r", "b", "g","k"])
sns.set_style("darkgrid")
L1 = [u8a_m,u8a_f]
L2 = [eu_m, eu_f]
for X in [0,1]:
    g_u= L1[X]
    g_e = L2[X]
    fig = plt.figure()

    gs = gridspec.GridSpec(2,2)
    ax2=plt.subplot(gs[:,1])
    ax0=plt.subplot(gs[0,0])
    ax1=plt.subplot(gs[1,0], sharex=ax0)
    plt.setp(ax0.get_xticklabels(), visible=False )


    ax0.set_xticks(np.arange(0,len((country_list_8a)),1))
    ax0.set_xticklabels(country_list_8a, fontsize=10)
    #labels = ax0.get_xticks()
    #plt.setp(labels, rotation=67.5)
    ax0.set_ylabel('% of 8a Users\n ' )
    ax0.set_title(['BMI of Males\n','BMI of Females\n'][X])
    ax0.scatter(range(len(country_list_8a)), g_u['Under'], marker="x",color=next(colors),label='Underweight')
    ax0.scatter(range(len(country_list_8a)), g_u['Healthy'],marker="x",color=next(colors), label='Healthy')
    ax0.scatter(range(len(country_list_8a)), g_u['Over'],marker="x", color=next(colors),label='Overweight')
    ax0.scatter(range(len(country_list_8a)), g_u['Obese'],marker="x",color=next(colors), label='Obese')
    ax0.set_ylim([-5,100])
    #ax0.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.)

    ax1.set_xticks(np.arange(0.0,len((country_list_8a)),1))
    ax1.set_xticklabels(country_list_8a, fontsize=10)
    ax1.set_ylabel('%' )
    ax1.set_ylabel('% of General EU Pop.\n (2014)')
    ax1.scatter(range(len((country_list))), g_e['Under'], marker="x",color=next(colors),label='Underweight')
    ax1.scatter(range(len((country_list))), g_e['Healthy'],marker="x",color=next(colors), label='Healthy')
    ax1.scatter(range(len((country_list))), g_e['Over'],marker="x",color=next(colors), label='Overweight')
    ax1.scatter(range(len((country_list))), g_e['Obese'], marker="x",color=next(colors),label='Obese')
    #ax1.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.)
    ax1.set_ylim([-5,100])

    ax2.set_xticks(np.arange(0.0,len((country_list_8a)),1))
    ax2.set_xticklabels(country_list_8a, fontsize=10)

    ratio_g_u = np.array(g_u['Under'])/np.array(g_e['Under'])
    ratio_g_h = np.array(g_u['Healthy'])/np.array(g_e['Healthy'])
    ratio_g_o = np.array(g_u['Over'])/np.array(g_e['Over'])
    ratio_g_ob = np.array(g_u['Obese'])/np.array(g_e['Obese'])

    ax2.set_title('BMI Ratio of "8a" Users to EU\n')
    ax2.scatter(range(len((country_list))), ratio_g_u,marker="x", color=next(colors),label='Underweight')
    ax2.scatter(range(len((country_list))), ratio_g_h,marker="x",color=next(colors),label='Healthy')
    ax2.scatter(range(len((country_list))), ratio_g_o,marker="x",color=next(colors), label='Overweight')
    ax2.scatter(range(len((country_list))), ratio_g_ob,marker="x", color=next(colors),label='Obese')
    ax2.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.)
    if X==0: ax2.set_ylim([-0.2,6])
    else: ax2.set_ylim([-0.2,12])

    for ax in fig.axes:
        matplotlib.pyplot.sca(ax)
        plt.xticks(rotation=67.5)
    plt.tight_layout()
    plt.show()
    fig.savefig("foo.pdf", bbox_inches='tight')
