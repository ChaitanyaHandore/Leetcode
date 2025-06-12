class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        seen = defaultdict(int)
        counter = 0
        for num in nums:
            tmp, tmp2 = num - k, num + k
            if tmp in seen:
                counter += seen[tmp]
            if tmp2 in seen:
                counter += seen[tmp2]
            
            seen[num] += 1
        
        return counter
