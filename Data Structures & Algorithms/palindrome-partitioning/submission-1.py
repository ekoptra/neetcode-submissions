class Solution:
    def __init__(self):
        self.polindrom_check = {}

    def is_polindrom(self, s: str) -> bool:
        if s in self.polindrom_check:
            return self.polindrom_check.get(s)

        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                self.polindrom_check[s] = False
                return False
            i += 1
            j -= 1

        self.polindrom_check[s] = True
        return True
    
    def solve(self, s: str, i: int, j: int, is_first: bool) -> List[List[str]]:
        if i == j:
            return [[s[i]]]
        
        res = self.solve(s, i, j - 1, False)
        last_word = s[j]

        new_res = []
        for subs in res:
            last_sub = subs[-1]
            # Pola dipisah
            if self.is_polindrom(last_sub):
                new_sub = subs.copy()
                new_sub.append(last_word)
                new_res.append(new_sub)
            
            # Pola digabung            
            last_sub += last_word
            if (not is_first) or self.is_polindrom(last_sub):
                subs[-1] = last_sub
                new_res.append(subs.copy())
        
        return new_res

    def partition(self, s: str) -> List[List[str]]:
        return self.solve(s, 0, len(s) -1, True)




