class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        current = head
        while current:
            next_node = current.next  # Save the next node
            current.next = prev       # Reverse the link
            prev = current            # Move prev forward
            current = next_node       # Move current forward
        return prev  # prev will be the new head of the reversed list

# Create the linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Reverse the linked list
solution = Solution()
reversed_head = solution.reverseList(head)

# Print the reversed linked list
current = reversed_head
while current:
    print(current.val if current.next else "")
    current = current.next
