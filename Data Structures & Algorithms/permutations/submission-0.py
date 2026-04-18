class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []        

        curr = []
        def dfs(remaining_set):
            if len(remaining_set) == 0:
                res.append(curr.copy())
                return

            for n in list(remaining_set):
                remaining_set.remove(n)
                curr.append(n)

                dfs(remaining_set)

                curr.pop()
                remaining_set.add(n)
        
        dfs(set(nums))

        return res