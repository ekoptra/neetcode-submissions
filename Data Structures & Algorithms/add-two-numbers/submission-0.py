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

            if adder >= 10:
                head2.val = adder - 10
                adder = 1
            else:
                head2.val = adder
                adder = 0

            prev = head2
            head1 = head1.next
            head2 = head2.next
        
        if head1:
            prev.next = head1
            while head1:
                adder += head1.val
                if adder >= 10:
                    head1.val = adder - 10
                    adder = 1
                else:
                    head1.val = adder
                    adder = 0
                
                prev = head1
                head1 = head1.next
        
        if head2:
            while head2:
                adder += head2.val
                if adder >= 10:
                    head2.val = adder - 10
                    adder = 1
                else:
                    head2.val = adder
                    adder = 0
                
                prev = head2
                head2 = head2.next

        if adder > 0:
            prev.next = ListNode(1)

        return l2