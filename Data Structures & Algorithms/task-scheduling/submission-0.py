class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = {}
        for t in tasks:
            if t in c:
                c[t] += 1
            else:
                c[t] = 1
        
        h = [(c[k] * -1) for k in c] 
        heapq.heapify(h)
        q = collections.deque()
        step = 0

        while h or q:
            step += 1
            if q and q[0][1] < step:
                top_q = q.popleft()
                heapq.heappush(h, top_q[0])

            if h:
                top_h = heapq.heappop(h)
                if top_h < -1:
                    q.append((top_h + 1, step + n))            


        return step
