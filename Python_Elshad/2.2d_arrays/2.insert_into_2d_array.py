import numpy as np

my_array = np.array([[1,2,3], [4,5,6]])

#my_array2 = np.insert(my_array, 0, [7,8,9], axis=0)
#parameters (array_to_add_to, position to add, array_to_add, row(0) or column(1))


#another_way (append adds to the end of the array)
my_array2 = np.append(my_array, [[7,8,9]], axis=0)

print(my_array2)

#Time Comp: O(m * n)
#Space Comp: O(m * n) 