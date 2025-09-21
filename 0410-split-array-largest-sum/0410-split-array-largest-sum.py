from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)
    
        def split(mid):
            subarray = 1
            currsum = 0
            for i in nums:
                currsum+=i
                if currsum>mid:
                    subarray+=1
                    currsum = i
            return subarray<=k

        while l<r:
            m = (l+r)//2
            if split(m):
                r = m
            else:
                l = m+1
        return l