class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in tokens:
            if i in ['+', '-', '*', '/']:
                operand2 = stack.pop()
                operand1 = stack.pop()
                if i == '+':
                    result = operand1 + operand2
                elif i == '-':
                    result = operand1 - operand2
                elif i == '*':
                    result = operand1 * operand2
                elif i == '/':
                    # Truncate toward zero
                    result = int(float(operand1) / operand2)
                stack.append(result)
            else:
                stack.append(int(i))
        return stack[0]