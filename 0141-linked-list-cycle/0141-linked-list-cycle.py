# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        st = set()

        while head is not None:

            # if this node is already present
            # in hashmap it means there is a cycle
            if head in st:
                return True

            # if we are seeing the node for
            # the first time, insert it in hash
            st.add(head)

            head = head.next

        return False
            