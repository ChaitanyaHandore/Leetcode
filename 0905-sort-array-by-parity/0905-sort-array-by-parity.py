class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        a = []
        b = []
        for i in range(len(nums)):
            if nums[i]%2==0:
                a.append(nums[i])
            else:
                b.append(nums[i])
        return a+b