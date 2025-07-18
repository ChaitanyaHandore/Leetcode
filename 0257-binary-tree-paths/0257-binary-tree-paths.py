# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        if not root:
            return []
        
        c = []

        def DFS(node,path):
            if not node:
                return 
            path+=str(node.val)
            if not node.left and not node.right:
                c.append(path)
            else:
                path+="->"
                DFS(node.left,path)
                DFS(node.right,path)
        DFS(root,"")
        return c