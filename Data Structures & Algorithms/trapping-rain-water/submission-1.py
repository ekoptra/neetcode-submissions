class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = 0

        while l < len(height) and height[l] == 0:
            l += 1
            r += 1
        
        left_highest = l

        total_area = 0
        total_checkpoint = 0
        while r < len(height):

            while r + 1 < len(height) and height[r] >= height[r+1]:
                r += 1
            
            if r + 1 == len(height):
                break

            while r + 1< len(height) and height[r] <= height[r+1]:
                r += 1
            
            if height[r] >= height[left_highest]:
                l = left_highest

            min_height = min(height[l], height[r]) 
            area = min_height  * (r - l)

            substract_val = 0
            while l < r:
                l += 1
                substract_val += min(min_height, height[l])
                
            curr_area = area - substract_val
            
            if height[r] >= height[left_highest]:
                left_highest = r
                total_area -= total_checkpoint
                total_checkpoint = 0
            else:
                total_checkpoint += curr_area

            total_area += curr_area

        return total_area
            
