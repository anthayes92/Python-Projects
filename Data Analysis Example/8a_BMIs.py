# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 17:04:07 2018

@author: ant
"""

import pandas as pd
import seaborn as sns
from pylab import *
import pickle
import numpy as py

#==============================================================================
# Unpack BMI data
#==============================================================================

fileObj=open("sexCountriesBMI.pkl", 'rb')
x= pickle.load(fileObj)
del  x[0][''] # delete anomalous first entry
M=x[0] # split genders
F=x[1]
df_M=pd.DataFrame.from_dict(M) # create dataframes from dictionary
df_F=pd.DataFrame.from_dict(F)


#==============================================================================
# Organise and bin data
#==============================================================================

# Choose countries with most data for bouldering (i.e where bouyldering is most popular)
country_list = ["ESP", "ITA", "SWE", "POL", "FRA", "DEU", "GBR", "NOR", "AUT"]

# bin into "Underweight", "Healthy", "Overweight" and "Obese"
lbls = ["Under","Healthy", "Over", "Obese"]

# Split sexes
titleG = ["Women","Men"]


count = -1
D =[]
for G in [df_F,df_M]:
    count += 1
    u=[]
    h=[]
    ov=[]
    ob=[]
    for j in range(0,4):
        print lbls[j]
        for x in list(G.columns):
            if x not in country_list: continue
            n = len(G[x][j])/(1.0*len(G[x][0]) + len(G[x][1]) + len(G[x][2]) + len(G[x][3]))*100.0
            if j==0: u.append(n)
            elif j==1: h.append(n)
            elif j==2: ov.append(n)
            else: ob.append(n)
            if n == 0: continue
            print x, n
            print'---------'
            print u, h, ov, ob


    D.append({'Under': u, 'Healthy':h, 'Over':ov, 'Obese':ob})

    # make some basic plots (sanity check)

    fig, ax = plt.subplots()
    fig.set_size_inches(10, 3.27)
    locs, labels = plt.xticks()
    plt.setp(labels, rotation=67.5)
    ax.set_xticks(range(len((country_list))))
    ax.set_xticklabels(country_list, fontsize=10)
    ylim([0,105])
    plt.title(titleG[count])
    plt.ylabel('Population %')
    plt.xlabel('Country', labelpad=-1)

    ### Step Plot
    #plt.step(range(len((df_F.columns))), u_f, label='Underweight')
    #plt.step(range(len((df_F.columns))), h_f, label='Healthy')
    #plt.step(range(len((df_F.columns))), ov_f, label='Overweight')
    #plt.step(range(len((df_F.columns))), ob_f, label='Obese')
    #plt.legend()

    plt.step(range(len((country_list))), u, label='Underweight')
    plt.step(range(len((country_list))), h, label='Healthy')
    plt.step(range(len((country_list))), ov, label='Overweight')
    plt.step(range(len((country_list))), ob, label='Obese')
    plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.)



# creat file of fully cleaned and organised data
D.reverse()
pickle.dump(D,open("bmi_8a.pkl","wb"))



################
# More Checks
################

### Swarm Plot
#sns.swarmplot(x=[u'AND'], y=u_f[3], color='r', label='Underweight')
#sns.swarmplot(x=[u'AND'], y=h_f[3], color='g', label='Healthy')
#sns.swarmplot(x=[u'AND'], y=ov_f[3], color='b', label='Overweight')
#sns.swarmplot(x=[u'AND'], y=ob_f[3], color='k', label='Obese')
#plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.)
#
#sns.swarmplot(x=df_F.columns, y=u_f, color='r')
#sns.swarmplot(x=df_F.columns, y=h_f, color='g')
#sns.swarmplot(x=df_F.columns, y=ov_f, color='b')
#sns.swarmplot(x=df_F.columns, y=ob_f, color='k')

#sns.swarmplot(x=[u'USA'], y=u_f[0], color='r', label='Underweight')
#sns.swarmplot(x=[u'USA'], y=h_f[0], color='g', label='Healthy')
#sns.swarmplot(x=[u'USA'], y=ov_f[0], color='b', label='Overweight')
#sns.swarmplot(x=[u'USA'], y=ob_f[0], color='k', label='Obese')
#plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.)
#
#sns.swarmplot(x=country_list, y=u_f, color='r')
#sns.swarmplot(x=country_list, y=h_f, color='g')
#sns.swarmplot(x=country_list, y=ov_f, color='b')
#sns.swarmplot(x=country_list, y=ob_f, color='k')
