import numpy as np

my_array = np.array([ [1,2,3],[4,5,6] ])

def traverse(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

traverse(my_array)
