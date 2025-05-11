class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        result = set()
        i = 1

        while i <= bound:
            j = 1
            while i + j <= bound:
                result.add(i + j)
                if y == 1: break
                j *= y
            if x == 1: break
            i *= x
        
        return list(result)