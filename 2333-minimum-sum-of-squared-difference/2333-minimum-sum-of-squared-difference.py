class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k1: int
        :type k2: int
        :rtype: int
        """
        from heapq import heapify, heappush, heappop
        heap = [ -abs(x-y) for x, y in zip(nums1, nums2)]
        s = -sum(heap)
        if k1+k2 >= s: return 0
        delta = k1 + k2
        heapify(heap)
        n = len(nums1)
        while delta > 0:
            d = -heappop(heap)
            gap = max(delta//n, 1) if heap else delta
            d -= gap
            heappush(heap, -d)
            delta -= gap
        return sum(pow(e,2) for e in heap)