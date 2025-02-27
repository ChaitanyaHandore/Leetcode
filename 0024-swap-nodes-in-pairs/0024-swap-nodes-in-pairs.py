# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        
        # Dummy node to simplify swapping logic
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while head and head.next:
            first = head
            second = head.next
            
            # Swapping
            prev.next = second
            first.next = second.next
            second.next = first
            
            # Move pointers forward
            prev = first
            head = first.next

        return dummy.next

    def printlist(self, node):
        while node:
            print(node.val)
            node = node.next
        print()

# Creating linked list: 2 -> 1 -> 3 -> 4
head = ListNode(2)
head.next = ListNode(1)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

solution = Solution()
result = solution.swapPairs(head)
solution.printlist(result)
