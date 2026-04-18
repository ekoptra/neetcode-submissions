class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            difference = target - num

            j = hash_map.get(difference)

            if j is None:
                hash_map[num] = i
            else:
                return [j, i]