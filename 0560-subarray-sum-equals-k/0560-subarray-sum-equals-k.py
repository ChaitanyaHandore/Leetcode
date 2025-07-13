class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict

        cprefix_count = defaultdict(int)
        cprefix_count[0] = 1  # For subarrays that start at index 0
        ccount = 0
        crunning_sum = 0

        for cnum in nums:
            crunning_sum += cnum

            if (crunning_sum - k) in cprefix_count:
                ccount += cprefix_count[crunning_sum - k]

            cprefix_count[crunning_sum] += 1

        return ccount