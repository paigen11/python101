# coding: utf-8
# Return the "centered" average of an array of ints, which we'll say is the mean 
# average of the values, except ignoring the largest and smallest values in the array. 
# If there are multiple copies of the smallest value, ignore just one copy, and likewise 
# for the largest value. Use int division to produce the final average. You may assume 
# that the array is length 3 or more.

# centered_average([1, 2, 3, 4, 100]) → 3
# centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
# centered_average([-10, -4, -2, -4, -2, 0]) → -3

def centered_average(new_list):
# step 1: sort the list from smallest to largest
	new_list.sort()

# step 2: eliminate the first and last number from the list
	# take off first element
	del new_list[0]
	# take off last element
	new_list.pop()

# step 3: if there a copies of a smallest or biggest number, ignore the dupes
	# determine if first and second element are equal and remove one if they are
	for i in range(0, len(new_list) - 1):
		if new_list[0] == new_list[1]:
			del new_list[0]
		# to remove dupes of largest values of new_list run a while loop (not done yet)
		# if new_list[len(new_list) -1] == new_list[len(new_list)-2]
		# 	new_list.pop()
		# while max(new_list) == (len(new_list) - 2):
		# 	new_list.pop
		# return new_list	

# step 4: sum up the remaining list and divide by number in list
	center_value = sum(new_list) / len(new_list)
	return center_value

print centered_average([1, 2, 3, 4, 100]) 
print centered_average([1, 1, 5, 5, 10, 8, 7]) 
print centered_average([-10, -4, -2, -4, -2, 0]) 

