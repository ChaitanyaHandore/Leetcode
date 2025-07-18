class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type words: List[str]
        :rtype: int
        """
        res = set()
        for s in A:
            sort_odd_even = ''.join(sorted(s[1::2]) + sorted(s[::2]))
            res.add(sort_odd_even)
        return len(res)