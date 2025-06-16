#create an array 
import array # only can create primitive data type arrays

#create an empty array
my_array = array.array('i')
print(my_array)

#create a non-empty array
my_array1 = array.array('i', [1,2,3,4])
print(my_array1)

#create a numpy array (can create arrays of any types)
import numpy as np 

#create an empty numpy array
my_array2 = np.array([], dtype=int) #need to mention type for empty array
print(my_array2)

#create a non-empty numpy array
my_array3 = np.array([1,2,3,4])

#Time & Space complexity for empty array is O(1)
#Time & Space complexity for non-empty array is O(N)