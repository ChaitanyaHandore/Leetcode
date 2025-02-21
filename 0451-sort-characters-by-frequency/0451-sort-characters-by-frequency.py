from collections import Counter

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Step 1: Count character frequencies
        ccounts = Counter(s)

        # Step 2: Sort characters by frequency (descending)
        csorted_chars = sorted(ccounts.items(), key=lambda x: x[1], reverse=True)

        # Step 3: Build the result string
        cresult = ''.join([cchar * ccount for cchar, ccount in csorted_chars])

        return cresult