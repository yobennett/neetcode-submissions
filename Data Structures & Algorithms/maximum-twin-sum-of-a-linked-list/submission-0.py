# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        maxSum = 0

        slow, fast = head, head
        prev = None

        # iterate until fast reaches end, slow at middle
        while fast and fast.next:

            # iterate fast
            fast = fast.next.next

            # iterate slow, reverse first half
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        result = 0
        while slow:
            result = max(result, prev.val + slow.val)
            # iterate prev (reverse first half)
            prev = prev.next
            # continue to iterate slow
            slow = slow.next

        return result
