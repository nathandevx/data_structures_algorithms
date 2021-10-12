# Can be N num elements
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# O(1)
def simple_func(array):
	total = 0  # O(1)
	return total  # O(1)


# O(N)
def find_sum(array):
	total = 0  # O(1)
	for num in array:  # O(N)
		total += 1  # O(1)
	return total  # O(1)


# O(N^2)
def find_sum2d(array):
	total = 0  # O(1)
	for row in array:  # O(N)
		for col in row:  # O(N)
			total += col  # O(1)
	return total  # O(1)


# O(2N) aka O(N)
def print_all_items_twice(items):
	for item in items:
		print(item)

	for item in items:
		print(item)


# O(2N) aka O(N)
def print_all_numbers_then_all_pair_sums(numbers):
	for number in numbers:
		print(number)

	for first_number in numbers:
		for second_number in numbers:
			print(first_number + second_number)


# O(1+n/2+100) aka O(N)
def print_first_item_then_first_half_then_say_hi_100_times(items):
	print(items[0])

	middle_index = len(items) / 2
	index = 0
	while index < middle_index:
		print(items[index])
		index += 1

	for time in range(100):
		print("hi")
