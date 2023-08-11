#!/usr/bin/env python
# coding: utf-8

# # Question-1: Number Range Checker 
# Write a program that prompts the user to enter a number. Check whether the number falls within any of the following ranges:
# 0-10: "Low Range"
# 11-50: "Medium Range"
# 51-100: "High Range"
# Outside of 0-100: "Out of Range"

# In[1]:


# Prompt the user to enter a number
number = float(input("Enter a number: "))

# Check the number against different ranges
if number >= 0 and number <= 10:
    print("Low Range")
elif number >= 11 and number <= 50:
    print("Medium Range")
elif number >= 51 and number <= 100:
    print("High Range")
else:
    print("Out of Range")


# In[ ]:




