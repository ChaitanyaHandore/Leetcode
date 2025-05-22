class Solution:
    def getSneakyNumbers(self, nums):
        xor_n2 = reduce(xor, nums)
        xor_n = reduce(xor, range(len(nums) - 2))
        
        xor_ab = xor_n2 ^ xor_n
        diff_bit = xor_ab & -xor_ab
        
        xor_n2_bit = reduce(xor, (n for n in nums if n & diff_bit))
        xor_n2_no_bit = reduce(xor, (n for n in nums if not n & diff_bit))
        
        xor_n_bit = reduce(xor, (n for n in range(len(nums) - 2) if n & diff_bit))
        xor_n_no_bit = reduce(xor, (n for n in range(len(nums) - 2) if not n & diff_bit))
        
        return [xor_n2_bit ^ xor_n_bit, xor_n2_no_bit ^ xor_n_no_bit]