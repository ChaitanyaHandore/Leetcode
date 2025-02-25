class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        # Split the path by the '/' delimiter and process each part
        components = path.split('/')
        
        # Initialize a stack to store the final path components
        stack = []
        
        for component in components:
            if component == '' or component == '.':
                # Skip empty or current directory components
                continue
            elif component == '..':
                # Go up one level by popping from the stack
                if stack:
                    stack.pop()
            else:
                # Add the directory to the stack
                stack.append(component)
        
        # Reconstruct the simplified path
        return '/' + '/'.join(stack)

# Example usage:
sol = Solution()
path = "/home//foo/"
print(sol.simplifyPath(path))  # Output: "/home/foo"