# Resource: https://www.programiz.com/dsa/linear-search
def linear_search(arr, x):
    for i, num in enumerate(arr):
        if num == x:
            return i
    return None


arr = [2, 4, 0, 1, 9]
result = linear_search(arr, 1)

if result:
    print(f"Element is at i = {result}")
else:
    print("Element not found")
