class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        c=0
        for i in range(len(words)):
            a=0
            for j in range(len(words[i])):
                if words[i][j] in allowed:
                    a+=1
                if a==len(words[i]):
                    c+=1
        return c