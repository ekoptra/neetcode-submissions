class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict_str = {}

        res = -1
        left_index = 0

        for i in range(len(s)):
            if s[i] in dict_str:
                last_i = dict_str[s[i]]
                if last_i >= left_index:
                    res = max(res, i - left_index)
                    left_index = last_i + 1
                    
            dict_str[s[i]] = i
        

        return max(res, len(s) - left_index)
