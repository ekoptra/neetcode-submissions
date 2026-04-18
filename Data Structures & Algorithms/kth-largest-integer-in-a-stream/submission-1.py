class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for num in nums:
            self.add(num)        

    def insert(self, num):
        self.heap.append(num)
        i = len(self.heap) - 1
        while True:
            parent = math.floor((i - 1) / 2) 
            if (parent < 0) or (self.heap[parent] <= self.heap[i]):
                break
            
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            i = parent
        
    def remove(self):
        pop = self.heap.pop()
        if len(self.heap) == 0:
            return
        
        i = 0
        self.heap[i] = pop
        while i < len(self.heap):
            left_child_idx = (i * 2) + 1
            right_child_idx = (i * 2) + 2
            idx_to_move = None

            if left_child_idx >= len(self.heap):
                break
            elif (right_child_idx >= len(self.heap)):
                if self.heap[left_child_idx] < self.heap[i]:
                    idx_to_move = left_child_idx
                else:
                    break
            elif (self.heap[left_child_idx] < self.heap[right_child_idx]) and (self.heap[left_child_idx] < self.heap[i]):
                idx_to_move = left_child_idx
            elif self.heap[right_child_idx] < self.heap[i]:
                idx_to_move = right_child_idx
            else:
                break 
            
            self.heap[idx_to_move], self.heap[i] = self.heap[i], self.heap[idx_to_move] 
            i = idx_to_move
            
             
    def add(self, val: int) -> int:
        if (len(self.heap) < self.k):
            self.insert(val)
        else:
            if self.heap[0] < val:
                self.remove()
                self.insert(val)
        
        return self.heap[0]

