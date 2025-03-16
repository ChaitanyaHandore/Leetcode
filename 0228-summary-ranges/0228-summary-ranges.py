class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        
        result = []
        start = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:  # Found a gap
                if start == nums[i - 1]:
                    result.append(str(start))
                else:
                    result.append(str(start) + "->" + str(nums[i - 1]))
                start = nums[i]  # Start a new range
        
        # Add the last range
        if start == nums[-1]:
            result.append(str(start))
        else:
            result.append(str(start) + "->" + str(nums[-1]))

        return result

# Test cases
sol = Solution()
print(sol.summaryRanges([0,1,2,4,5,7]))  # Output: ["0->2","4->5","7"]
print(sol.summaryRanges([0,2,3,4,6,8,9]))  # Output: ["0","2->4","6","8->9"]
print(sol.summaryRanges([]))  # Output: []
print(sol.summaryRanges([1]))  # Output: ["1"]
print(sol.summaryRanges([1,3]))  # Output: ["1","3"]