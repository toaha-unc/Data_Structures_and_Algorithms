import array

my_array = array.array('i', [1,2,3,4,5])

def traverse_array(array):
    for i in my_array:
        print(i)

traverse_array(my_array)

#Time Comp = O(N)
#Space Comp = O(1)