# Add two numbers | leetcode 02 | https://leetcode.com/problems/add-two-numbers/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class AddTwoNumbers(object):
    def solution_one(self, l1: list[ListNode], l2: list[ListNode]) -> list[ListNode]:
        res = ListNode()
        head = res

        while l1 != None or l2 != None:
            if l1 == None:
                this_val = res.val + l2.val
                l2 = l2.next
            elif l2 == None:
                this_val = res.val + l1.val
                l1 = l1.next
            else:
                this_val = res.val + l1.val + l2.val
                l1, l2 = l1.next, l2.next

            this_digit = this_val % 10
            next_digit = this_val // 10

            res.val = this_digit
            if l1 != None or l2 != None:
                res.next = ListNode(next_digit)
                res = res.next

            if next_digit > 0:
                res.next = ListNode(next_digit)
                res = res.next

        return head

        # def addTwoNumbers(self, l1, l2):
        #     """
        #     :type l1: ListNode
        #     :type l2: ListNode
        #     :rtype: ListNode
        #     """
        #     last = 0
        #     head = prev = None
        #     while True:
        #         if l2 is None and l1 is None and last == 0:
        #             break
        #         val = last
        #         if l2 is not None:
        #             val += l2.val
        #             l2 = l2.next
        #         if l1 is not None:
        #             val += l1.val
        #             l1 = l1.next
        #         if val >= 10:
        #             val = val % 10
        #             last = 1
        #         else:
        #             last = 0
        #         current = ListNode(val)
        #         if prev is None:
        #             head = current
        #         else:
        #             prev.next = current
        #         prev = current
        #     return head

    def solution(self, l1, l2):
        """
        Solution
        :param l1: int
        :param l2: int
        :return:
        """
        carry = 0
        head = curr = ListNode(0)
        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            curr.next = ListNode(val % 10)
            curr = curr.next
            carry = val / 10
        if carry > 0:
            curr.next = ListNode(carry)
        return head.next
