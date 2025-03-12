class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        cJewelsSet = set(jewels)
        return sum(cStone in cJewelsSet for cStone in stones)

# Example usage:
solution = Solution()
print(solution.numJewelsInStones("aA", "aAAbbbb"))  # Output: 3
print(solution.numJewelsInStones("z", "ZZ"))        # Output: 0