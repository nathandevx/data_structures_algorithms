# Resource: https://www.programiz.com/dsa/bubble-sort

# Explained: swap every element until sorted
# Subtract i: in the second loop because the elements at the end of the list are sorted,
# each i loop puts the largest element at the end of the loop, therefore there's no need to check it.
def bubble_sort(arr):
	size = len(arr)
	for i in range(size):  # loop through list
		for k in range(0, size - i - 1):  # loop to compare elements
			if arr[k] > arr[k + 1]:  # < to sort descending order
				arr[k + 1], arr[k] = arr[k], arr[k + 1]  # smallest, largest = largest, smallest


data = [5, 3, 2, 4, 1]
bubble_sort(data)
print(f'Sorted: {data}')
