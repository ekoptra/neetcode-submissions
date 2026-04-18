# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2

        new_head = None
        while head1 and head2:
            if head1.val <= head2.val:
                head1, head2 = head2, head1

            if new_head is None:
                new_head = head2
                
            while head2.next and head2.next.val <= head1.val:
                head2 = head2.next
            
            next_head2 = head2.next
            head2.next = head1
            head2 = next_head2
        
        if new_head is None:
            if head1 is not None:
                new_head = head1
            elif head2 is not None:
                new_head = head2

        return new_head 
                