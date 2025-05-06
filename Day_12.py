#!/usr/bin/env python
# coding: utf-8

# # Introduction to Loops
# -Sometimes a programmer wants to execute a group of statements a certain number of times. This can be done using loops. Based on this loops are further classified into following main types;
# * for loop
# * while loop
# ### The for Loop:
# - for loops can iterate over a sequence of iterable objects in python. Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries.
# - Example: iterating over a string:

# In[1]:


name = "Samarth"
for i in name:
    print(i)


# In[11]:


name = "Samarth"
for i in name:
    print(i,end=",")


# In[15]:


name = "Samarth"
for i in name:
    print(i)
    if (i=="S"):
        print("This is Something Special")


# ### Example: iterating over a list:

# In[17]:


colors = ["Red", "Green", "Blue", "Yellow"]
for i in colors:
    print(i)


# In[19]:


Fruits = ["Apple","Chery", "Banana"]
for fruit in Fruits:
    print(fruit)


# In[21]:


#iterating over a list
Fruits = ["Apple","Chery", "Banana"]
for fruit in Fruits:
    print(fruit)
    for i in fruit:
        print(i)


# ### range():
# - What if we do not want to iterate over a sequence? What if we want to use for loop for a specific number of times?
# - Here, we can use the range() function.
# - Example:

# In[22]:


for k in range(5):
    print(k)


# In[23]:


for k in range(5):
    print(k+1)


# In[24]:


for k in range(1,9):
    print(k)


# In[27]:


for i in range(1,201):
    print(i)


# In[ ]:




