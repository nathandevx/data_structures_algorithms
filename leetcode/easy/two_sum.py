"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
"""


def two_sum(nums, target):
	for i1, num1 in enumerate(nums):
		for i2, num2 in enumerate(nums):
			if i1 == i2:
				continue
			if (num1 + num2) == target:
				return i1, i2


# nums = [2,7,11,15]
# target = 9

# nums = [3, 2, 3]
# target = 6

# nums = [3, 3]
# target = 6

print(two_sum(nums, target))
