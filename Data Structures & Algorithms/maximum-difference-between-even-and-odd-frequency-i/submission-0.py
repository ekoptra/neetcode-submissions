class Solution:
    def maxDifference(self, s: str) -> int:
        count_dict = {}

        for char in s:
            count_dict[char] = count_dict.get(char, 0) + 1
        
        a1 = 0
        a2 = len(s)

        for key in count_dict:
            if count_dict[key] % 2 == 0:
                a2 = min(a2, count_dict[key])
            else:
                a1 = max(a1, count_dict[key])
        
        return a1 - a2