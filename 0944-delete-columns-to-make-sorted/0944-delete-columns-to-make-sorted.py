class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        cdelete_count = 0
        for ccol in zip(*strs):  # Transposing the list of strings to iterate column-wise
            if list(ccol) != sorted(ccol):  
                cdelete_count += 1
        return cdelete_count

# Test Cases
solution = Solution()
print(solution.minDeletionSize(["cba","daf","ghi"]))  # Output: 1
print(solution.minDeletionSize(["a","b"]))           # Output: 0
print(solution.minDeletionSize(["zyx","wvu","tsr"])) # Output: 3