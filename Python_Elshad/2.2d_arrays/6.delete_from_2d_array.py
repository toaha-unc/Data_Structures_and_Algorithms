import numpy as np

my_array = np.array([ [1,2,3],[4,5,6] ])

my_array2 = np.delete(my_array, 0, axis=0)
#parameters (array_to_delete_from, position to delete_from, row(0) or column(1))

    
            

print(my_array2)

#Time Comp: O(m * n)
#Space Comp: O(m * n) 