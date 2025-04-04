class Solution(object):
    def checkSubarraySum(self, nums, k):
        remainders_found = {0: -1} # To handle the case when subarray starts from index 0
        curr_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i]
            remainder = curr_sum % k

            if remainder in remainders_found:
                # Check if the length of the subarray is at least 2
                if i - remainders_found[remainder] >= 2:
                    return True
            else:
                # Store the remainder and the current index
                remainders_found[remainder] = i

        return False