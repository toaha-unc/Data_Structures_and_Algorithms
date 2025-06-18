from array import *

my_array = array('i', [1,2,3])
print(my_array)
my_array1 = array('i', [4,5,6])
print(my_array1)
my_array.extend(my_array1)
print(my_array)