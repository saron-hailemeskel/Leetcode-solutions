class Solution:
    def getIntersectionNode(self, headA, headB):
        a = headA
        b = headB

        while a != b:
            if a is None:
                a = headB
            else:
                a = a.next

            if b is None:
                b = headA
            else:
                b = b.next

        return a