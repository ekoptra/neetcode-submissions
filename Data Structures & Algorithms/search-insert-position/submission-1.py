class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            center = (l + r) // 2
            if nums[center] ==  target:
                return center
            elif nums[center] < target:
                l = center + 1
            else:
                r = center - 1

        return r + 1