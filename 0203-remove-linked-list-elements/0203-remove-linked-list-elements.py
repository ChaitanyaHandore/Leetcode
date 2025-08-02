# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cdummy = ListNode(-1)
        cdummy.next = head
        cprev = cdummy
        ccurrent = head

        while ccurrent:
            if ccurrent.val == val:
                cprev.next = ccurrent.next
            else:
                cprev = ccurrent
            ccurrent = ccurrent.next

        return cdummy.next