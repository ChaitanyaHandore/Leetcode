class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}  # Dictionary to store the numbers and their indices

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i

        return []  # In case no solution is found

solution = Solution()
nums = [2, 7, 11, 15]
target = 9
print(solution.twoSum(nums, target))
