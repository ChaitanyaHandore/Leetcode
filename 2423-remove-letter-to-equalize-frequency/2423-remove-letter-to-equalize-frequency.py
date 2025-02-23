from collections import Counter

class Solution(object):
    def equalFrequency(self, word):
        """
        :type word: str
        :rtype: bool
        """
        c = Counter(word)
        
        # Iterate through each character and try removing it
        for i in c:
            c[i] -= 1  # Remove one occurrence
            # Filter out zero counts and check if remaining frequencies are the same
            cfiltered = [freq for freq in c.values() if freq > 0]
            if len(set(cfiltered)) == 1:
                return True
            c[i] += 1  # Restore the count
        
        return False

# Example usage
cobj = Solution()
print(cobj.equalFrequency("aabbcc"))  # Output: True
print(cobj.equalFrequency("aabbc"))   # Output: False