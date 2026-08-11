class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0

        heights.append(0)   # Dummy bar

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                area = height * width
                max_area = max(max_area, area)

            stack.append(i)

        heights.pop()   # Remove dummy bar
        return max_area


# Different Input
heights = [4, 2, 7, 3, 5, 6]

obj = Solution()
print("Histogram:", heights)
print("Largest Rectangle Area:", obj.largestRectangleArea(heights))