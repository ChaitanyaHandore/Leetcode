class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        cwhite_count = blocks[:k].count('W')  # Initial count of 'W' in first window
        cmin_operations = cwhite_count
        
        for ci in range(k, len(blocks)):
            if blocks[ci - k] == 'W':  # Remove leftmost element
                cwhite_count -= 1
            if blocks[ci] == 'W':  # Add new rightmost element
                cwhite_count += 1
            cmin_operations = min(cmin_operations, cwhite_count)  # Track min operations
        
        return cmin_operations

# Test cases
sol = Solution()
print(sol.minimumRecolors("WBBWWBBWBW", 7))  # Output: 3
print(sol.minimumRecolors("WBWBBBW", 2))     # Output: 0