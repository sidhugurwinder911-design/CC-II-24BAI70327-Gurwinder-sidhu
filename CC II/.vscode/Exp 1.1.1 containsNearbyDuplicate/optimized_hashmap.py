class Solution:

    def containsNearbyDuplicate(self, nums, k):

        seen = {}

        for i, num in enumerate(nums):

            if num in seen and i - seen[num] <= k:
                return True

            seen[num] = i

        return False


nums = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter k: "))

sol = Solution()
print(sol.containsNearbyDuplicate(nums, k))