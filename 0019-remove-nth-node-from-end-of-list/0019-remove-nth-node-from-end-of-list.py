class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head

        left = dummy
        right = dummy

        # Create a gap of n nodes
        for _ in range(n):
            right = right.next

        # Move both pointers
        while right.next:
            left = left.next
            right = right.next

        # Delete the node
        left.next = left.next.next

        return dummy.next