import math

class Solution(object):
    def is_palindrome(self, c_num):
        return str(c_num) == str(c_num)[::-1]

    def is_prime(self, c_num):
        if c_num < 2:
            return False
        if c_num in (2, 3):
            return True
        if c_num % 2 == 0 or c_num % 3 == 0:
            return False
        c_sqrt = int(math.sqrt(c_num))
        for c_i in range(5, c_sqrt + 1, 2):
            if c_num % c_i == 0:
                return False
        return True

    def primePalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if 8 <= n <= 11:
            return 11  # Optimization to avoid even-length palindromes

        while True:
            if self.is_palindrome(n) and self.is_prime(n):
                return n
            n += 1
            if n > 11 and len(str(n)) % 2 == 0:
                n = 10 ** len(str(n)) + 1  # Skip even-length palindromes

# Example usage:
sol = Solution()
print(sol.primePalindrome(6))   # Output: 7
print(sol.primePalindrome(8))   # Output: 11
print(sol.primePalindrome(13))  # Output: 101