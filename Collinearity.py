
# coding: utf-8

# ## Collinearity Check
# Collinearity for any three points can be determined easily by taking the determinant of a matrix containing the points.

# In[1]:


# Define Points (feel free to change these)
# By default these will be cast as int64 arrays
import numpy as np
p1 = np.array([1, 2])
p2 = np.array([2, 3])
p3 = np.array([3, 4])


# ### General Case
# 
# Define a function to determine collinearity using the `np.linalg.det()` function. Introduce the `epsilon` threshold to allow a tolerance for collinearity. If the determinant is less than `epsilon` then the points are collinear. 
# 

# In[5]:


def collinearity_float(p1, p2, p3, epsilon=1e-2): 
    collinear = False
    # TODO: Add a third dimension of z=1 to each point
    # TODO: Create the matrix out of three points
    # TODO: Calculate the determinant of the matrix. 
    # TODO: Set collinear to True if the determinant is less than epsilon
    mat = np.vstack((augm_point(p1),augm_point(p2),augm_point(p3)))
    det = np.linalg.det(mat)
    if np.abs(det)<epsilon:
        collinear = True
    return collinear
def augm_point(p):
    return np.array([p[0],p[1],1.])


# ### Integer Case
# Define a function to take three points and test for collinearity by evaluating the determinant using the simplified version for the 2D case:
# 
# $ det = x_1(y_2-y_3) + x_2(y_3-y_1) + x_3(y_1-y_2)$

# In[6]:


def collinearity_int(p1, p2, p3): 
    collinear = False
    # TODO: Calculate the determinant of the matrix using integer arithmetic 
    # TODO: Set collinear to True if the determinant is equal to zero
    det = p1[0]*(p2[1]-p3[1]) + p2[0]*(p3[1]-p1[1]) + p3[0]*(p1[1]-p2[1])
    if det == 0:
        collinear = True
    return collinear


# ### Test it and time it

# In[7]:


import time
t1 = time.time()
collinear = collinearity_float(p1, p2, p3)
t_3D = time.time() - t1

t1 = time.time()
collinear = collinearity_int(p1, p2, p3)
t_2D = time.time() - t1
print(t_3D/t_2D)


# ### Which one is faster ???

# Check the solution [here](/notebooks/Collinearity-Solution.ipynb).
