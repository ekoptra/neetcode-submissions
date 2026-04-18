class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        i = 0
        while i < len(nums):
            print(nums[i])
            if nums[i] < 0:
                i += 1
                continue

            index_val = nums[i] - 1
            if index_val != i:
                if nums[index_val] < 0:
                    return nums[i]
                else:
                    nums[i], nums[index_val] = nums[index_val], nums[i]
                    nums[index_val] = -1
            else:
                nums[i] = -1
                i += 1 