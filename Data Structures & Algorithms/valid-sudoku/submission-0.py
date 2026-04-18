class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column_check = {}
        row_check = {}
        subbox_check = {}

        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val == ".":
                    continue
                    
                key_i = i // 3
                key_j = j // 3

                key = f"{key_i}:{key_j}"

                # Check subbox
                if key in subbox_check:
                    dict_subbox_check = subbox_check[key]
                    if val in dict_subbox_check:
                        return False
                    else:
                        subbox_check[key][val] = True
                else:
                    subbox_check[key] = {val: True}

                if i in row_check:
                    dict_row_check = row_check[i]
                    if val in dict_row_check:
                        return False
                    else:
                        row_check[i][val] = True
                else:
                    row_check[i] = {val: True}
                
                if j in column_check:
                    dict_column_check = column_check[j]
                    if val in dict_column_check:
                        return False
                    else:
                        column_check[j][val] = True
                else:
                    column_check[j] = {val: True}

        return True