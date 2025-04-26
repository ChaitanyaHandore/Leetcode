class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2
            
            # Calculate hours needed at speed mid
            hours = 0
            for pile in piles:
                hours += (pile + mid - 1) // mid  # ceiling division
            
            if hours <= h:
                right = mid  # Try slower speed
            else:
                left = mid + 1  # Need faster speed

        return left