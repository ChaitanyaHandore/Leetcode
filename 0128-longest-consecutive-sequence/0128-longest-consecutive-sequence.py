class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        s = sorted(set(nums))
        c = 1
        max_len = 1

        for i in range(len(s)-1):
            if s[i+1] == s[i] + 1:
                c += 1
                max_len = max(max_len, c)
            else:
                c = 1

        return max_len