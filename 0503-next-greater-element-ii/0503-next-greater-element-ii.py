class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n         # default -1 for all
        stack = []             # monotonic decreasing stack

        # traverse array twice in reverse
        for i in range(2*n - 1, -1, -1):
            num = nums[i % n]

            # pop all smaller/equal elements
            while stack and num >= stack[-1]:
                stack.pop()

            # only fill result for the first n elements
            if i < n:
                res[i] = -1 if not stack else stack[-1]

            # push current element into stack
            stack.append(num)

        return res