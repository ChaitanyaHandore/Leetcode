class Solution(object):
    def wordBreak(self, cs, cwordDict):
        """
        :type cs: str
        :type cwordDict: List[str]
        :rtype: bool
        """
        cwordSet = set(cwordDict)  # Convert list to set for O(1) lookup
        clen = len(cs)
        cdp = [False] * (clen + 1)
        cdp[0] = True  # Base case: Empty string can always be segmented
        
        for ci in range(1, clen + 1):
            for cj in range(ci):
                if cdp[cj] and cs[cj:ci] in cwordSet:
                    cdp[ci] = True
                    break  # No need to check further
            
        return cdp[clen]

# Example usage:
sol = Solution()
print(sol.wordBreak("leetcode", ["leet", "code"]))  # Output: True
print(sol.wordBreak("applepenapple", ["apple", "pen"]))  # Output: True
print(sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # Output: False