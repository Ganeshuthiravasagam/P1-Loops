#!/usr/bin/env python
# coding: utf-8

# In[1]:


## Question 1

for i in range(2000, 3201):    
    if i%7==0 and i%5!=0:
        print(i, end = ",")
    


# In[2]:


## Question 2

First_name=input("Enter first name: ")
Last_name=input("Enter last name: ")
print(First_name[::-1], Last_name[::-1])


# In[4]:


## Question 3

Diameter = 12
r=Diameter/2
V=4/3*(3.14*(r**3))
print(V)


# In[ ]:




