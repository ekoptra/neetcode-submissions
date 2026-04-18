class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts = {}
        
        for s in s1:
            counts[s] = 1 + counts.get(s, 0)
        
        l = r = 0
        length_substring = 0

        while r < len(s2):
            count = counts.get(s2[r])

            if (count is None) or (count == 0):
                while (l < r) and (s2[l] != s2[r]):
                    counts[s2[l]] += 1
                    length_substring -= 1
                    l += 1
                
                l += 1
                r += 1
            else:
                counts[s2[r]] -= 1
                length_substring += 1
                r += 1

                if length_substring == len(s1):
                    return True

        return False

