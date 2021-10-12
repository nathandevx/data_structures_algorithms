def partition(array, low, high):
	pivot = array[high]  # rightmost element as pivot
	i = low - 1  # largest element pointer

	for j in range(low, high):  # compare each element with pivot
		if array[j] <= pivot:
			i += 1
			array[i], array[j] = array[j], array[i]  # i is larger

	array[i + 1], array[high] = array[high], array[i + 1]  # swap pivot with i (larger)
	return i + 1  # return position where partition is done


def quick_sort(array, low, high):
	if low < high:
		# Find pivot element such that
		# Element smaller than pivot are on the left
		# Element larger than pivot are on the right
		pi = partition(array, low, high)
		quick_sort(array, low, pi - 1)  # left of pivot
		quick_sort(array, pi + 1, high)  # right of pivot


data = [5, 2, 7, 6, 3, 1, 9, 4, 8]
quick_sort(data, 0, len(data) - 1)
print(f'Sorted: {data}')
