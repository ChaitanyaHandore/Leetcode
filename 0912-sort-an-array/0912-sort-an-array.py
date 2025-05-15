class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.cquick_sort(nums, 0, len(nums) - 1)
        return nums

    def cquick_sort(self, carr, cleft, cright):
        if cleft < cright:
        # Skip recursion if the subarray is all same values
            if all(carr[i] == carr[cleft] for i in range(cleft + 1, cright + 1)):
                return
            cpi = self.cpartition(carr, cleft, cright)
            self.cquick_sort(carr, cleft, cpi - 1)
            self.cquick_sort(carr, cpi + 1, cright)

    import random

    def cpartition(self, carr, cleft, cright):
        # Randomly pick a pivot index and swap with last
        cpivot_index = random.randint(cleft, cright)
        carr[cpivot_index], carr[cright] = carr[cright], carr[cpivot_index]
        
        cpivot = carr[cright]
        ci = cleft - 1
        for cj in range(cleft, cright):
            if carr[cj] <= cpivot:
                ci += 1
                carr[ci], carr[cj] = carr[cj], carr[ci]
        carr[ci + 1], carr[cright] = carr[cright], carr[ci + 1]
        return ci + 1