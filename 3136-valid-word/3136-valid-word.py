class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) < 3:
            return False

        cvowels = set('aeiouAEIOU')
        chas_vowel = False
        chas_consonant = False

        for cchar in word:
            if not cchar.isalnum():  # Special character check
                return False
            if cchar.isalpha():  # Check only letters for vowels/consonants
                if cchar in cvowels:
                    chas_vowel = True
                else:
                    chas_consonant = True

        return chas_vowel and chas_consonant

# Example usage:
csol = Solution()
print(csol.isValid("234Adas"))  # ✅ True
print(csol.isValid("b3"))       # ❌ False (length < 3 and no vowel)
print(csol.isValid("a3$e"))     # ❌ False (contains '$' and no consonant)
print(csol.isValid("aei1"))     # ❌ False (no consonant)
print(csol.isValid("B1c"))      # ❌ False (no vowel)
print(csol.isValid("abc123"))   # ✅ True