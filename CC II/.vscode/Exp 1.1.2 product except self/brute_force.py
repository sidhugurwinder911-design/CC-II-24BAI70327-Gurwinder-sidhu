##Prefix & suffix method to solve the problem of finding the product of all elements in an array except for the current element without using division.
class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n

        for i in range(1, n):
            answer[i] = answer[i - 1] * nums[i - 1]

        right = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right
            right *= nums[i]

        return answer


nums = list(map(int, input("Enter array elements: ").split()))

sol = Solution()

print("Output:", sol.productExceptSelf(nums))