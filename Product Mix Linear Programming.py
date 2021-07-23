#!/usr/bin/env python
# coding: utf-8

# In[13]:


# Import PuLP modeler functions
from pulp import *


# In[14]:


# defining the LP maximization problem type
prob = LpProblem("ProductMix", LpMaximize)


# In[15]:


# defining variable - LpVariable(variable name, lower Bound=None, uppper Bound=None, catagory='Continuous')
x1 = LpVariable("x1", lowBound=0) # Create a variable x1 >= 0
x2 = LpVariable("x2", lowBound=0) # Create another variable x2 >= 0


# In[16]:


# Objective Function
prob += 700*x1 + 900*x2


# In[17]:


# Constraints
prob += 3*x1 + 5*x2 <= 3600  # Wood
prob += 1*x1 + 2*x2 <= 1600  # Labor
prob += 50*x1 + 20*x2 <= 48000 #Machine


# In[26]:


# Display the LP problem
prob


# In[27]:


# Solve with the default solver
prob.solve()


# In[28]:


# Print the solution status
print("Status:", LpStatus[prob.status])


# In[29]:


# Show the solution (1st method)
value(x1), value(x2), value(prob.objective)


# In[30]:


# Show the solution (2nd method)
for v in prob.variables():
    print (v.name, "=", v.varValue)


# In[23]:


print ("objective=", value(prob.objective))    

