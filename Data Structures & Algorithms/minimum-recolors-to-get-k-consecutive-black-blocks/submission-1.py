class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i = 0
        j = 0
        count_black = 0
        while j < k:
            if blocks[j] == 'B':
                count_black += 1
            j += 1
        
        res = k - count_black
        i += 1
        while j < len(blocks):
            if blocks[i-1] == 'B':
                count_black -= 1
            if blocks[j] == 'B':
                count_black += 1
            
            i += 1
            j += 1
            res = min(k - count_black, res)
        
        return res
        
