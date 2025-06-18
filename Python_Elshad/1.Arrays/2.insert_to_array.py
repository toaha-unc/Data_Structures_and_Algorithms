import array

my_array = array.array('i', [1,2,3])
my_array.insert(0,0) #index, element
print(my_array)

#Time Comp = O(N)
#Space Comp = O(1)