class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            center = (left + right) // 2

            if nums[center] == target:
                return center
            elif nums[center] < nums[right]:
                if (nums[center] < target) and (target <= nums[right]):
                    left = center + 1
                else:
                    right = center - 1
            else:
                if (nums[left] <= target) and (target < nums[center]):
                    right = center - 1
                else:
                    left = center + 1

        return -1