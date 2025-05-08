# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        cBefore = ListNode(0)
        cAfter = ListNode(0)
        cBeforeHead = cBefore
        cAfterHead = cAfter

        cCurrent = head
        while cCurrent:
            if cCurrent.val < x:
                cBefore.next = cCurrent
                cBefore = cBefore.next
            else:
                cAfter.next = cCurrent
                cAfter = cAfter.next
            cCurrent = cCurrent.next

        # Link the two partitions
        cAfter.next = None
        cBefore.next = cAfterHead.next

        return cBeforeHead.next