from collections import Counter

class Solution(object):
    def countBadPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cgood_pairs = Counter()
        ctotal_pairs = len(nums) * (len(nums) - 1) // 2  # Total possible pairs
        cgood_count = 0
        
        for cindex, cnum in enumerate(nums):
            ckey = cnum - cindex  # Transform the equation: j - i == nums[j] - nums[i] => nums[i] - i == nums[j] - j
            cgood_count += cgood_pairs[ckey]  # Count good pairs with the same key
            cgood_pairs[ckey] += 1  # Update counter for future pairs
        
        return ctotal_pairs - cgood_count  # Bad pairs = Total pairs - Good pairs

# Example test cases
csolution = Solution()
print(csolution.countBadPairs([4, 1, 3, 3]))    # Output: 5
print(csolution.countBadPairs([1, 2, 3, 4, 5])) # Output: 0