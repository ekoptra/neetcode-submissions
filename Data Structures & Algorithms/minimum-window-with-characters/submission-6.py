class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        t_count = {}
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1 

        l = r = 0
        target_satisfied = len(t_count.keys())
        res = ""
        current_satisfied = 0
        s_count = {}

        while l < len(s) and (s[l] not in t_count):
            l += 1
        
        if l >= len(s):
            return ""
        
        r = l + 1
        
        s_count[s[l]] = s_count.get(s[l], 0) + 1
        if s_count[s[l]] == t_count[s[l]]:
            current_satisfied += 1
            if current_satisfied == target_satisfied: 
                if (res == "") or (r - l + 1 < len(res)):
                    res = s[l:r]
    
        while (r < len(s)) and (l < len(s)):
            while current_satisfied != target_satisfied:
                if s[r] in t_count:
                    s_count_before = s_count.get(s[r], 0)
                    s_count[s[r]] = s_count_before + 1

                    if (s_count_before < t_count[s[r]]) and (s_count[s[r]] == t_count[s[r]]):
                        current_satisfied += 1

                        if current_satisfied == target_satisfied:
                            break

                r += 1
                if r >= len(s): 
                    return res
            

            if (res == "") or (r - l + 1 < len(res)):
                res = s[l:(r+1)]

            s_count[s[l]] -= 1
            l += 1
            if s_count[s[l-1]] < t_count[s[l-1]]: 
                current_satisfied -= 1
            
            while (l < len(s)) and (s[l] not in t_count):
                l += 1
            
            if current_satisfied != target_satisfied:
                r += 1
            
        return res

        