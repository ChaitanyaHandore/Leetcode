class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        c = Counter(s)
        a = []
        b = []
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for i, j in c.items():
            if i in vowels:
                a.append(j)
            else:
                b.append(j)
        
        max_vowel = max(a) if a else 0
        max_consonant = max(b) if b else 0

        return max_vowel + max_consonant