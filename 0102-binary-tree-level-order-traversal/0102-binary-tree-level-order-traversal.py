# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        cresult = []
        if not root:
            return cresult

        cqueue = deque([root])  # initialize queue with root

        while cqueue:
            clevel = []
            for _ in range(len(cqueue)):  # process all nodes in current level
                cnode = cqueue.popleft()
                clevel.append(cnode.val)

                # add children to queue
                if cnode.left:
                    cqueue.append(cnode.left)
                if cnode.right:
                    cqueue.append(cnode.right)

            cresult.append(clevel)  # add current level to result

        return cresult
