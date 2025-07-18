class Solution:
    def minLength(self, s):
        temp = []
        for ch in s:
            if temp and temp[-1] == 'A' and ch == 'B':
                temp.pop()
            elif temp and temp[-1] == 'C' and ch == 'D':
                temp.pop()
            else:
                temp += ch
        return len(temp)