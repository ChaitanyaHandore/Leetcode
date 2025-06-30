class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        difference = (sum(A) - sum(B)) / 2
        A = set(A)
        for candy in set(B):
            if difference + candy in A:
                return [difference + candy, candy]