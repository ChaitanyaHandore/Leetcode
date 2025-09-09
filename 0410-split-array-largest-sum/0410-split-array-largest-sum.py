from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # Greedy: can we split into <= k subarrays if no subarray sum exceeds `largest`?
        def cansplit(largest: int) -> bool:
            subarray = 1
            currsum = 0
            for n in nums:
                # we know largest >= max(nums), so no single n will break it
                if currsum + n <= largest:
                    currsum += n
                else:
                    subarray += 1
                    currsum = n
                    if subarray > k:   # early exit
                        return False
            return True  # used <= k subarrays

        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            mid = (l + r) // 2
            if cansplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res