class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map_values = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        results = []
        chars = []

        def dfs(i):
            if i >= len(digits):
                if len(chars) > 0:
                    results.append("".join(chars))
                return
            
            for char in map_values.get(digits[i]):
                chars.append(char)
                dfs(i + 1)
                chars.pop()

        dfs(0)
        return results



        