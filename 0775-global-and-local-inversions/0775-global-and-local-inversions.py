class Solution:
    def isIdealPermutation(self, A):
        for i in range(len(A)):
            if i - A[i] > 1 or i - A[i] < -1: return False
        return True