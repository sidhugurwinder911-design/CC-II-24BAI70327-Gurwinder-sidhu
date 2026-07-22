def search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1


# Driver Code
nums = list(map(int, input("Enter array elements: ").split()))
target = int(input("Enter target: "))

print("Index:", search(nums, target))