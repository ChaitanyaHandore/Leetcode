class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        words = sentence.split()

        index = -1
        for i, word in enumerate(words):
            if word.startswith(searchWord):
                index = i + 1  # 1-based index
                break
        return index