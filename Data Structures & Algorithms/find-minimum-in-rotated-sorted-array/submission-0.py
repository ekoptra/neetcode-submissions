class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        min_n = 1000
        while left <= right:
            center = math.ceil((right + left)/2)
            min_n = min(min_n, nums[center])

            if nums[left] < nums[center]:
                min_n = min(min_n, nums[left])
                left = center + 1
            else:
                right = center - 1

        return min_n
            
        