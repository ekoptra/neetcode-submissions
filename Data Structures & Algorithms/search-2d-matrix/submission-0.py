class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        m = len(matrix)
        n = len(matrix[-1])
        right = (m * n) - 1

        while left <= right:
            center = math.ceil((left + right) / 2)

            row = math.ceil((center + 1) / n) - 1
            col = center - (row * n)

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = center + 1
            else:
                right = center - 1

        return False