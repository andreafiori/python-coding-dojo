"""
# https://leetcode.com/articles/intersection-two-linked-lists/

"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class IntersectionOfTwoLinkedLists:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        :type headA, headB: ListNode
        :rtype: ListNode
        """
        # two points
        if not headA or not headB:
            return None
        a, b = headA, headB
        ans = None
        while a or b:
            if not a:
                a = headB
            if not b:
                b = headA
            if a == b and not ans:
                ans = a
            a, b = a.next, b.next
        return ans
