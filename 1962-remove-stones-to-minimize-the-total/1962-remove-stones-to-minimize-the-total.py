import heapq

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heappop = heapq.heappop
        heappush = heapq.heappush
        
        # Max-heap
        heap = [-num for num in piles]
        heapq.heapify(heap)

        total = sum(piles)
        
        # Algorithm
        for _ in range(k):
            curr_max = -heappop(heap)
            removed = curr_max // 2
            total -= removed
            heappush(heap, -(curr_max - removed))

        return total
        