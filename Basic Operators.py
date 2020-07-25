#!/usr/bin/env python
# coding: utf-8

# In[1]:


number = 1 + 2 * 3 / 4.0
print(number)


# In[2]:


remainder = 11 % 3
print(remainder)


# In[3]:


squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)


# In[4]:


helloworld = "hello" + " " + "world"
print(helloworld)


# In[5]:


lotsofhellos = "hello" * 10
print(lotsofhellos)


# In[6]:


even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)


# In[7]:


print([1,2,3] * 3)


# In[9]:


x= object()
y= object()

# TODO: change this code
x_list = [x]
y_list = [y]
big_list = []

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
    if big_list.count(x) == 10 and big_list.count(y) == 10:
            print("Great!")
        
    
    


# In[ ]:





# In[ ]:




