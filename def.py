def quick_sort(list):
	less = []
	equal = []
	greater = []

	if len(list) > 1:
		pivot = list[0]
		for i in list:
			if i < pivot:
				less.append(i)
			if i == pivot:
				equal.append(i)
			if i > pivot:
				greater.append(i)
		return quick_sort(less) + equal + quick_sort(greater)
	else:
		return list


print quick_sort([1, 5, 7, 2, 4])