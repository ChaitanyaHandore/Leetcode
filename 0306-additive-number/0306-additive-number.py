class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        
        for i in range(1, n):
            for j in range(i + 1, n):
                num1, num2 = num[:i], num[i:j]
                
                # Check for leading zeros
                if (len(num1) > 1 and num1[0] == '0') or (len(num2) > 1 and num2[0] == '0'):
                    continue
                
                while j < n:
                    sum_str = str(int(num1) + int(num2))
                    k = j + len(sum_str)
                    
                    if k > n or num[j:k] != sum_str:
                        break
                    
                    num1, num2 = num2, sum_str
                    j = k
                    
                    if k == n:
                        return True
        
        return False

# Test cases
sol = Solution()
print(sol.isAdditiveNumber("112358"))  # Output: True
print(sol.isAdditiveNumber("199100199"))  # Output: True
print(sol.isAdditiveNumber("123"))  # Output: True
print(sol.isAdditiveNumber("1023"))  # Output: False