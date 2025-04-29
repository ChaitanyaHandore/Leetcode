class Solution(object):
    def minimumPairRemoval(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def is_non_decreasing(clist):
            for ci in range(1, len(clist)):
                if clist[ci] < clist[ci - 1]:
                    return False
            return True

        coperations = 0

        while not is_non_decreasing(nums):
            cmin_sum = float('inf')
            cindex = -1

            # Find leftmost adjacent pair with the minimum sum
            for ci in range(len(nums) - 1):
                cpair_sum = nums[ci] + nums[ci + 1]
                if cpair_sum < cmin_sum:
                    cmin_sum = cpair_sum
                    cindex = ci

            # Merge the pair
            cnew_num = nums[cindex] + nums[cindex + 1]
            nums = nums[:cindex] + [cnew_num] + nums[cindex + 2:]
            coperations += 1

        return coperations