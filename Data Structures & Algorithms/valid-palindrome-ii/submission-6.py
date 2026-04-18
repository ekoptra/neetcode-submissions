class Solution:
    def validPalindrome(self, s: str) -> bool:
        test = [(s, True)]

        while test:
            t, can_remove = test.pop()
            i, j = 0, len(t) - 1

            while i < j:
                if t[i] == t[j]:
                    i += 1
                    j -= 1
                else:
                    if not can_remove:
                        break
                    if t[i+1] == t[j]:
                        test.append((t[i+1:j+1], False))
                    if t[i] == t[j-1]:
                        test.append((t[i:j], False))
                    break
            else:
                return True

        return False
