class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in ['+', '-', '*', '/']:
                stack.append(int(t))
            else:
                val1 = stack.pop()
                val2 = stack.pop()

                if t == '+':
                    res = val1 + val2
                elif t == '*':
                    res = val1 * val2
                elif t == "/":
                    res = int(val2 / val1)
                elif t == "-":
                    res = val2 - val1
                
                stack.append(res)

        return stack[0]