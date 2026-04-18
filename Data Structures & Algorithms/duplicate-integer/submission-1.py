class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        pass_data = {}
        for n in nums:
            value = pass_data.get(n)

            if value is None:
                pass_data[n] = True
            else:
                return True
        
        return False