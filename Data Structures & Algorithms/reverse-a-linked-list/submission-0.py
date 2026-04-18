# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev_node = None
        while head:
            next_val = head.next
            head.next = prev_node
        
            prev_node = head

            if next_val is None:
                break
                
            head = next_val
        
        return head