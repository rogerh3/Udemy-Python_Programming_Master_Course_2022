#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Python Basics
# Udemy - Python Programming Master Course 2022
# Roger Hayden


# # Variables and Identifiers

# Print Statements

# In[2]:


print("Hello")


# In[3]:


print("Python", "Data Science", 100)


# Variables

# In[4]:


# Setting the variable i
i = 42


# In[5]:


print(i)


# In[7]:


# Checking the data type of i
type(i)


# Location of a Variable

# In[9]:


# Looking at the memory location of the variable i
id(i)


# Dynamic Variable Changes

# In[10]:


# Variables in Python are Dynamic and can be changed/updated easily
i = "Coding Minutes"
print(i)


# In[11]:


type(i)


# In[12]:


id(i)


# Reviewing Data Types

# In[16]:


# You can do this for each data type and variable
num = 55
print(num, ",", type(num))


# Taking Input from the User

# In[17]:


name = input("Enter your name: ")


# In[18]:


print(name)


# Data Type Casting

# In[19]:


num = "8"
print(num, type(num))


# In[21]:


# Casting the num variable with the int data type
num = int(num)
print(num, type(num))


# In[25]:


# Collecting a input from the user while casting it to be an integer
age = int(input("What is your age: "))


# In[26]:


print(age, type(age))


# Python Statements

# In[27]:


# You can use a \ when doing multiline Python statements
a = 1+2+3+4+    5+6+7+8
print(a)


# In[28]:


# You can also use ()
b = (1+2+3+4+
    5+6+7+8)
print(b)


# Output Formatting

# In[29]:


a = 10
b = 20

# Default method of using .format
print("The value of a is {} and b is {}.".format(a,b))


# In[30]:


# We can also assign positions to each bracket
print("The value of a is {0} and b is {1}.".format(a,b))


# In[31]:


# Another option using variable assignments
print("The value of a is {a} and b is {b}.".format(a = a,b = b))


# In[ ]:




