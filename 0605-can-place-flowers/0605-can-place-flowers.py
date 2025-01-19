class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        length = len(flowerbed)
        
        for i in range(length):
            if flowerbed[i] == 0:
                # Check previous and next plots
                prev = flowerbed[i - 1] if i > 0 else 0
                next = flowerbed[i + 1] if i < length - 1 else 0
                
                if prev == 0 and next == 0:  # Can plant here
                    flowerbed[i] = 1
                    count += 1
                
            if count >= n:  # No need to continue if we've already planted enough
                return True
        
        return count >= n