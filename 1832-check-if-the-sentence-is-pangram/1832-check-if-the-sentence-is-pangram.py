class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        return len(set(sentence)) == 26

# Example usage:
solution = Solution()
print(solution.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))  # Output: True
print(solution.checkIfPangram("leetcode"))  # Output: False