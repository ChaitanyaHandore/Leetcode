import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cmin_heap = []
        for cnum in nums:
            heapq.heappush(cmin_heap, cnum)
            if len(cmin_heap) > k:
                heapq.heappop(cmin_heap)
        return cmin_heap[0]