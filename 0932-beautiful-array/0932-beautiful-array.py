class Solution:
    def beautifulArray(self, n):
        return (
            [1, 2][:n]
            if n < 3
            else [x * 2 - 1 for x in self.beautifulArray((n + 1) // 2)]
            + [x * 2 for x in self.beautifulArray(n // 2)]
        )