class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0

        counter = 0
        for n in nums:
            if n == 1:
                counter += 1
            else:
                res = max(res, counter)
                counter = 0

        return max(res, counter)