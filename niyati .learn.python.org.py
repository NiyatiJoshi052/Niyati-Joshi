#!/usr/bin/env python
# coding: utf-8

# # python program for condition.

# In[1]:


x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3)  # prints out True


# In[2]:


x = 2
if x == 2:
    print(" x equls two!")
else:
    print(" x does not equal to two.")


# # python program for loops.

# In[3]:


primes = [2,3,5,7]
for prime in primes:
    print(prime)


# In[4]:


# prints out 0,1,2,3,4

count = 0
while count < 5:
    print(count)
    count += 1 # This is the same as count = count + 1


# # python program for string formatting.

# In[6]:


# This prints out: A list: [1,2,3]
mylist = [1,2,3]
print("A list: %s" % mylist)


# In[ ]:




