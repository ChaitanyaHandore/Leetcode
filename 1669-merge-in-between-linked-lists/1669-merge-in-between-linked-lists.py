# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """

        # Step 1: Find node at position a-1
        cprev = list1
        for _ in range(a - 1):
            cprev = cprev.next

        # Step 2: Find node at position b
        cafter = cprev
        for _ in range(b - a + 2):  # +2 because we want node after b
            cafter = cafter.next

        # Step 3: Connect cprev to list2 head
        cprev.next = list2

        # Step 4: Traverse to end of list2
        clast = list2
        while clast.next:
            clast = clast.next

        # Step 5: Connect end of list2 to node after b
        clast.next = cafter

        return list1