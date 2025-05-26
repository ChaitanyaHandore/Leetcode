class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        c = 0
        for i in range(left, right + 1):
            ones_count = bin(i).count('1')
            if self.is_prime(ones_count):
                c += 1
        return c

    def is_prime(self, cn):
        if cn <= 1:
            return False
        for ci in range(2, int(cn ** 0.5) + 1):
            if cn % ci == 0:
                return False
        return True