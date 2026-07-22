def search_all(nums, target):
    indices = []

    for i in range(len(nums)):
        if nums[i] == target:
            indices.append(i)

    return indices


# Driver Code
nums = list(map(int, input("Enter array elements: ").split()))
target = int(input("Enter target: "))

result = search_all(nums, target)

if result:
    print("Target found at indices:", result)
else:
    print("Target not found")