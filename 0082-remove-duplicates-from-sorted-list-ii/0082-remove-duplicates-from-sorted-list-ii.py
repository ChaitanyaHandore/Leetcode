# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from collections import Counter

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Step 1: Count occurrences of each value
        c_counts = Counter()
        c_current = head
        while c_current:
            c_counts[c_current.val] += 1
            c_current = c_current.next

        # Step 2: Remove nodes with duplicate values
        c_dummy = ListNode(0)  # Dummy node to handle edge cases
        c_dummy.next = head
        c_prev, c_current = c_dummy, head

        while c_current:
            if c_counts[c_current.val] > 1:  # If duplicate, skip the node
                c_prev.next = c_current.next
            else:
                c_prev = c_current
            c_current = c_current.next

        return c_dummy.next