import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.preprocessing import StandardScaler # Used for scaling of data
from sklearn.model_selection import train_test_split
from keras.models import Sequential # model creation
from keras.layers import Dense, Dropout # model components
from keras import metrics, regularizers # performance measures
import matplotlib.pyplot as plt # visulisation
from keras import backend as K
from keras.wrappers.scikit_learn import KerasRegressor
from preprocess import *
import time

# plt.interactive(True) # toggle plots in ipython

# =======================================
# Import and scale the preprocessed data
# =======================================
X_train = onehotlabels[0:n_train + n_val+1,:] # training data

scale = StandardScaler() # Always standardise-scale the data before using NN (i.e normalise s.t mean=0 var=1)
X_train = scale.fit_transform(X_train)

y = df_train['Surface_FR'].values
seed = 7
np.random.seed(seed) # use this value to seed the model
# split into 67% for train and 33% for validation
X_train, X_val, y_train, y_val = train_test_split(X_train, y, test_size=0.33, random_state=seed)

t1=time.time() # start timer

#===============================================================================
# Build the Nueral Network
#===============================================================================
def create_model():
    model = Sequential() # define a sequential model
    model.add(Dense(64, input_dim=X_train.shape[1], activation='relu')) # the 1st layer of densely connected of neurons
    model.add(Dropout(0.2)) # this layer is added during the tuning process, it reduces the number of connections between neurons in these layers (by 20%)
    model.add(Dense(32, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(40, activation='relu'))
    model.add(Dense(1))  # the final layer; a single nueron which gives a value in the range [0,1]
    # Compile model
    model.compile(optimizer ='adam', loss = 'mean_squared_error',
              metrics =[metrics.mae])
    return model

model = create_model()
model.summary() # prints a summary of model architecture in terminal

history = model.fit(X_train, y_train, validation_data=(X_val,y_val), epochs=100, batch_size=150) # this is where the model training is instantiated

print('=============================================')
print("Time taken to generate and run model: %s s " % round((time.time() - t1),2) )
print('=============================================')
print(' ')
print(' ')

#=================================================
# Time-stamp and save the trained model parameters
#=================================================
localtime=time.localtime()
timestamp=time.strftime(' %b-%d-%Y_%H:%M:%S', localtime)
filepath='./model_params/'
model.save(filepath + timestamp)

#=================================================
# Generate plots for model performance evaluation
#=================================================
t2 = time.time()
# summarize history for accuracy
plt.figure(1)
plt.plot(history.history['mean_absolute_error'])
plt.plot(history.history['val_mean_absolute_error'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'validate'], loc='upper left')

# summarize history for loss
plt.figure(2)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'validate'], loc='upper left')

#=============================================
# Test Model and use Model to Make Predictions
#=============================================
X_test = onehotlabels[n_train + n_val+2:,:] # encoded test data
scale = StandardScaler() # Again, always standard scale the data before using NN!
X_test = scale.fit_transform(X_test)

predictions = model.predict(X_test) # use the trained model to make pedictions on the test data
y_test = df_test['Surface_FR'].values # these are the "true" values, the model perfomance is essentially the doffernce between this and the predicted values

#===========================================================
# Define statistical measures to test the model performance
#===========================================================
# while predefined performance metrics exist, it is staightfoward to calculate
# statistical measures of accuracy to provide low level testing

pred_mean = predictions.mean()
test_mean = y_test.mean()
pred_sd = predictions.std()
test_sd = y_test.std()

# Calculate and build a list of "absolute errors" between test and prediction data points
test_predictions, pred_ae = [], []
error_count,i = 0, 0
for p in predictions:
    test_predictions.append(float(p))
    dist = abs( y_test[i] - float(p) )
    i+=1
    pred_ae.append(dist)
    if dist >= 2*test_sd:
        error_count+=1

test_label = [l for l in y_test]

# Common performance metrics of ML algos
mae = sum(pred_ae)/len(pred_ae) # calculate mean absolute error
sqr_ae_pred=[i**2 for i in pred_ae] # calculate square absolute error
mse = (sum(sqr_ae_pred))/len(pred_ae) # calculate mean squae error

#errors = {'In total': error_count,'As a percentage': 100*error_count/len(predictions) }

#===========================================================
# Plot Test Results
#===========================================================
plt.figure(3)
plt.scatter(y_test[0:1000], test_predictions[0:1000])
lineStart=0
lineEnd = max(test_predictions)
plt.plot([lineStart, lineEnd], [lineStart, lineEnd], 'k-')
plt.xlabel('True Values')
plt.ylabel('Predictions')
plt.axis('equal')
plt.axis('square')
plt.title('First 1000 datapoints of Surface_FR')
plt.show()
# lazy terminal output for model dev
print('--------------------------------------------------------------------------------------------')
print('Model Performance Metrics:')
print('--------------------------------------------------------------------------------------------')
print('  ')
print('Statistical moments of predicted vs. true Surface-FR:')
print("Predited mean of Surface-FR = {}".format(pred_mean))
print("True mean of Surface-FR = {}".format(test_mean))
print('  ')
print("Predicted standard deviation of Surface-FR = {}".format(pred_sd))
print("True standard deviation of Surface-FR = {}".format(test_sd))
print('  ')
print('Accuracy measures of predictions:')
print("Mean Absolute Error = {}".format(mae))
print("Mean Square Error = {}".format(mse))
print('  ')
# print('Errors (greater than 2*sigma)')
# print(errors)
# print('  ')
print('--------------------------------------------------------------------------------------------')
print(' ')
print(' ')
print('=======================================================')
print("Time taken evaluate model and generate plots: %s s " % round((time.time() - t2),2) )
print('=======================================================')
