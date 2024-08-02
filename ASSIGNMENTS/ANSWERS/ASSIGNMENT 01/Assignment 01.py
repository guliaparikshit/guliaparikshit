#!/usr/bin/env python
# coding: utf-8

# In[1]:


#ASSIGNMENT 01

Create one variable using following data types
string
list
float
tuple
# In[2]:


a="parikshit"


# In[3]:


a


# In[4]:


type(a)


# In[5]:


b=[1,3,5,6,8,9,"parikshit",]


# In[6]:


b


# In[7]:


type(b)


# In[8]:


c=234.345


# In[9]:


c


# In[10]:


type(c)


# In[11]:


d=(2,4,5)


# In[12]:


d


# In[13]:


type(d)

Checking the data types of the given variables
var1 = ‘ ‘
var2 = ‘[ DS , ML , Python]’
var3 = [ ‘DS’ , ’ML’ , ‘Python’ ]
var4 = 1
# In[14]:


a=''


# In[21]:


type(a)


# In[22]:


b='DS,ML,Python'


# In[23]:


type(b)


# In[25]:


c=['DS','ML','Python']


# In[26]:


type(c)


# In[27]:


d=1


# In[28]:


type(d)

Explain the use of following opeartors using examples
/
%
//
**/ is an arithmetic operator used for division as shown below 10 on division with 2 gives 5 .
# In[34]:


10/2

% is also an arithmetic operator further classified as remainder operator , as given below 2 completely divides 10 so answer is zero.
# In[30]:


10%2

// it is a division floor it rounds the result to nearest whole number , as given below basically quotient that is 3 as 3*3 is 9 on further dividing it will result in points so its rounding off till 3 only.
# In[32]:


11//3

** it is an power operator used for solving power questions or someething related as it basically tells u the power of the number and how many times , as given below power of 2 , 3 times is 2*2 which is 4 further*2 which is 8. 2**3 = 2*2*2
# In[35]:


2**3

Create a list of length 10 of your choice containing multiple types of data. Using for loop print the
element and its data type.
# In[36]:


z=[1,2,3,4,5,'parikshit',5+7j,True,13.54,100]


# In[44]:


z


# In[45]:


for i in z:
    print(i)


# In[46]:


for i in z:
    print(i)
    print(type(i))

