class Solution:
    def __init__(self):
        self.result = []

    def generate_subsets(self, nums_remains: List[int], curr: List[int]):
        self.result.append(curr)
        nums = nums_remains.copy()
        
        while len(nums) > 0:
            pop_val = nums.pop()
            self.generate_subsets(nums, curr + [pop_val])
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.generate_subsets(nums, [])
        return self.result
