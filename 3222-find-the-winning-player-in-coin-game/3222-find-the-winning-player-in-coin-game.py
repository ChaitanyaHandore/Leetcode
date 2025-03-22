class Solution(object):
    def winningPlayer(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: str
        """
        
        turn = 0
        while True:
            if x >= 1 and y >= 4:
                x -= 1
                y -= 4
            else:
                return "Bob" if turn % 2 == 0 else "Alice"
            turn += 1
        