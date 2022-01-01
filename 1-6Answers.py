#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("QUESTION # 1 \n")
print("Twinkle,twinkle,little star,")
print("        " + "How i wonder what you are")
print("               " + "Up above the world so high,")
print("               " + "like a diamond in the sky.")
print("Twinkle,twinkle,little star,")
print("        " + "How i wonder what you are")


# In[3]:


print("\nQuestion # 2 \n")

import platform
print(platform.python_version())


# In[9]:


print("\nQuestion # 3 \n")
import datetime
currentdtime = datetime.datetime.now()
print("Current date & time:" + currentdtime.strftime("%d-%m-%Y %H:%M:%S"))


# In[12]:


print("\nQuestion # 4 \n")

pivalue = 3.14
r = float(input("Input the value of Radius of the Circle: "))
area = pivalue * r * r
print("Area of the Circle is " + str(area));


# In[13]:


print("\nQuestion # 5 \n")
firstname = input("Input your First Name: ")
lastname= input("Input your Last Name: ");
print(lastname + " " + firstname)


# In[14]:


print("\nQuestion # 6 \n")
a = input("Input the first value:")
b = input("Input the second value:")
a = int(a)
b = int(b)
c = a + b
print("Result is " + str(c))


# In[ ]:




