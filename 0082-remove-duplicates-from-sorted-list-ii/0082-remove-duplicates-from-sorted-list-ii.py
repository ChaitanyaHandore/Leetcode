# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        freq = {}
        curr = head
        while curr:
            freq[curr.val] = freq.get(curr.val, 0) + 1
            curr = curr.next

        dummy = ListNode(0)
        tail = dummy
        curr = head
        while curr:
            if freq[curr.val] == 1:
                tail.next = ListNode(curr.val)
                tail = tail.next
            curr = curr.next
        return dummy.next