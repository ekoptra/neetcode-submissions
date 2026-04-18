class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        curr = [["(", 1, 0]]
        while len(curr) > 0:
            new_curr = []
            for c in curr:
                if c[1] == n and c[2] == n:
                    res.append(c[0])
                else:
                    if c[1] < n:
                        new_curr.append([c[0] + "(", c[1] + 1, c[2]])
                    
                    if c[2] < n and c[1] > c[2]:
                        new_curr.append([c[0] + ")", c[1], c[2] + 1])
            
            curr = new_curr.copy()

        return res