class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = 0
        s = []

        for o in operations:
            if o == 'C':
                pop_val = s.pop()
                score -= pop_val
                continue

            new_score = 0
            if o == '+':
                new_score = s[-2] + s[-1]
            elif o == 'D':
                new_score = s[-1] * 2
            else:
                new_score = int(o)
            
            score += new_score
            s.append(new_score)
        
        return score