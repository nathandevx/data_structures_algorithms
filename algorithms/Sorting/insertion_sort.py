# Resource: https://www.programiz.com/dsa/insertion-sort
# Explained: Compare the key with each element on left until a smaller one is found,
# then put the key to the right of the smaller one
def insertion_sort(arr):
	for i in range(1, len(arr)):
		key = arr[i]
		k = i - 1
		while k >= 0 and key < arr[k]:  # key>arr[k] = descending order,
			arr[k + 1] = arr[k]  # make key = k
			k -= 1  # go left
		arr[k + 1] = key  # if you can't go left anymore, tghen


data = [5, 3, 2, 4, 1]
insertion_sort(data)
print(f'Sorted: {data}')
