# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        adder = 0
        head1, head2 = l1, l2

        prev = None
        while head1 and head2:
            adder += head1.val + head2.val
            
            head2.val = adder - 10 if adder >= 10 else adder
            adder = 1 if adder >= 10 else 0

            prev = head2
            head1 = head1.next
            head2 = head2.next
        
        if head1:
            prev.next = head1
            head2 = head1
        
        while head2:
            adder += head2.val

            head2.val = adder - 10 if adder >= 10 else adder
            adder = 1 if adder >= 10 else 0
            
            prev = head2
            head2 = head2.next

        if adder > 0:
            prev.next = ListNode(1)

        return l2