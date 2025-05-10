class Solution(object):
    def maxRotateFunction(self, nums):
        n = len(nums)
        if n < 2:
            return 0

        total_sum = sum(nums)
        current_value = sum(i * nums[i] for i in range(n))
        max_value = current_value

        for i in range(1, n):
            current_value += total_sum - n * nums[-i]
            max_value = max(max_value, current_value)

        return max_value