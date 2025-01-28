class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Edge case: If the list is empty or has only one node, return None
        if not head or not head.next:
            return None

        # Use two pointers (slow and fast) to find the middle
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Remove the middle node
        prev.next = slow.next

        return head

    def printlist(self, node):
        """Print the linked list."""
        while node:
            print(node.val if node.next else "\n")
            node = node.next

# Create the linked list: 1 -> 3 -> 4 -> 7 -> 1 -> 2 -> 6
head = ListNode(1)
head.next = ListNode(3)
head.next.next = ListNode(4)
head.next.next.next = ListNode(7)
head.next.next.next.next = ListNode(1)
head.next.next.next.next.next = ListNode(2)
head.next.next.next.next.next.next = ListNode(6)

# Delete the middle node
solution = Solution()
result = solution.deleteMiddle(head)

# Print the resulting linked list
solution.printlist(result)
