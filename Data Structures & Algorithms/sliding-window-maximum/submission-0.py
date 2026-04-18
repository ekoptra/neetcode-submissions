class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []

        r = 0
        while True:            
            heap.append(r)
            i = len(heap) - 1

            while i > 0:
                heap_parent_idx = (i-1) // 2

                if nums[heap[heap_parent_idx]] >= nums[heap[i]]:
                    break

                heap[heap_parent_idx], heap[i] = heap[i], heap[heap_parent_idx]
                i = heap_parent_idx
            
            if r + 1 >= k: break
            
            r += 1
            
        res = []
        l = 0

        while r < len(nums):
            if heap[0] >= l:
                res.append(nums[heap[0]])
            else:
                heap[0] = heap.pop()
                i = 0
                
                while i < len(heap):
                    heap_right_idx = (i*2) + 1
                    heap_left_idx = (i*2) + 2

                    if heap_left_idx >= len(heap):
                        break
                    elif heap_right_idx >= len(heap):
                        max_child_idx = heap_left_idx
                    elif nums[heap[heap_right_idx]] < nums[heap[heap_left_idx]]:
                        max_child_idx = heap_left_idx
                    else:
                        max_child_idx = heap_right_idx
                    
                    if nums[heap[max_child_idx]] < nums[heap[i]]:
                        break
                    
                    heap[max_child_idx], heap[i] = heap[i], heap[max_child_idx]
                    i = max_child_idx

                continue
            
            r += 1
            if r >= len(nums):
                break

            heap.append(r)
            i = len(heap) - 1   
             
            while i > 0:
                heap_parent_idx = (i-1) // 2

                if nums[heap[heap_parent_idx]] >= nums[heap[i]]:
                    break

                heap[heap_parent_idx], heap[i] = heap[i], heap[heap_parent_idx] 
                i = heap_parent_idx
            

            l += 1

        return res

