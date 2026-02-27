"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Question: https://leetcode.com/problems/merge-two-sorted-lists/

"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MergeTwoSortedLists:
    def solution_one(self, l1, l2):
        # dummy head
        pos = dummyHead = ListNode(-1)
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                pos.next = l1
                l1 = l1.next
            else:
                pos.next = l2
                l2 = l2.next
            pos = pos.next
        # merge residual l1
        if l1 is not None:
            pos.next = l1
        # merge residual l2
        if l2 is not None:
            pos.next = l2
        return dummyHead.next


    def solution_two(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode()
        tail = answer
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2=list2.next
            tail = tail.next

        if list1:
                tail.next = list1
        elif list2:
                tail.next = list2

        return answer.next
