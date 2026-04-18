# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoList(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        dummy = head = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next

            head = head.next
        
        head.next = list1 or list2
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        while len(lists) > 1:
            merged_list = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                merged_list.append(self.mergeTwoList(l1, l2))
            
            lists = merged_list 

        return lists[0]

