#!/usr/bin/env python
# coding: utf-8

# # Python program to print hello world!!

# In[1]:


print("Hello Niyati Joshi")
print("Enrollment no 180630107021")


# # python program to add two numbers.

# In[6]:


a=int(input("enter the 1st number"))
b=int(input("enter the 2nd number"))
c=a+b
print("answer is:",c)
print("Niyati Joshi")
print("Enrollment is : 180630107021")


# # python program to find square root.

# In[7]:


a=input("Enter number:")
r=float(a)**0.5;
print("answer is:",r)
print("Niyati Joshi")
print("Enrollment no : 180630107021")


# # python program to calculate area of triangle.

# In[8]:


b=input("enter the base :")
h=input("enter the height :")
area=(0.5 * float(h) * float(b))
print("answer is :",area)
print("Niyati Joshi")
print("Enrollment is : 180630107021")


# # python program to solve quadratic equation.

# In[11]:


from math import sqrt

print("Quadratic function : (a * x^2)  + b*x + c")
a= float(input("a: "))
b= float(input("b: "))
c= float(input("c: "))

r = b**2 - 4*a*c

if r > 0:
    num_roots = 2
    x1 = (((-b) + sqrt(r))/(2*a))
    x2=  (((-b) - sqrt(r))/(2*a))
    print("There are 2 roots: %f and %f" % (x1, x2))
elif r == 0:
    num_roots =1
    x =(-b) / 2*a
    print("There is one root:", x)
else:
    num_roots = 0
    print("No roots, discriminant < 0,")
    exit()
    
print("Niyati Joshi")
print("Enrollment is : 180630107021")
    
    
          


# # python program to swap two variables.

# In[12]:


a=input("enter 1st number:")
b=input("enter 2nd number:")
print("1st number :",a)
print("2nd number :",b)

temp=a
a=b
b=temp
print("after swapping")
print("1st number :",a)
print("2nd number :",b)
print("Niyati Joshi")
print("Enrollment no : 180630107021")


# # python program to generate a random number.

# In[22]:


import random

print(random.randint(0,9))
print("Niyati Joshi")
print("Enrollment number: 180630107021")


# # python program to convert kilometers to Miles.

# In[24]:


kilometers=float(input("enter value in km:"))
f=0.621371
miles=kilometers*f
print(miles)
print("Niyati Joshi")
print("Enrollment number: 180630107021")


# # python program to convert celsius To fahrenheit.
# 

# In[25]:


celsius = float(input("enter celsius:"))
fahrenheit = (celsius * 1.8) + 32
print(fahrenheit)
print("Niyati Joshi")
print("Enrollment number: 180630107021")


# In[ ]:




