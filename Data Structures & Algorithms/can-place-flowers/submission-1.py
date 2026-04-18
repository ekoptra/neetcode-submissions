class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        number_can_place = 0

        i = 0
        while i < len(flowerbed) and (number_can_place < n):
            if flowerbed[i] == 1:
                i += 2
            else:                
                if (i + 1 < len(flowerbed)) and (flowerbed[i+1] == 0):
                    number_can_place += 1
                    i += 2
                else:
                    if i + 1 == len(flowerbed):
                        number_can_place += 1
                        
                    i += 1
        
        print(number_can_place)
        return number_can_place >= n
        