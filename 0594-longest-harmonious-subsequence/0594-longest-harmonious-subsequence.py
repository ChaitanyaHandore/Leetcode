from collections import Counter

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ccounter = Counter(nums)
        cmax_length = 0
        
        for cnum in ccounter:
            if cnum + 1 in ccounter:
                cmax_length = max(cmax_length, ccounter[cnum] + ccounter[cnum + 1])
        
        return cmax_length

# Example test cases
csolution = Solution()
print(csolution.findLHS([1, 3, 2, 2, 5, 2, 3, 7]))  # Output: 5
print(csolution.findLHS([1, 2, 3, 4]))              # Output: 2
print(csolution.findLHS([1, 1, 1, 1]))              # Output: 0