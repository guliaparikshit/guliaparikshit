#!/usr/bin/env python
# coding: utf-8
Using a while loop, verify if the number A is purely divisible by number B and if so then how many
times it can be divisible.
# In[72]:


a=int(input("enter the number a"))
b=int(input("enter the number b"))
if a%b==0:
    print("a is purely divisble by b")
else:
    print("a is not purely divisble by b")

Create a list containing 25 int type data. Using for loop and if-else condition print if the element is
divisible by 3 or not.
# In[36]:


z=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]


# In[69]:


for i in z:
    print(i)
if i%3==0:
    print("the number is divisible by 3")
else:
    print("the number is not divisible by 3")

What do you understand about mutable and immutable data types? Give examples for both showing
this property.mutable data types are basically the type of data types in which we can change something at a particular index. for example list is a mutable data type as shown below we created a list named it 'p'. now we want to change first element from 2 to 1 so we can change at particular index p[0] data available at 1st index is 2 replaced by 1.
# In[50]:


p=[2,3,45,6,"parikshit"]


# In[51]:


p[0]=1


# In[52]:


p

whereas immutable data types are basically the type of data types in which we cannot change something at a particular index. for example string is an immutable data type as shown below we created a string named it 's'. now we want to change first element from 's' to 'p' so we cannot change at particular index as string is immutable hence it will give an error.
# In[53]:


s="snake"


# In[55]:


s[0]=p


# In[ ]:




