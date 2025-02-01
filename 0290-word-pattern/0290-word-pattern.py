class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
        if len(pattern) != len(words):  # Check if pattern and words have the same length
            return False
        
        char_to_word = {}
        word_to_char = {}
        
        for c, word in zip(pattern, words):
            if c in char_to_word:
                if char_to_word[c] != word:  # Pattern already mapped to a different word
                    return False
            else:
                if word in word_to_char:  # Word already mapped to a different pattern character
                    return False
                char_to_word[c] = word
                word_to_char[word] = c
        
        return True