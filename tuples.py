# Arrays are changeable. If, for some reason, you wanted an array but it couldn't be changed...
# enter tuples.

a_list = [1,2,3]
a_tuple = (1,2,3)
print a_list[2]
print a_tuple[2]

# python's cool with changing lists, but not tuples
a_list[2] = 4
print a_list[2]

# a_tuple[2] = 4 - this gets Python angry, it freaks out

for single_tuple in a_tuple:
	print single_tuple	