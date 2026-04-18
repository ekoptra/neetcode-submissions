class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            center = (right + left) // 2
            if nums[center] > nums[right]: 
                left = center + 1
            else: 
                right = center

        return nums[right]
            
            
        