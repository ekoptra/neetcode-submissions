class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_map_s = {}
        hash_map_t = {}

        for s_char in s:
            hash_map_s[s_char] = hash_map_s.get(s_char, 0) + 1
        
        for t_char in t:
            hash_map_t[t_char] = hash_map_t.get(t_char, 0) + 1

        for s_key in hash_map_s.keys():
            s_value = hash_map_s.get(s_key)
            t_value = hash_map_t.get(s_key)

            if s_value != t_value:
                return False
        
        return True
            