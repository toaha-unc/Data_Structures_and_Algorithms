import numpy as np

my_array = np.array([ [1,2,3],[4,5,6] ])

def search(array, target):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == target:
                return [i,j]
    return -1
    
            

print(search(my_array, 6))

#Time Comp: O(m * n)
#Space Comp: O(1) 