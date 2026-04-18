# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        n_list = 1
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            n_list += 2
        
        if fast is None:
            n_list -= 1
        
        index_to_delete = n_list - n + 1
        slow_index = math.ceil((n_list + 1) / 2)
        
        curr = None
        if index_to_delete > slow_index:
            curr = slow
            index_to_delete -= slow_index
        else:
            curr = head
            index_to_delete -= 1
        
        prev = None
        while index_to_delete > 0:
            prev = curr
            curr = curr.next
            index_to_delete -= 1
        
        if curr == head:
            head = head.next
        else:
            prev.next = curr.next
        
        return head

        
