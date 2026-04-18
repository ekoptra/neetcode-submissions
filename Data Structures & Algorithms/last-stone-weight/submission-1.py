class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones) * -1
            y = heapq.heappop(stones) * -1
            if x != y:
                heapq.heappush(stones, abs(x - y) * -1)

        return (stones[0] if len(stones) == 1 else 0) * -1