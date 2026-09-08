class Solution:
    def subsets(self, nums):
        result = []
        n = len(nums)

        # Generate all possible bitmasks
        for mask in range(1 << n):
            subset = []

            # Check each element
            for i in range(n):
                if mask & (1 << i):
                    subset.append(nums[i])

            result.append(subset)

        return result


# Main Program
nums = [1, 2, 3]

solution = Solution()
result = solution.subsets(nums)

print("=" * 50)
print("          ALL SUBSETS - BRUTE FORCE")
print("=" * 50)

print("Input :", nums)
print("Number of elements :", len(nums))
print("Total subsets      :", 2 ** len(nums))

print("\nAll Subsets:")
print("-" * 50)

for i, subset in enumerate(result, 1):
    print(f"{i}. {subset}")

print("-" * 50)
print("Total Subsets:", len(result))
print("=" * 50)