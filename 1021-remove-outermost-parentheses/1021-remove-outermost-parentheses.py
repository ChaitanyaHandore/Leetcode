class Solution(object):
    def removeOuterParentheses(self, s):
        result = []
        depth = 0
        for char in s:
            if char == '(':
                if depth > 0:
                    result.append('(')
                depth += 1
            else:
                depth -= 1
                if depth > 0:
                    result.append(')')
        return ''.join(result)


        
        