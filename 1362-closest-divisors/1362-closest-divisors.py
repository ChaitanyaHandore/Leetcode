class Solution(object):
    def closestDivisors(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        x = num
        for a in xrange(int((x + 2)**0.5), 0, -1):
            if (x + 1) % a == 0:
                return [a, (x + 1) / a]
            if (x + 2) % a == 0:
                return [a, (x + 2) / a]