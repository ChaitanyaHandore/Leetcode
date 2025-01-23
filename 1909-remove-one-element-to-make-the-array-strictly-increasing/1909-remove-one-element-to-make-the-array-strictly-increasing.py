class Solution:
    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0  # Count of violations

        for i in range(1, len(nums)):
            # Check for a violation of the strictly increasing order
            if nums[i] <= nums[i - 1]:
                count += 1

                # If there is more than one violation, return False
                if count > 1:
                    return False

                # Check if we can "remove" nums[i] or nums[i-1]
                if i > 1:
                    if nums[i] <= nums[i - 2]:
                        if i + 1 < len(nums) and nums[i + 1] <= nums[i - 1]:
                            return False

        return True