class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        # Find the current maximum candies
        c_max = max(candies)
        
        # Determine if each child can have the maximum candies
        maxCandies = max(candies)
        result = []

        for candy in candies:
            result.append(candy + extraCandies >= maxCandies)

        return result