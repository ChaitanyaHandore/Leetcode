class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        from collections import Counter
        
        # Split sentences into words and count frequencies
        cwords1 = s1.split()
        cwords2 = s2.split()
        
        # Merge both word lists
        ccombined = cwords1 + cwords2
        
        # Count frequency of all words
        ccounter = Counter(ccombined)
        
        # Collect words that appear exactly once
        cuncommon = [cword for cword in ccounter if ccounter[cword] == 1]
        
        return cuncommon