def linear_search(arr, target):
    """
    Iterates through the list to find the target element.
    Returns the index if found, otherwise returns -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Element found, return its index
    return -1  # Element not found after checking the whole list

# --- Example Usage ---
numbers = [10, 23, 4, 90, 50, 45]
target_value = 90

result = linear_search(numbers, target_value)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the list")
    