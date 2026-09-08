class Solution:
    def subsets(self, nums):
        result = []

        def backtrack(start, current):
            # Add current subset
            result.append(current[:])

            # Try remaining elements
            for i in range(start, len(nums)):
                # Choose
                current.append(nums[i])

                # Explore
                backtrack(i + 1, current)

                # Backtrack
                current.pop()

        backtrack(0, [])

        return result


# Main Program
nums = [1, 2, 3]

solution = Solution()
result = solution.subsets(nums)

print("=" * 50)
print("        ALL SUBSETS - BACKTRACKING")
print("=" * 50)

print("Input              :", nums)
print("Number of elements :", len(nums))
print("Total subsets      :", 2 ** len(nums))

print("\nAll Subsets:")
print("-" * 50)

for i, subset in enumerate(result, 1):
    print(f"{i}. {subset}")

print("-" * 50)
print("Total Subsets:", len(result))
print("=" * 50)