class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        cnums = sorted(nums)
        # Three largest
        c1 = cnums[-1] * cnums[-2] * cnums[-3]
        # Two smallest (possibly negative) and the largest
        c2 = cnums[0] * cnums[1] * cnums[-1]
        return max(c1, c2)