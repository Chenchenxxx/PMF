#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import random
import math
from data_pre import *
from evaluation import *


# In[6]:


class PMF():
    def __init__(self, 
                 train_data,            
                 test_data,             
                 user_c,                     # 就是N:the number of user
                 item_c,                     # 就是M:the number of item
                 K=10,                  # K: the number of latent factor
                 learning_rate=0.001,   
                 lamda1=0.1, # lamda_u
                 lamda2=0.1, # lamda_v
                 max_iter=50    
                ):
        self.train_data = train_data
        self.test_data = test_data
        self.user_c = user_c
        self.item_c = item_c
        self.K = K
        self.learning_rate = learning_rate
        self.lamda1 = lamda1
        self.lamda2 = lamda2
        self.max_iter = max_iter
    
    def update(self, u, v, r, learning_rate, lamda1, lamda2):
        #误差
        error = r - np.dot(u.T,v)    
        #更新u v
        Eu = error * v - lamda1 * u #偏导        
        Ev = error * u - lamda2 * v        
        u = u + learning_rate * Eu #更新u
        v = v + learning_rate * Ev
        loss = 0.5 * math.pow(error, 2) + 0.5 * lamda1 * (np.square(u).sum()) + 0.5 * lamda2 * (np.square(v).sum())
        return u, v, loss
    
    def prediction(self, U, V):
        user_c,K = U.shape
        rates_pred=[]
        for u in range(user_c):
            rates_pred.append(np.sum(U[u,:]*V, axis=1))
        return np.array(rates_pred)
    
    def train(self):
        train_matrix = user_item_matrix(self.user_c, self.item_c,self.train_data)
        test_matrix = user_item_matrix(self.user_c, self.item_c,self.test_data)

        U = np.random.normal(0, 0.1, (self.user_c, self.K)) #正态分布
        V = np.random.normal(0, 0.1, (self.item_c, self.K))

        results = []
        for step in range(self.max_iter):
            loss=0
            for data in self.train_data:
                u,i,r = data
                U[u],V[i],ls = self.update(U[u], V[i], r, self.learning_rate, self.lamda1, self.lamda2)
                loss += ls
            pred_matrix = self.prediction(U,V)
            train_rmse = evaluation(pred_matrix, train_matrix)
            test_rmse = evaluation(pred_matrix, test_matrix)
            results.append(np.array([loss, test_rmse]))

            if step % 5 ==0:
                print('step:{}  loss:{},  train_rmse:{},  test_rmse:{}'.format(step,loss,train_rmse,test_rmse))
        return U, V, np.array(results)
   
    #top K电影推荐
    def topK(self, U, V, user_id):
        pred_matrix = self.prediction(U, V)
        indexs = np.argsort(-pred_matrix[user_id,:])  #top 5
        indexs = indexs[0:5]
        print('user id : ' + str(user_id))
        for i in range(len(indexs)):
            print('No.' + str(i) + ' movie recommended, rate : ' + str(pred_matrix[user_id, indexs[i]]))

        
        
                      
    


# In[ ]:




