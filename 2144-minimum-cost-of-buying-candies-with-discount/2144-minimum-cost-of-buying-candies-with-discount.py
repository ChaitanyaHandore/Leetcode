class Solution(object):
    def minimumCost(self, A):
        """
        :type cost: List[int]
        :rtype: int
        """
        return sum(a for i,a in enumerate(sorted(A)) if (len(A) - i) % 3)