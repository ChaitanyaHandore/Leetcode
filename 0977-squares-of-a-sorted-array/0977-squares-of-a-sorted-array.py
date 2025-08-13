class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = [x ** 2 for x in nums]  # square each number
        nums.sort()  # sort in ascending order
        return nums