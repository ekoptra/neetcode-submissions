class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(s, num_open, num_close):
            if len(s) == 2 * n:
                res.append(s)
                return
            
            if num_open < n:
                backtrack(s + "(", num_open + 1, num_close)
            
            if num_close < num_open:
                backtrack(s + ")", num_open, num_close + 1)

        backtrack("", 0, 0)
        return res