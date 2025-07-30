import heapq

class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        # Convert all to integers for correct numeric comparison
        min_heap = []
        
        for cnum in nums:
            heapq.heappush(min_heap, int(cnum))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # Return as string (as required by the problem)
        return str(min_heap[0])