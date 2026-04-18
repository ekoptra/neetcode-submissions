class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        heap = []

        for i in range(len(position)):
            heap.append(i)
            
            j = len(heap) - 1
            while j > 0:
                parent = (j-1) // 2
                if position[heap[parent]] < position[heap[j]]:
                    heap[parent], heap[j] = heap[j], heap[parent]
                j = parent
            
        stack = []
        while len(heap) > 0:
            highest_idx = heap[0]
            last_idx = heap.pop()

            if len(heap) > 0:
                heap[0] = last_idx

                j = 0
                while True:
                    left = (j * 2) + 1
                    right = (j * 2) + 2
                    max_idx = None
                    if left >= len(heap):
                        break
                    elif right >= len(heap):
                        max_idx = left
                    elif position[heap[left]] > position[heap[right]]:
                        max_idx = left
                    else:
                        max_idx = right
                    
                    if position[heap[max_idx]] <= position[heap[j]]:
                        break
                    
                    heap[max_idx], heap[j] = heap[j], heap[max_idx]
                    j = max_idx

            
            if len(stack) == 0:
                stack.append(highest_idx)
            else:
                top_idx_in_stack = stack[-1]
                speed_difference = speed[highest_idx] - speed[top_idx_in_stack]
                if speed_difference <= 0:
                    stack.append(highest_idx)
                else:
                    position_difference = position[top_idx_in_stack] - position[highest_idx]
                    time_to_catch_up = position_difference / speed_difference

                    catch_up_at_position = position[highest_idx] + (time_to_catch_up * speed[highest_idx])
                    if (catch_up_at_position > target):
                        stack.append(highest_idx)
                
        return len(stack)                   




        
        
            