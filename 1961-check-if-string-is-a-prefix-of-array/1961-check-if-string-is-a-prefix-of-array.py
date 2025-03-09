class Solution(object):
    def isPrefixString(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        c_prefix = ""
        for c_word in words:
            c_prefix += c_word
            if c_prefix == s:
                return True
            if len(c_prefix) > len(s):  # Stop early if prefix exceeds s
                return False
        return False