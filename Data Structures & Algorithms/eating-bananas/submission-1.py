class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1

        min_k = None
        while left <= right:
            k = math.floor((right+left+1)/2)

            is_ok = True
            curr_h = 0
            for p in piles:
                curr_h += math.ceil(p/k)

                if curr_h > h:
                    is_ok = False
                    break

            if is_ok:
                if min_k is None:
                    left = 1
                min_k = k
                right = k - 1
            else:
                left = k + 1

        return min_k
            






