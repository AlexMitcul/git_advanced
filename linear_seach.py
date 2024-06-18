def linear_search(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return index  # Return the index of the target element
    return -1  # Return -1 if the target element is not found

# Example usage:
arr = reversed([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
target = 7
result = linear_search(arr, target)
if result != -1:
    print(f"Element {target} is at index {result}")
else:
    print(f"Element {target} is not in the array")

