class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_right = -1
        j = len(arr) - 1

        while j >= 0:
            temp = arr[j]
            arr[j] = max_right
            max_right = max(max_right, temp)
            j -= 1
        
        return arr