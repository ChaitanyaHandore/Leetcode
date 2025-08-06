# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        current = head
        h = []
        while current:
            h.append(current.val)
            current = current.next
        result = int("".join(map(str, h)), 2)
        return result