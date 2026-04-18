class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if len(self.max_heap) == len(self.min_heap):
            if len(self.min_heap) > 0 and num > self.min_heap[0]:
                heapq.heappush(self.min_heap, num)
                val = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, val * -1)
            else:
                heapq.heappush(self.max_heap, num * -1)
        else:
            if num < (self.max_heap[0] * -1):
                heapq.heappush(self.max_heap, num * -1)
                val = heapq.heappop(self.max_heap) * -1
                heapq.heappush(self.min_heap, val)
            else:
                heapq.heappush(self.min_heap, num)

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return self.max_heap[0] * -1
        
        left_val = self.max_heap[0] * -1
        right_val = self.min_heap[0]
        return (left_val + right_val) / 2
        