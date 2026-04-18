class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_hash_map = {}
        
        for word in strs:
            freq_array = [0] * 26
            for char in word:
                freq_array[ord(char) - ord('a')] += 1
            
            hashable_freq_array = tuple(freq_array)

            group_hash_map[hashable_freq_array] = group_hash_map.get(hashable_freq_array, []) + [word]

        return [group_hash_map[key] for key in group_hash_map] 