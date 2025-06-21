import numpy as np

my_array= np.array([[1,2,3], [4,5,6]])
print(my_array)

def accessElements(array, rowIndex, colIndex) -> None:
    if rowIndex >= len(array) or colIndex >= len(array[0]):
        print("Incorrent index")
    else:
        print(array[rowIndex][colIndex])

accessElements(my_array, 0,0)

#Time Comp: O(1)
#Space Comp: O(1) 