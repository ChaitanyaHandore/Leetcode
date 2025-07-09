class Solution(object):
    def smallestRangeII(self, A, K):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        A.sort()
        mi, ma = A[0], A[-1]
        ans = ma - mi
        for i in xrange(len(A) - 1):
            a, b = A[i], A[i+1]
            ans = min(ans, max(ma-K, a+K) - min(mi+K, b-K))
        return ans