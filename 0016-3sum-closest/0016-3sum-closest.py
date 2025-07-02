class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        cclosest = float('inf')
        
        for ci in range(len(nums) - 2):
            cleft = ci + 1
            cright = len(nums) - 1
            
            while cleft < cright:
                cs = nums[ci] + nums[cleft] + nums[cright]
                
                # Check if this sum is closer to target
                if abs(cs - target) < abs(cclosest - target):
                    cclosest = cs

                # Move pointers
                if cs < target:
                    cleft += 1
                elif cs > target:
                    cright -= 1
                else:
                    return cs  # Exact match
        
        return cclosest