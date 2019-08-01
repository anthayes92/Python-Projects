import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import *
import random
from scipy.stats import norm
from sklearn import preprocessing

#plt.interactive(True) # toggle plots in ipython

df=pd.read_csv('saf.csv') # read in data from .csv to pandas dataframe
rows = len(df.index)

# create function for checking numerical data
def check_numeric_data(col,data_type):
    """ Bespoke function to loacate unexpected data types
    Args:
        col = column of DataFrame (string)
        data_type = the expected instance of the individual data objects (int64 or float)
    """
    m = df[col].mean()
    s = df[col].std()

    count = 0
    wrong_type, anom, zero = [], [], []

    for d in df[col]:
        if not isinstance(d,data_type): # check for wrong data types/missing data
            wrong_type.append(count)
        elif d<0.0 or abs(d-m)>5*s: # check for negative or anomalous data points (greater than 5-sigma)
            anom.append(count)
        elif d==0:
            zero.append(count) # check for zeros
        count+=1

    if wrong_type == []:
        wrong_type = None

    if anom == []:
        anom = None

    if zero == []:
        zero = None

    indicies_of_potential_errors = {'type error':wrong_type, 'anomalies':anom, 'zeros': zero} # dictionary of bad data types

    print('Indicies of potentially erronous data points: {}'.format(indicies_of_potential_errors))
    return indicies_of_potential_errors

#===============================================
# Plot correlation matrix of numerical data
#===============================================
# In order to get a high level understanding of the correlations
# within the numerical data we can plot a correlation matrix of numerical data.
# This helps determine the data that is worth feeding to the ML algo

corrmat = df.corr()
k = 9 # number of variables for heatmap
cols = corrmat.nlargest(k, 'Surface_FR')['Surface_FR'].index # we are interested in how data correlates to "SurfaceFR" of molecules
cm = corrcoef(df[cols].values.T)
sns.set(font_scale=1.25)
hm = sns.heatmap(cm, cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size': 10}, yticklabels=cols.values, xticklabels=cols.values)
#plt.show()

df = df.drop(['Molecule_type',  'h1_len',  'h2_len',  'h3_len',  'l1_len',  'l2_len',  'l3_len'],axis=1)

#========================================================
# Plot Surface_FR vs. categrocial data vs numerical data
#=======================================================
# Since we can’t calculate correlations between numerical and categorical data
# we can plot bar charts to get an indication of correlation

plot=sns.barplot(x='Position', y='Surface_FR', palette="ch:.25", data=df)
plot=sns.catplot(x='AA', y='Surface_FR', palette="ch:.25", data=df)
#plt.show()

################################################################################
# Split data
################################################################################
# In order to train, test and validate the ML algo, we must split the available data set accordingly

n_train = int(0.75*rows) # number of data points for training = 75% of total dataset (75324)
n_val = int((rows - n_train)/2) # number of data poins for validation = 12.5% of total dataset (12554)
n_test =  n_val # # number of data points for testing = 12.5% of total dataset (12554)
# create dataframes:
df_train = df.loc[0:n_train + n_val]
df_test = df.loc[n_train + n_val+2: n_train + n_val + n_test]

################################################################################
# One-hot-encode categorical features
################################################################################
# To feed the neural net categorical data, we must encode it to a “numerical alphabet”
# The method used here is one-hot encoding

# create dataframe of catagorical variables
categoricals = df.drop(['Surface_FR',],axis=1)
AA_and_Position = df.drop(['Surface_FR','VHF', 'VLF', 'Chains'],axis=1)

# encode labels with value between 0 and n_classes-1.
le = preprocessing.LabelEncoder()

# use df.apply() to apply le.fit_transform to all columns
f_t = categoricals.apply(le.fit_transform)

# 1. Instantiate
enc = preprocessing.OneHotEncoder()
# 2. Fit
enc.fit(f_t)
# 3. Transform
onehotlabels = enc.transform(f_t).toarray()
