class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        word = set(word)
        c=0
        for i in word:
            if i.islower():
                if i.upper() in word:
                    c+=1
            else:
                if i.lower() in word:
                    c+=1
        return c/2