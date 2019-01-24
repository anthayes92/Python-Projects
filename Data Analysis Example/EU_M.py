# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 10:57:39 2018

@author: ant
"""
import pickle
import seaborn as sns
from pylab import *
import pandas as pd

#==============================================================================
# Organise and bin data
#==============================================================================

# Create DataFrame
df = pd.read_csv('EU.csv', sep='\t', header=0)

# Choose countries with most data for bouldering (i.e where bouyldering is most popular)
country_list = ["ES ", "IT ", "SE ", "PL ", "FR ", "DE ", "UK ", "NO ", "AT "]

# bin into "Underweight", "Healthy", "Overweight" and "Obese"
u_eu=[]
h_eu=[]
ov_eu=[]
ob_eu=[]

for i in range(0,4):
    #print i
    for j in country_list:
        if i==3: u_eu.append(df[j][i])
        elif i==0: h_eu.append(df[j][i])
        elif i==1: ov_eu.append(df[j][i])
        else: ob_eu.append(df[j][i])
pickle.dump({"Under":u_eu, "Healthy":h_eu, "Over":ov_eu, "Obese":ob_eu},open("eu_bmi_m.pkl","wb"))


fig, ax = plt.subplots()
fig.set_size_inches(10, 3.27)
locs, labels = plt.xticks()
plt.setp(labels, rotation=67.5)
ax.set_xticks(range(len((country_list))))
ax.set_xticklabels(country_list, fontsize=10)
ylim([0,105])
#plt.title(titleG[count])
plt.ylabel('Population %')
plt.xlabel('Country', labelpad=-1)

### Step Plot
#plt.step(range(len((df_F.columns))), u_f, label='Underweight')
#plt.step(range(len((df_F.columns))), h_f, label='Healthy')
#plt.step(range(len((df_F.columns))), ov_f, label='Overweight')
#plt.step(range(len((df_F.columns))), ob_f, label='Obese')
#plt.legend()

plt.step(range(len((country_list))), u_eu, label='Underweight')
plt.step(range(len((country_list))), h_eu, label='Healthy')
plt.step(range(len((country_list))), ov_eu, label='Overweight')
plt.step(range(len((country_list))), ob_eu, label='Obese')
plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.)
