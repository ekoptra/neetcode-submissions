class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        num_rows, num_cols = len(board), len(board[0])
        visited = set()

        def dfs(row, col, i):
            if i == len(word):
                return True
            
            if (row < 0 or col < 0 or
                row >= num_rows or col >= num_cols or
                word[i] != board[row][col] or
                (row, col) in visited):
                return False
            
            visited.add((row, col))
            res = (dfs(row - 1, col, i + 1) or
                   dfs(row + 1, col, i + 1) or
                   dfs(row, col - 1, i + 1) or
                   dfs(row, col + 1, i + 1))
            visited.remove((row, col))
            return res
        
        for i in range(num_rows):
            for j in range(num_cols):
                if dfs(i, j, 0):
                    return True

        return False 


