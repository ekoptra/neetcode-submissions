class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):
            while len(stack) != 0:
                idx = stack.pop()

                if temperatures[idx] > temperatures[i]:
                    res[i] = idx - i
                    stack.append(idx)
                    break
            
            stack.append(i)
        
        return res