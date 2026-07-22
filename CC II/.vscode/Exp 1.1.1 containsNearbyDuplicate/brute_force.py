class Solution:
    def containsNearbyDuplicate(self, nums, k):

        n = len(nums)

        for i in range(n):

            for j in range(i + 1, n):

                if nums[i] == nums[j] and abs(i - j) <= k:
                    return True

        return False

nums = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter k: "))

sol = Solution()
print(sol.containsNearbyDuplicate(nums, k))