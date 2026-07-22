class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)

        answer = [1] * n

        # Prefix Product
        for i in range(1, n):
            answer[i] = answer[i - 1] * nums[i - 1]

        # Suffix Product
        right = 1

        for i in range(n - 1, -1, -1):
            answer[i] *= right
            right *= nums[i]

        return answer


# Driver Code
nums = list(map(int, input("Enter array elements: ").split()))

sol = Solution()

print("Output:", sol.productExceptSelf(nums))