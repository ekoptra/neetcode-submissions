# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = slow
        slow = slow.next
        prev.next = None
        while slow:
            slow_next = slow.next
            slow.next = prev
            prev = slow
            slow = slow_next
        
        left, right = head, prev
        is_left = True
        while left != right:
            if is_left:
                next_left = left.next
                left.next = right
                left = next_left
            else:
                next_right = right.next
                right.next = left
                right = next_right
                
            is_left = not is_left


