class Solution(object):
    def minAbsoluteSumDiff(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums1)
        sorted_nums1 = sorted(nums1)
        total = 0
        max_reduction = 0
        
        for i in range(n):
            a, b = nums1[i], nums2[i]
            curr_diff = abs(a - b)
            total += curr_diff
            
            idx = bisect.bisect_left(sorted_nums1, b)
            if idx < n:
                max_reduction = max(max_reduction, curr_diff - abs(sorted_nums1[idx] - b))
            if idx > 0:
                max_reduction = max(max_reduction, curr_diff - abs(sorted_nums1[idx - 1] - b))
        
        return (total - max_reduction) % MOD