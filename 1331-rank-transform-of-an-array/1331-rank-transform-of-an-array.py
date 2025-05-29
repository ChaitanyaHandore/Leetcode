class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # Step 1: Get sorted unique values
        c_sorted_unique = sorted(set(arr))
        
        # Step 2: Map each value to its rank
        c_rank = {c_value: c_rank + 1 for c_rank, c_value in enumerate(c_sorted_unique)}
        
        # Step 3: Replace each value in arr with its rank
        return [c_rank[c_value] for c_value in arr]