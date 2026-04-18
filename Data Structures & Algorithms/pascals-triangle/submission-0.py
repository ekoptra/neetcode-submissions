class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        last_val = []

        while len(res) < numRows:
            if len(last_val) == 0:
                res.append([1])
                last_val = [1]
            elif len(last_val) == 1:
                res.append([1, 1])
                last_val = [1, 1]
            else:
                j = 1
                curr = [1]
                while j < len(last_val):
                    curr.append(last_val[j-1] + last_val[j])
                    j += 1
                curr.append(1)
                res.append(curr.copy())
                last_val = curr.copy()

        return res