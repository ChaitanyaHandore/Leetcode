class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        cres = []
        cpath = []
        cused = [False] * len(nums)

        def backtrack():
            if len(cpath) == len(nums):
                cres.append(cpath[:])
                return

            for ci in range(len(nums)):
                if not cused[ci]:
                    cpath.append(nums[ci])
                    cused[ci] = True
                    backtrack()
                    cpath.pop()
                    cused[ci] = False

        backtrack()
        return cres