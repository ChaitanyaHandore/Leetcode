class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        r = []
        nums.sort()
        
        for i,a in enumerate(nums):
            if i >0 and nums[i-1]==a:
                continue
            
            i = i+1
            j = len(nums)-1
            while i<j:
                s = a + nums[i]+nums[j]
                if s>0:
                    j-=1
                elif s<0:
                    i+=1
                else:
                    r.append([a,nums[i],nums[j]])
                    i+=1
                    while nums[i]==nums[i-1] and i<j:
                        i+=1
        return r