# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import Optional

class Solution:
    def detectCycle(self, head: Optional['ListNode']) -> Optional['ListNode']:
        if not head:
            return None
        
        slow, fast = head, head

        # Phase 1: Detect if a cycle exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            # No cycle
            return None

        # Phase 2: Find the entry point of the cycle
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow