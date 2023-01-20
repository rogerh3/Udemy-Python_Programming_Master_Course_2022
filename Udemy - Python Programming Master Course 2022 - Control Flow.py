#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Control Flow
# Udemy - Python Programming Master Course 2022
# Roger Hayden
# 12/14/2022


# # Control Flow

# # Conditional Statements

# In[2]:


# Example of a basic if, else statement
    # The colons are important to build a block within the conditions and the indentation is for the 
    # statement within the block 
age = 21
if(age >= 18):
    print("You are eligible to vote")
    print("Thank you for being interested in voting") # example of running 2 lines within a block
else:
    print("You are not able to vote")


# In[4]:


# Adding in elif (else if)
num = 3
if (num > 0):
    print("Your number is positive")
elif(num == 0):
    print("Your number is zero")
else:
    print("Your number is negative")


# # Nested If Else

# In[8]:


# Using a nested if else versus doing if, elif, else in this example
num = -2.3
if (num >= 0):
   if(num == 0):
        print("Your number is zero")
   else:
        print("Your number is positive")
else:
    print("Your number is negative")


# # Python Question - Finding the Largest Element between 3 Numbers

# In[12]:


# Example of a if statement that checks 3 numbers to see which value is the largest
# This method only works for a small number of comparisons before it becomes too lengthy
num1 = 50
num2 = 30
num3 = 40

largest = 0

if((num1 >= num2) and (num1 >= num3)):
    largest = num1
elif((num2 >= num1) and (num2 >= num3)):
    largest = num2
else:
    largest = num3
print("The largest number is: ", largest)


# # While Loop

# In[14]:


# Example - Printing even numbers from 1 to 20 

# initialize variable
i = 1 
# while loop and ending condition
while(i < 20):
    # inside while
    if(i%2 == 0):
        print(i) 
    
    # updating the variable
    i = i+1


# # For Loop

# In[5]:


# For loop to print 3 - 12
for i in range(3, 13):
    print(i)


# In[9]:


# Using a For Loop with Else
for i in range(2, 21):
    if(i % 2 == 0): # Printing only numbers divisible by 2 (or mod 2)
        print(i, end = ", ") # By using end = ", " the variables are all printed on one line
else:
    print()
    print("No Elements Left")


# In[13]:


# Using For to perform mathematical functions

n = 9 #Setting variable n to 9

for i in range (1, 11):
    print("{} x {} = {}".format(n, i, n*i))
else:
    print("Complete") # Print Complete when the mathematical operations are complete


# # Python Question - Pattern Printing

# In[18]:


# How to print the stars like they are displayed below using for loops

n = 5
# *
# **
# ***
# ****
# *****


for i in range(1, n+1): # Rows are n
    for j in range(1, i+1): # i is used to output the number of stars in a row
        print("*", end = " ") # Seperates the stars by spaces
        
    print(end = "\n") # Breaks the stars into the appropriate row


# In[23]:


# You can also use one for loop to create the same output
for i in range(1, n+1): 
    print("* " * (i))


# # Python Questions - Working on Loops

# Question 1: Given a variable n, calculate the sum of the first n numbers
# 
# i.e. n = 5, 1+2+3+4+5 = 15

# In[3]:


# n is the number of values chosen starting at 1
n = 3
# s will be the sum
s = 0

# We are beginning our range at 1 so for whatever number of values you want to use (n) we will get with n+1
for i in range(1, n+1):
    s += i # This will add the value of i each iteration, i is the range from 1 to n+1
    
print("The sum of the first {} numbers is {}".format(n,s))


# Question 2: Given a variable n, find if n is a prime number or not?

# In[6]:


# n is the value we are checking
n = 13

# Default prime to true
prime = True 

for i in range(2, n): # When using range n actually represents n-1 and n+1 represents n
    if(n % i == 0): # This checks to see if any number between 2 and n-1 is able to divide n
        # If this is true the number IS NOT PRIME
        prime = False
        
if(prime):
    print("{} is prime.".format(n))
else:
    print("{} IS NOT prime".format(n))


# # CODE CHALLENGE

# Find the sum of all odd numbers from 1 to N

# In[5]:


n = 10
s = 0

for i in range (1, n+1):
    if(i % 2 != 0):
        s += i
        
print(s)


# # Break, Continue and Pass

# Break and Continue can be used to alter the normal flow of a loop
# 
# - Break: Used to exit all coming iterations in a loop 
# - Continue: Skips the current iteration and moves to the next iteration 
# - Pass: If you want to keep the block as empty you can use pass

# In[7]:


# This is a normal loop that outputs 1 to 9
for i in range (1, 10):
    print(i)
else:
    print("No Elements Left")


# Using Break

# In[13]:


# If we USE BREAK within this loop above
for i in range(1,10):
    if(i==5):
        break # Implementing break here breaks the loop at 5 and then outputs the else string
    print(i)
    
else:
    print("No elements left")


# Using Continue

# In[14]:


# If we USE CONTINUE within this loop above
for i in range(1,10):
    if(i==5):
        continue # Implementing continue here skips the specified value which is 5 here
    print(i)
    
else:
    print("No elements left")


# Using Pass

# In[16]:


# By using pass here, we are able to bypass the syntax error and continue through the code
if(4 < 6):
    pass


# # CODE CHALLENGE

# You are given the distance and time, calculate the cab fare for the passenger using the following properties
# 
# - basePrice = 50Rs
# - freeKms = 5 Kms
# - perKm = 10Rs
# - freeMins = 15 minutes
# - perMins = 2Rs

# In[43]:


distance = 21
time = 40

price = 0

if (time < 15):
    print(50)
elif (distance < 5):
    print(50)
else:
    print((distance - 5)*(10)+(time - 15)*(2)+50)


# # CODE CHALLENGE

# You are given a number n, you have to print the factorial of n

# In[44]:


n = 5
factorial = 1

for i in range(1, n+1):
    factorial = factorial * i
    
print(factorial)


# # CODE CHALLENGE

# You are given an integer N, add all of the digits of N together

# In[45]:


from split import chop

N = 2534

def getSum(n):
    
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum
   
print(getSum(N))


# In[ ]:




