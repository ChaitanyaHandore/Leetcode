from collections import Counter

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        c1, c2 = Counter(s1), Counter(s2[:len(s1)])  # Initial frequency count
        
        if c1 == c2:
            return True
        
        for i in range(len(s1), len(s2)):
            c2[s2[i]] += 1  # Add new character to window
            c2[s2[i - len(s1)]] -= 1  # Remove old character from window
            
            if c2[s2[i - len(s1)]] == 0:
                del c2[s2[i - len(s1)]]  # Remove zero-count characters
            
            if c1 == c2:
                return True
        
        return False

# Test cases
sol = Solution()
print(sol.checkInclusion("ab", "eidbaooo"))  # Output: True
print(sol.checkInclusion("ab", "eidboaoo"))  # Output: False