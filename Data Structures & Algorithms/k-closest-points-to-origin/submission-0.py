class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = []

        for p in points:
            distance = math.sqrt(p[0] * p[0] + p[1] * p[1])
            
            if len(q) < k:
                heapq.heappush(q, (distance * -1, p[0], p[1]))
            else:
                if (q[0][0] * -1) > distance:
                     heapq.heappop(q)
                     heapq.heappush(q, (distance * -1, p[0], p[1]))
        
        return [ [p[1], p[2]] for p in q]