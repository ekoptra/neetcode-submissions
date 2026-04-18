class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)

        start_nums = []
        for n in nums:
            if (n-1) not in set_nums:
                start_nums.append(n)

        max_val = 0
        for n in start_nums:
            i = 1

            while (n+1) in set_nums:
                i += 1
                n += 1
            
            if max_val < i:
                max_val = i
        
        return max_val