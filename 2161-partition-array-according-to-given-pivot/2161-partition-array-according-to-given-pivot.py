class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        a = []
        r = []
        s = []
        for i in range(len(nums)):
            if nums[i]<pivot:
                a.append(nums[i])
            elif nums[i]==pivot:
                s.append(nums[i])
            else:
                r.append(nums[i])
        c = a+s+r
        return c