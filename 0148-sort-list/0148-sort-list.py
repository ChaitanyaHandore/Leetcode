class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        # Step 1: Find the length of the linked list
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # Step 2: Bottom-up merge sort
        dummy = ListNode(0, head)
        size = 1  # Initial size of sublists

        while size < length:
            prev, curr = dummy, dummy.next
            while curr:
                # Split the linked list into two halves
                left = curr
                right = self.split(left, size)
                curr = self.split(right, size)

                # Merge sorted halves
                merged = self.merge(left, right)
                prev.next = merged

                # Move prev pointer to the end of merged list
                while prev.next:
                    prev = prev.next

            size *= 2  # Double the sublist size

        return dummy.next

    def split(self, head, size):
        """ Splits the linked list into two parts of given size and returns the second part. """
        if not head:
            return None
        for _ in range(size - 1):
            if not head.next:
                break
            head = head.next
        next_part, head.next = head.next, None
        return next_part

    def merge(self, left, right):
        """ Merges two sorted linked lists and returns the head of the merged list. """
        dummy = tail = ListNode()
        while left and right:
            if left.val < right.val:
                tail.next, left = left, left.next
            else:
                tail.next, right = right, right.next
            tail = tail.next
        tail.next = left if left else right
        return dummy.next

# Example Usage:
def printList(head):
    curr = head
    while curr:
        print(curr.val, )
        curr = curr.next
    print("None")

# Creating a sample linked list: 4 -> 2 -> 1 -> 3
head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
print("Original List:")
printList(head)

solution = Solution()
sorted_head = solution.sortList(head)
print("Sorted List:")
printList(sorted_head)