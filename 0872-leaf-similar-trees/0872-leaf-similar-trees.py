# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        def get_leaf_sequence(node):
            # Helper function to retrieve the leaf sequence of a tree
            if not node:
                return []
            if not node.left and not node.right:  # If it's a leaf node
                return [node.val]
            # Recursively gather leaf sequences from left and right subtrees
            return get_leaf_sequence(node.left) + get_leaf_sequence(node.right)
        
        # Get leaf sequences for both trees
        leaf_seq1 = get_leaf_sequence(root1)
        leaf_seq2 = get_leaf_sequence(root2)
        
        # Compare the two sequences
        return leaf_seq1 == leaf_seq2
        