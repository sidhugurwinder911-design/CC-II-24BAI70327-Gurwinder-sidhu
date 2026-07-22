def search_insert(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        # Target found
        if nums[mid] == target:
            return mid

        # Search in the right half
        elif nums[mid] < target:
            left = mid + 1

        # Search in the left half
        else:
            right = mid - 1

    # Target not found; left is the insertion position
    return left


# Driver Code
nums = [1, 3, 5, 6]
target = 2

result = search_insert(nums, target)
print("Insert Position:", result)