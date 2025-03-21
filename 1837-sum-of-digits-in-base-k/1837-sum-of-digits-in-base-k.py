class Solution:
    def sumBase(self, n, k):
        addition = 0
        while n != 0:
            addition += n % k
            n = n // k
        return addition