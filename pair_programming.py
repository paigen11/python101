# coding: utf8

# Write a function that takes a list of numbers as a parameter. Return the sum of all the numbers. 
# Bonus: Add an error handler that returns the message, “The list must include only numbers” if 
# any non-numbers are included. You will need to research a means to tell what data type an element is.

nums = [1,2,3,4]

def sum_of_numbers(nums):
	sum = 0
	for i in nums:
		try: 
			sum += i
		except TypeError:
			print "the list must only include numbers"
	return sum

print sum_of_numbers(nums)


# Write a function that will take a list of numbers and returns all combinations of those numbers. 
# Print them off to the screen on a new line.
  
# Bonus: Do permutations

import itertools
stuff = [1,2,3, 4, 5, 6]
for L in range(0, len(stuff)+1):
	for subset in itertools.combinations(stuff, L):
		print (subset)

iterables = [1, 2, 3]

from itertools import permutations
for p in permutations(iterables):
	print(p)

# 3.    Choose one of the array sorting algorithms:
# a.    bubble sort
# b.    selection sort
# c.    merge sort
# d.    quick sort
# and implement it.

def bubble_sort(array):
	n = len(array)-1
	swapped = True
	while n > 0:
		swapped = False
		for i in range(n):
			if array[i] > array[i + 1]:
				swapped = True
				temp = array[i]
				array[i] = array[i + 1]
				array[i + 1] = temp
		n = n - 1

array = [4, 3, 1, 2, 5, 7, 6, 234, 62, 2342342, 224, 1, 3]
bubble_sort(array)
print(array)

unsorted_list = [64, 25, 12, 22, 11]
def quick_sort(list):
	lower = []
	higher = []
	equal = []

	if len(list) > 1:
		pivot = list[0]
		for i in list:
			if i < pivot:
				lower.append(i)
			if i == pivot:
				equal.append(i)
			if i > pivot:
				higher.append(i)
		return quick_sort(lower) + equal + quick_sort(higher)
	else:
		return list

print quick_sort(unsorted_list)							
