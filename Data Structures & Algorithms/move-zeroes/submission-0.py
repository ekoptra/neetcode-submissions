class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i_zero = 0
        i = 0
        while True:
            while i_zero < len(nums):
                if nums[i_zero] == 0:
                    break
                i_zero += 1
            
            if i_zero > i:
                i = i_zero + 1
            
            while i < len(nums):
                if nums[i] != 0:
                    break
                i += 1
            
            if (i == len(nums)) or (i_zero == len(nums)):
                break
            
            nums[i], nums[i_zero] = nums[i_zero], nums[i]
            i += 1
            i_zero += 1
