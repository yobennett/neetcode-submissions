# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val


class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        h = []
        result = ListNode(0)
        curr = result

        for l in lists:
            if l:
                heapq.heappush(h, NodeWrapper(l))

        while h:
            w = heapq.heappop(h)
            curr.next = w.node
            curr = curr.next

            if w.node.next:
                heapq.heappush(h, NodeWrapper(w.node.next))

        return result.next