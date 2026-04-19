class Solution:
    def is_polindrom(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    
    def solve(self, s: str, is_first: bool) -> List[List[str]]:
        if len(s) == 1:
            return [[s]]
        
        res = self.solve(s[:-1], False)
        last_word = s[-1]

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
        return self.solve(s, True)




