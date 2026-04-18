class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):

                if board[i][j] == ".":
                    continue
                
                value = int(board[i][j])
                if value in row[i]:
                    return False
                else:
                    row[i].add(value)
                
                if value in col[j]:
                    return False
                else:
                    col[j].add(value)

                box_row = i // 3
                box_col = j // 3
                box_idx = box_row * 3 + box_col

                if value in box[box_idx]:
                    return False
                else:
                    box[box_idx].add(value)
        
        return True

