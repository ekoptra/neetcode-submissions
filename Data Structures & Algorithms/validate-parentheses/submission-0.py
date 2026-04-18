class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in ('(', '{', '['):
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False

                value = stack.pop()

                if (char == ')') and (value != '('):
                    return False
                elif (char == '}') and (value != '{'):
                    return False
                elif (char == ']') and (value != '['):
                    return False
        
        return True if len(stack) == 0 else False