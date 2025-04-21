class Solution(object):
    def minimizeSet(self, divisor1, divisor2, uniqueCnt1, uniqueCnt2):
        """
        :type divisor1: int
        :type divisor2: int
        :type uniqueCnt1: int
        :type uniqueCnt2: int
        :rtype: int
        """
        def lcm(a, b):
            def gcd(x, y):
                while y:
                    x, y = y, x % y
                return x
            return abs(a * b) // gcd(a, b)
        
        lcm_val = lcm(divisor1, divisor2)
        left, right = 1, 10**10
        ans = right
        
        while left <= right:
            mid = (left + right) // 2
            
            # Numbers not divisible by divisor1
            valid1 = mid - mid // divisor1
            # Numbers not divisible by divisor2
            valid2 = mid - mid // divisor2
            # Total valid numbers (considering overlap)
            total = mid - mid // lcm_val
            
            # Check if we can get enough numbers for both arrays
            if valid1 >= uniqueCnt1 and valid2 >= uniqueCnt2 and total >= uniqueCnt1 + uniqueCnt2:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans