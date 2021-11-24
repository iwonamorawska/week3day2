#!/usr/bin/env python
# coding: utf-8

# # Exercise #1
# Filter out all of the empty strings from the list below
# 
# Output: ['Argentina', 'San Diego', 'Boston', 'New York']

# In[60]:


places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]
def new_places(place):
    if place.strip()=="":
        return False
    else:
        return True 
more_new_places=list(filter(new_places, places))
print(more_new_places)


# # Exercise #2
# Write an anonymous function that sorts this list by the last name...
# Hint: Use the ".sort()" method and access the key"

# In[71]:


author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]
sorted_author=sorted(author, key=lambda x: x.split(" ")[-1].lower())
print(sorted_author)


# # Exercise #3
# Convert the list below from Celsius to Farhenheit, using the map function with a lambda...
# 
# Output: [('Nashua', 89.6), ('Boston', 53.6), ('Los Angelos', 111.2), ('Miami', 84.2)]

# In[83]:


# F = (9/5)*C + 32
places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]
f_places=list(map(lambda x,c :((float(9/5))*c+32), places))
print(f_places)


# # Exercise #4
# Write a recursion function to perform the fibonacci sequence up to the number passed in.
# 
# Output for fib(5) => 
# Iteration 0: 1
# Iteration 1: 1
# Iteration 2: 2
# Iteration 3: 3
# Iteration 4: 5
# Iteration 5: 8

# In[ ]:




