# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        
        from collections import deque
        queue = deque([(root, 1)])  # Store the node and its depth
        
        while queue:
            c_node, c_depth = queue.popleft()
            
            # Check if it's a leaf node
            if not c_node.left and not c_node.right:
                return c_depth
            
            # Add the left child to the queue
            if c_node.left:
                queue.append((c_node.left, c_depth + 1))
            
            # Add the right child to the queue
            if c_node.right:
                queue.append((c_node.right, c_depth + 1))