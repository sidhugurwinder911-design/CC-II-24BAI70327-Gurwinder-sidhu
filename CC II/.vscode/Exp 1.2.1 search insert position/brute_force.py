def search_insert(nums, target):
    # Traverse the array
    for i in range(len(nums)):

        # If target is found
        if nums[i] == target:
            return i

        # If target should be inserted before nums[i]
        if nums[i] > target:
            return i

    # If target is greater than all elements
    return len(nums)


# Driver Code
nums = [1, 3, 5, 6]
target = 7

result = search_insert(nums, target)
print("Insert Position:", result)