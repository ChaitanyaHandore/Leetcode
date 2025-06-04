class Solution(object):
    def smallestRepunitDivByK(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k % 2 == 0 or k % 5 == 0:
            return -1  # Repunit can't be divisible by even numbers or multiples of 5

        cremainder = 0
        for ci in range(1, k + 1):  # max length needed is at most k
            cremainder = (cremainder * 10 + 1) % k
            if cremainder == 0:
                return ci  # Found the smallest repunit divisible by k

        return -1  # If not found within k iterations