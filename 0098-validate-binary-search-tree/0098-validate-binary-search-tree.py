class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def helper(node, low, high):
            # Base case: if node is None, it's a valid BST by definition
            if not node:
                return True
            
            # Check the current node's value falls within the valid range
            if node.val <= low or node.val >= high:
                return False
            
            # Recursively check the left and right subtree with updated bounds
            return helper(node.left, low, node.val) and helper(node.right, node.val, high)
        
        # Initial call to the helper function with the entire range of valid values
        return helper(root, float('-inf'), float('inf'))