class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        pass_data = []
        for n in nums:
            if n not in pass_data:
                pass_data.append(n)
            else:
                return True
        
        return False