class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        from collections import Counter
        c1 = Counter(words1)
        c2 = Counter(words2)
        
        count = 0
        for word in c1:
            if c1[word] == 1 and c2[word] == 1:
                count += 1
                
        return count