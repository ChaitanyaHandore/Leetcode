class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        a=sorted(nums)

        dict={}

        for i,num in enumerate(a):
            if num not in dict:
                dict[num]=i

        ret=[]

        for i in nums:
            ret.append(dict[i])

        return ret

        