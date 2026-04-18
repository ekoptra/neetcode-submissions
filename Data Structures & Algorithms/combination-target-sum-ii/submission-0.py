class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        subset = []
        def dfs(i, total):
            if target == total:
                result.append(subset.copy())
                return

            if i >= len(candidates) or total > target:
                return
            
            
            subset.append(candidates[i])
            dfs(i + 1, total + candidates[i])
            
            subset.pop()
            while i + 1 < len(candidates):
                if candidates[i] != candidates[i+1]:
                    dfs(i+1, total)
                    return
                i += 1
        
        dfs(0, 0)
        return result