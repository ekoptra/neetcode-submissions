class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0
        for log in logs:
            if log[0] == "." and log[1] == ".":
                if res > 0:
                    res -= 1
            elif log[0] == ".":
                pass
            else:
                res += 1
        return res