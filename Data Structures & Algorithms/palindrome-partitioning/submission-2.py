class Solution:
    def __init__(self):
        self.polindrom_check = {}

    def is_polindrom(self, s: str, i: int, j: int) -> bool:
        i_raw = i
        j_raw = j

        if (i, j) in self.polindrom_check:
            return self.polindrom_check.get((i, j))

        while i < j:
            if s[i] != s[j]:
                self.polindrom_check[(i_raw, j_raw)] = False
                return False
            i += 1
            j -= 1

        self.polindrom_check[(i_raw, j_raw)] = True
        return True
    

    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            
            for j in range(i, len(s)):
                if self.is_polindrom(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j + 1)
                    part.pop()
        
        dfs(0)
        return res




