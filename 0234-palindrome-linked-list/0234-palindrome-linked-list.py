# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast= head
        slow =head
        #  first find the middle/slow
        while fast and fast.next:
            fast= fast.next.next
            slow= slow.next
        # reverse half way after the middle
        prev=None
        while slow:
            l= slow.next
            slow.next= prev
            prev=slow
            slow=l
#  checking

        left, right= head, prev
        while right:
            if left.val!=right.val:
                return False
            left= left.next
            right=right.next
        return True


        
        