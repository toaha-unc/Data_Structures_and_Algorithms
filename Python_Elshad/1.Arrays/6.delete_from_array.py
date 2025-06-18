import array

my_array = array.array('i', [1,2,3])

my_array.remove(1)

print(my_array)

#Time Comp = O(N), removing not at end
#            O(1) removing at end
#Space Comp = O(1)