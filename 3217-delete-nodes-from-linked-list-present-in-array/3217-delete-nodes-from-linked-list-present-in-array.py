class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums, head):
        # Create a set for efficient lookup of values in nums
        values_to_remove = set(nums)

        # Handle the case where the head node needs to be removed
        while head and head.val in values_to_remove:
            head = head.next

        # If the list is empty after removing head nodes, return None
        if not head:
            return None

        # Iterate through the list, removing nodes with values in the set
        current = head
        while current.next:
            if current.next.val in values_to_remove:
                # Skip the next node by updating the pointer
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next

        return head
    
    def printlist(self, head):
        current = head
        while current:
            print(current.val,)
            current = current.next
        print("None")


# Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

nums = [1, 2, 3]

solution = Solution()
result = solution.modifiedList(nums, head)

solution.printlist(result)  # Corrected variable name