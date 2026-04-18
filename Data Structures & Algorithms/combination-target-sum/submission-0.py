class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        subset = []
        def dfs(i, t):
            if i >= len(nums) or t < 0:
                return
            
            if t == 0:
                result.append(subset.copy())
                return
           
            subset.append(nums[i])
            dfs(i, t - nums[i])

            subset.pop()
            dfs(i + 1, t)
        
        dfs(0, target)
        return result
            


            
