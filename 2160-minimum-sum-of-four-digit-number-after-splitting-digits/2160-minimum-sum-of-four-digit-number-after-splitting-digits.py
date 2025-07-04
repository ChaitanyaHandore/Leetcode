from itertools import permutations

class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        cdigits = list(str(num))
        cmin_sum = float('inf')

        for cperm in permutations(cdigits):
            for csplit in range(1, len(cperm)):
                cnew1 = int(''.join(cperm[:csplit]))
                cnew2 = int(''.join(cperm[csplit:]))
                cmin_sum = min(cmin_sum, cnew1 + cnew2)

        return cmin_sum