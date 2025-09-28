from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()   # stores indices
        res = []

        for i in range(len(nums)):
            # remove smaller elements
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # remove indices outside window
            if dq[0] == i - k:
                dq.popleft()

            # record result after first k-1 steps
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res