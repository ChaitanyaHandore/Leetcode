class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        from collections import Counter
        import re

        # Convert to lowercase and remove punctuation
        cwords = re.findall(r'\w+', paragraph.lower())

        # Count word frequencies
        ccounter = Counter(cwords)

        # Find the most common non-banned word
        for cword, ccount in ccounter.most_common():
            if cword not in banned:
                return cword