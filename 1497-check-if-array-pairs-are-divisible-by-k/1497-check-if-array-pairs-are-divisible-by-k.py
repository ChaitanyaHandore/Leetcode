class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        from collections import Counter
        
        # Count remainders
        c_remainders = Counter([c_num % k for c_num in arr])
        
        for c_rem in c_remainders:
            # Special case for remainder 0
            if c_rem == 0:
                if c_remainders[c_rem] % 2 != 0:
                    return False
            # Special case for k/2 when k is even
            elif k % 2 == 0 and c_rem == k // 2:
                if c_remainders[c_rem] % 2 != 0:
                    return False
            # Check if count matches its complement
            elif c_remainders[c_rem] != c_remainders[k - c_rem]:
                return False
        
        return True