class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        from collections import Counter
        s_count = Counter(s)
        t_count = Counter(t)

        for ch in t_count:
            if t_count[ch] != s_count.get(ch, 0):
                return ch