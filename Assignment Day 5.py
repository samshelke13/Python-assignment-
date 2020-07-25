#!/usr/bin/env python
# coding: utf-8

# In[1]:


list1=[0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]


# In[2]:


list1.sort(reverse=1)


# In[3]:


print(list1)


# In[5]:


list1=[10,20,40,60,70,80]
list2=[5,15,25,35,45,60]


# In[7]:


res=list1+list2


# In[11]:


for each in range(5,81):
    if each in res:
        print(each,end=",")


# In[ ]:




