class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if left == right:
            return head
        
        # Dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Move `prev` to the node just before the `left`-th node
        for _ in range(left - 1):
            prev = prev.next
        
        # `start` will be the first node to be reversed
        start = prev.next
        then = start.next
        
        # Reverse the sublist between left and right
        for _ in range(right - left):
            start.next = then.next
            then.next = prev.next
            prev.next = then
            then = start.next
        
        return dummy.next

    def printlist(self, node):
        while node:
            print(node.val, )
            node = node.next
        print()

# Test case
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

left = 2
right = 4
solution = Solution()
result = solution.reverseBetween(head, left, right)
solution.printlist(result)