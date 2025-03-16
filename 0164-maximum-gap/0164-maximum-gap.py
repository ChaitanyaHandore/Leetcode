class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0

        min_val, max_val = min(nums), max(nums)
        if min_val == max_val:
            return 0

        # Compute bucket size and count
        bucket_size = max(1, (max_val - min_val) // (len(nums) - 1))
        bucket_count = (max_val - min_val) // bucket_size + 1

        # Initialize buckets with [min, max]
        buckets = [[float('inf'), float('-inf')] for _ in range(bucket_count)]

        # Place elements in buckets
        for num in nums:
            index = (num - min_val) // bucket_size
            buckets[index][0] = min(buckets[index][0], num)
            buckets[index][1] = max(buckets[index][1], num)

        # Compute maximum gap
        max_gap = 0
        prev_max = min_val

        for min_bucket, max_bucket in buckets:
            if min_bucket == float('inf'):  # Skip empty buckets
                continue
            max_gap = max(max_gap, min_bucket - prev_max)
            prev_max = max_bucket

        return max_gap

# Test cases
sol = Solution()
print(sol.maximumGap([3,6,9,1]))  # Output: 3
print(sol.maximumGap([10]))       # Output: 0