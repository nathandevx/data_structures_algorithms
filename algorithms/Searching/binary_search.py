# Resource: https://www.programiz.com/dsa/binary-search
def binary_search(arr, x, low, high):
    """
    :param arr: the list
    :param x: find this number
    :param low: beginning index of list i=0
    :param high: ending index of list i=len(arr)-1
    :return: x index value if found, -1 otherwise
    """
    while low <= high:
        mid = low + (high - low)//2  # 1 // 2 = 0
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:  # if mid is less than x, move low to the right of mid
            low = mid + 1
        else:
            high = mid - 1  # if mid is greater than x, move high to the left of mid
    return None


array = [1, 2, 3, 4, 5]
x = 4

result = binary_search(array, x, 0, len(array)-1)  # minus 1 because if the list is even then we want the leftmost mid number

if result:
    print(f"Element is at i = {result}")
else:
    print("Element not found")
