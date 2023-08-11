#!/usr/bin/env python
# coding: utf-8

# # Question-2:Leap Year Checker 
# Write a program that asks the user to input a year and determines whether the year is a leap year or not. A leap year is either divisible by 4 but not by 100, or divisible by 400.
# 

# In[1]:


# Prompt the user to input a year
year = int(input("Enter a year: "))

# Check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")


# In[ ]:




