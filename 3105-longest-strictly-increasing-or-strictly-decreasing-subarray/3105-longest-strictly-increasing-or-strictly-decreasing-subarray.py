class Solution(object):
    def longestMonotonicSubarray(self, c_nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not c_nums:
            return 0
    
        c_inc = c_dec = c_max_len = 1
        
        for c_i in range(1, len(c_nums)):
            if c_nums[c_i] > c_nums[c_i - 1]:  # Strictly increasing
                c_inc += 1
                c_dec = 1
            elif c_nums[c_i] < c_nums[c_i - 1]:  # Strictly decreasing
                c_dec += 1
                c_inc = 1
            else:  # Reset if equal
                c_inc = c_dec = 1

            c_max_len = max(c_max_len, c_inc, c_dec)
        
        return c_max_len

