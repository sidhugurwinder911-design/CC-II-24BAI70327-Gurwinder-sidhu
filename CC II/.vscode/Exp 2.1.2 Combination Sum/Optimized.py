class Solution:
    def combinationSum(self, candidates, target):
        result = []

        # Sort for early pruning
        candidates.sort()

        def backtrack(start, current, remaining):
            # Target reached
            if remaining == 0:
                result.append(current[:])
                return

            # Try candidates from start index
            for i in range(start, len(candidates)):

                # Pruning
                if candidates[i] > remaining:
                    break

                # Choose
                current.append(candidates[i])

                # Reuse same candidate
                backtrack(i, current, remaining - candidates[i])

                # Backtrack
                current.pop()

        backtrack(0, [], target)

        return result


# Main Program
candidates = [2, 3, 5]
target = 8

solution = Solution()
result = solution.combinationSum(candidates, target)

print("=" * 55)
print("       COMBINATION SUM - OPTIMIZED BACKTRACKING")
print("=" * 55)

print("Candidates :", candidates)
print("Target     :", target)

print("\nValid Combinations:")
print("-" * 55)

if result:
    for i, combination in enumerate(result, 1):
        print(f"{i}. {combination}  -> Sum = {sum(combination)}")
else:
    print("No valid combinations found.")

print("-" * 55)
print("Total Combinations:", len(result))
print("=" * 55)