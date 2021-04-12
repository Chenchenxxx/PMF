#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np


# In[ ]:


def data_propress(file):
    user_id,item_id=0,0
    users,rated_items={},{}
    rated_info=[]
    f=open(file)
    for line in f.readlines():
        if '::' in line:
            u, i, r, _ = line.split('::')
        else:
            u, i, r, _ = line.split()
    
        if int(u) not in users.keys():
            users[int(u)]=user_id
            user_id+=1
        if int(i) not in rated_items.keys():
            rated_items[int(i)]=item_id
            item_id+=1
        rated_info.append([users[int(u)],rated_items[int(i)],float(r)])
    
    f.close()
    user_c,item_c=user_id,item_id
    return user_c,item_c, rated_info, rated_items

def user_item_matrix(user_c,item_c, rated_info):
    matrix=np.zeros([user_c,item_c])
    info_array = np.array(rated_info)
    matrix[info_array[:,0].astype(int),info_array[:,1].astype(int)]=info_array[:,2].astype(np.float32)
    return matrix


# In[2]:





# In[ ]:




