#!/usr/bin/env python
# coding: utf-8

# # python program to of classes and objects.

# In[1]:


class Myclass:
    variable = "blah"
    
    def function(self):
        print("This is a message inside the class.")
        
myobjectx = Myclass()
myobjecty = Myclass()

myobjecty.variable = "yackity"

# Then print out both values
print(myobjectx.variable)
print(myobjecty.variable)


# # python program for function.

# In[4]:


# Define our 3 functions
def my_function():
    print("Hello From My Function!")
    
def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))
    
def sum_two_numbers(a, b):
    return a + b

# print(a simple greeting)
my_function()

# print - "Hello, John Doe, From My Function!, I wish you a great year!"
my_function_with_args("John Doe","a great year!")

# after this line x will hold the value 3!
x = sum_two_numbers(1,2)
    


# # python program for basic string operation.

# In[5]:


astring = "Hello world!"
print(astring.upper())
print(astring.lower())


# In[6]:


astring = "Hello world!"
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))


# In[ ]:




