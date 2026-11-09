# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = head = ListNode()

        while list1 and list2:
            
            # list1 smaller than list2
            # shift list1 to point to current list1's next node
            # list1 -> list2
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next

            # list2 smaller than list1
            # shift list2 to point to current list2's next node
            # list2 -> list1
            else:
                head.next = list2
                list2 = list2.next

            head = head.next

        # any leftovers
        # can only be either list1 or list2, not both
        head.next = list1 or list2
        
        return dummy.next