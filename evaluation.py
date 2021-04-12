#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from sklearn.metrics import mean_squared_error
from pylab import *
import matplotlib
import matplotlib.pyplot as plt


# In[ ]:

def get_rmse(r_pred, true_matrix):
    y_pred = r_pred[true_matrix>0]
    y_true = true_matrix[true_matrix>0]
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    return rmse 

def evaluation(pred_matrix, true_matrix):
    rmse = get_rmse(pred_matrix, true_matrix)
    return rmse

def figure(values_list, name=''):
    fig=plt.figure(name)
    x = range(len(values_list))
    plot(x, values_list, color='g',linewidth=3)
    plt.title(name + ' curve')
    plt.xlabel('Iterations')
    plt.ylabel(name)
    show()

