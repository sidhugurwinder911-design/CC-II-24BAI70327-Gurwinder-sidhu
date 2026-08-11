class Solution:
    def largestRectangleArea(self, heights):
        n = len(heights)
        max_area = 0

        # Choose every starting bar
        for i in range(n):
            min_height = heights[i]

            # Extend the rectangle to the right
            for j in range(i, n):
                min_height = min(min_height, heights[j])
                width = j - i + 1
                area = min_height * width

                max_area = max(max_area, area)

        return max_area


# Example
heights = [2, 1, 5, 6, 2, 3]
obj = Solution()
print("Largest Rectangle Area:", obj.largestRectangleArea(heights))