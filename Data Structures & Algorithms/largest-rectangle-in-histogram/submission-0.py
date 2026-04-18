class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack_right = []
        stack_left = []
        right = [n - 1] * n
        left = [0] * n

        for i in range(n):
            while stack_right and heights[stack_right[-1]] > heights[i]:
                last_i = stack_right.pop()
                right[last_i] = i - 1
            stack_right.append(i)

            j = n - i - 1
            while stack_left and heights[stack_left[-1]] > heights[j]:
                last_j = stack_left.pop()
                left[last_j] = j + 1
            stack_left.append(j)
        
        res = 0
        for i, height in enumerate(heights):
            res = max(res, (right[i] - left[i] + 1) * height)
        
        return res