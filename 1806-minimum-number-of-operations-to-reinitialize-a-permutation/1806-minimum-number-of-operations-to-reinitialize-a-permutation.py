class Solution(object):
    def reinitializePermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        mod = n - 1
        curr_power = 2
        cnt = 1
        # Find multiplicative order modulo n-1
        while curr_power != 1:
            curr_power = (2*curr_power) % mod
            cnt += 1
        return cnt
