class Solution:
    def findMinimumOperations(self, s1, s2, s3):
        size, l1, l2, l3 = 0, len(s1), len(s2), len(s3)

        for a, b, c in zip(s1, s2, s3):
            if a == b == c:
                size += 1
            else: break
        
        return (l1 + l2 + l3) - 3 * size if size > 0 else -1