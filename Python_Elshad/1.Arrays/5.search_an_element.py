import array

my_array = array.array('i', [1,2,3])

def linear_search(array, target): # return index
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1

print(linear_search(my_array, 2))

#Time Comp = O(N)
#Space Comp = O(1)