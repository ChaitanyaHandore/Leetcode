class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        r = []
        nums.sort()
        
        for i, a in enumerate(nums):
            if i > 0 and nums[i - 1] == a:
                continue
            
            j = len(nums) - 1
            l = i + 1
            while l < j:
                s = a + nums[l] + nums[j]
                if s > 0:
                    j -= 1
                elif s < 0:
                    l += 1
                else:
                    r.append([a, nums[l], nums[j]])
                    l += 1
                    j -= 1
                    while l < j and nums[l] == nums[l - 1]:
                        l += 1
                    while l < j and nums[j] == nums[j + 1]:
                        j -= 1
        return r