class Solution(object):
    def sortArrayByParityII(self, nums):
        new = [0] * len(nums)
        e = 0 ; o = 1

        for i in nums:
            if i % 2 == 0:
                new[e] = i
                e += 2
            else:
                new[o] = i
                o += 2

        return new
        