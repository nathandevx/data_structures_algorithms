# Resource: https://www.programiz.com/dsa/selection-sort

# Explained: "the element of i" is assumed to be the smallest number,
# if a smaller number is found it will replace "the element of i"
def selection_sort(arr):
	size = len(arr)
	for i in range(size):  # loop through list
		low_num = i
		for k in range(i + 1, size):  # loop to compare low num with every other element
			if arr[k] < arr[low_num]:  # > to sort in ascending order
				low_num = k
		arr[i], arr[low_num] = arr[low_num], arr[i]  # smallest, largest = largest, smallest


data = [5, 3, 2, 4, 1]
selection_sort(data)
print(f'Sorted: {data}')