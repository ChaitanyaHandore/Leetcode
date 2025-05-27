class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        d = []
        result = []
        for i in range(len(s)):
            if s[i]==c:
                d.append(i)
        for i in range(len(s)):
            a = []
            for j in range(len(d)):
                a.append(abs(i-d[j]))
            result.append(min(a))

        return result