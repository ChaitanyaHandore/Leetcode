class Solution(object):
    def maxSumMinProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = [(-1, 0)] 
        running_max = running_sum = 0
        nums.append(0)
        for v in nums:
            while stack[-1][0] >= v:
                min_value, _ = stack.pop()
                running_max = max(running_max, min_value * (running_sum - stack[-1][1]))
            running_sum += v
            stack.append((v, running_sum))
        return running_max % (10**9+7)