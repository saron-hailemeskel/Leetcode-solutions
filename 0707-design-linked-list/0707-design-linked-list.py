class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        if index < self.size // 2:
            curr = self.head
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - 1 - index):
                curr = curr.prev
        return curr.val

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index <= 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            curr = self.head
            for _ in range(index):
                curr = curr.next
            
            new_node = ListNode(val)
            pred = curr.prev
            
            pred.next = new_node
            new_node.prev = pred
            new_node.next = curr
            curr.prev = new_node
            
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        curr = self.head
        if self.size == 1:
            self.head = None
            self.tail = None
        elif index == 0:
            self.head = self.head.next
            self.head.prev = None
        elif index == self.size - 1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            if index < self.size // 2:
                curr = self.head
                for _ in range(index):
                    curr = curr.next
            else:
                curr = self.tail
                for _ in range(self.size - 1 - index):
                    curr = curr.prev
            
            pred = curr.prev
            succ = curr.next
            pred.next = succ
            succ.prev = pred
            
        self.size -= 1