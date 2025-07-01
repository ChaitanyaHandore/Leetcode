class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        from collections import Counter

        count = Counter(digits)
        res = []

        # Check all 3-digit even numbers (100 to 998)
        for num in range(100, 1000, 2):
            c = Counter(map(int, str(num)))
            if all(count[d] >= c[d] for d in c):
                res.append(num)

        return res