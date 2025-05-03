class Solution:
    def solve(self, s, k):
        n = len(s)
        i = n - 1
        j = 1
        v = []
        
        while i >= 0:
            if s[i] == k[j]:
                v.append(i)
                j -= 1
            if j == -1:
                break
            i -= 1
        
        if len(v) < 2:
            return 1e5
        
        a = v[0]
        b = v[1]
        return (n - 1) - a + a - b - 1
    
    def minimumOperations(self, s):
        n = len(s)
        a = n
        
        for char in s:
            if char == '0':
                a -= 1
                break
        
        a = min(a, self.solve(s, "00"))
        a = min(a, self.solve(s, "25"))
        a = min(a, self.solve(s, "50"))
        a = min(a, self.solve(s, "75"))
        
        return a

# Usage example
solution = Solution()
s = "example"  # Replace with your input string
result = solution.minimumOperations(s)
print(result)