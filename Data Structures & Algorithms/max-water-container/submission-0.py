class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1

        max_water = 0
        while i < j:
            min_height = min(heights[i], heights[j])
            max_water = max(max_water, min_height * (j-i))

            if heights[i] > heights[j]:
                j -= 1
            elif heights[i] < heights[j]:
                i += 1
            else:
                if i+1 == j:
                    i += 1
                else:
                    if heights[i+1] > heights[j-1]:
                        i += 1
                    elif heights[i+1] < heights[j-1]:
                        j -= 1
                    else:
                        i += 1
        
        return max_water
