class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        used_board_index = set()
        def check_position(char_index, row, col):
            if char_index >= len(word):
                return True
            
            if word[char_index] != board[row][col]:
                return False
            
            used_board_index.add((row, col))

            if len(used_board_index) == len(word):
                return True

            if (row - 1 >= 0) and ((row -1, col) not in used_board_index):
                check_result = check_position(char_index + 1, row - 1, col)
                if check_result:
                    return True
            
            if (col - 1 >= 0) and ((row, col - 1) not in used_board_index):
                check_result = check_position(char_index + 1, row, col - 1)
                if check_result:
                    return True
            
            if (row + 1 < len(board)) and ((row + 1, col) not in used_board_index):
                check_result = check_position(char_index + 1, row + 1, col)
                if check_result:
                    return True

            if (col + 1 < len(board[0])) and ((row, col + 1) not in used_board_index):
                check_result = check_position(char_index + 1, row, col + 1)
                if check_result:
                    return True

            used_board_index.remove((row, col))
            return False
        
        i = 0
        while i < len(board):
            j = 0
            while j < len(board[i]):
                check_result = check_position(0, i, j)
                if check_result:
                    return True
                j += 1
            i += 1
        
        return False


