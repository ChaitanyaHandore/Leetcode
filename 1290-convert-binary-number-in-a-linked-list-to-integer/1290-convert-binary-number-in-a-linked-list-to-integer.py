class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def getDecimalValue(self, head):
        c = 0
        while head:
            c = c * 2 + head.val  # Shift the current value left (multiply by 2) and add the current node's value
            head = head.next
        return c

# Example usage
head = ListNode(1)
head.next = ListNode(0)
head.next.next = ListNode(1)

solution = Solution()
print(solution.getDecimalValue(head))