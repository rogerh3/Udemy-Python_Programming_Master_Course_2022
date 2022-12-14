#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Operators and Expressions
# Udemy - Python Programming Master Course 2022
# Roger Hayden
# 12/13/2022


# # Operators and Expressions

# Arithmetic Operators

# In[11]:


# Adding Numbers
num1 = 12
num2 = 3

add = num1 + num2
print("a + b = {}".format(add))


# In[19]:


# Displaying other Arithmetic Operations
sub = num1 - num2
mul = num1 * num2
div = num1 / num2
f_div = num1 // num2 #Floor Division
exp = num1 ** num2
mod = num1 % num2


# In[20]:


print("a - b = {}".format(sub))
print("a * b = {}".format(mul))
print("a / b = {}".format(div))
print("a // b = {}".format(f_div))
print("a ** b = {}".format(exp))
print("a % b = {}".format(mod))


# Comparison Operators

# In[21]:


print(num1, num2)


# In[23]:


# Responds with a Boolean True or False
print(num1 > num2)


# In[27]:


# Examples of Comparison Operators
print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)
print(num1 == num2)
print(num1 != num2)


# Logical Operators

# In[30]:


# and example
# Returns a Boolean Result
(10 > 5) and (20 != 3)


# In[31]:


# or example
# Returns a Boolean Result
(10 > 5) or (20 != 3)


# In[32]:


# not example - negates the result that is originally obtained within the not grouping
# Returns a Boolean Result
not((10 > 5) and (20 != 3))


# Bitwise Operators

# In[34]:


# Returns the Binary of 10
# Result is 1010
bin(10)


# In[36]:


# Returns Binary of 4
# Result is 0100
bin(4)


# In[37]:


# Bitwise & of 10 with 4
# Max value in any column can be 1, so the result ends up being 0
10 & 4


# In[38]:


# Bitwise | of 10 and 4
# If any column contains a 1 then the 1 is kept, if all options are 0 then you just keep a 0
# Then you calculate the power of each position to get what the total is based off of position
# Result in Binary is 1110 which changes to 2^3 + 2^2 + 2^1 + 2^0 = 14
10 | 4


# In[40]:


# Bitwise xor 4 with 4
# xor means if you have:
    # 0 0 then you return 0
    # 0 1 or 1 0 then you return 1
    # 1 1 then you return 0
# This can not have multiple of the same value in the column
4^4


# Assignment Operators

# In[46]:


# Assigning a value to "a"
a = 5
print(a)


# In[47]:


# Incrementing a by 1
a = a + 1
print(a)


# In[48]:


# Also incrementing a by 1
a += 1
print(a)


# In[49]:


# Incrementing a by multiplication of 2
a *= 2
print(a)


# Multiple Assignments

# In[50]:


a, b, c = "ML", 34, 0.3
print(a, b, c)


# In[51]:


# Assigning numerous variables to the same values
a = b = c = 7
print(a, b, c)


# Special Operators

# In[52]:


my_str = "Good Morning"


# In[54]:


# Checking if Good is in my string
"Good" in my_str


# In[55]:


# Checking if Bad is in my string
"Bad" in my_str


# In[56]:


# Checking if Bad is NOT in my string
"Bad" not in my_str


# In[57]:


a = 5000
b = 300


# In[58]:


id(a)
id(b)


# In[60]:


# Checking if a is b, or if a and b have the SAME LOCATION (NOT VALUE)
a is b


# In[62]:


# Checking if a IS NOT b
a is not b


# In[ ]:




