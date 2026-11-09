class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, index: int) -> int:
        node = self.head.next
        while node and index > 0:
            node = node.next
            index -= 1
        if node and node != self.tail and index == 0:
            return node.val
        return -1
        

    def addAtHead(self, val: int) -> None:
        node, nxt, prev = ListNode(val), self.head.next, self.head
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev

    def addAtTail(self, val: int) -> None:
        node, nxt, prev = ListNode(val), self.tail, self.tail.prev
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and index == 0:
            node, nxt, prev = ListNode(val), curr, curr.prev
            prev.next = node
            nxt.prev = node
            node.next = nxt
            node.prev = prev

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and curr != self.tail and index == 0:
            nxt, prev = curr.next, curr.prev
            nxt.prev = prev
            prev.next = nxt


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)