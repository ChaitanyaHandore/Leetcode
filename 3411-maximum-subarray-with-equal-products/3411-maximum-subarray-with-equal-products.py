class Solution:
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def lcm(self, a, b):
        return (a * b) // self.gcd(a, b)

    def maxLength(self, nums):
        pro = 1
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                gcd = nums[i]
                lcm = 1
                product = 1
                for k in range(i, j + 1):
                    gcd = self.gcd(nums[k], gcd)
                    lcm = self.lcm(nums[k], lcm)
                    product *= nums[k]
                if product == (lcm * gcd):
                    max_len = j - i + 1
                    pro = max(pro, max_len)
        return pro