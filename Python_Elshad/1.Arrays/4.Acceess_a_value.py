import array

my_array = array.array('i', [1,2,3])

def access_element(array, index):
    if index > len(array)-1:
        print('No element at this index')
    else:
        print(array[index])

access_element(my_array, 2)

#Time Comp = O(1)
#Space Comp = O(1)