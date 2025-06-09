class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        from collections import Counter
        ccount = Counter(digits)
        cresult = set()
        
        for c1 in range(1, 10):  # Hundreds place (1-9 to avoid leading zero)
            for c2 in range(0, 10):  # Tens place
                for c3 in range(0, 10, 2):  # Units place (even numbers only)
                    cnum = [c1, c2, c3]
                    cnum_count = Counter(cnum)
                    if all(ccount[d] >= cnum_count[d] for d in cnum):
                        cresult.add(c1 * 100 + c2 * 10 + c3)
        
        return len(cresult)