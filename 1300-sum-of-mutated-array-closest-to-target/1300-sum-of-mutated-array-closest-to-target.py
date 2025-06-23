class Solution(object):
    def findBestValue(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        def get_mutated_sum(value):
            return sum(min(x, value) for x in arr)

        low, high = 0, max(arr)
        result = high
        min_diff = float('inf')
        
        while low <= high:
            mid = (low + high) // 2
            curr_sum = get_mutated_sum(mid)
            diff = abs(curr_sum - target)

            if diff < min_diff or (diff == min_diff and mid < result):
                min_diff = diff
                result = mid
            
            if curr_sum < target:
                low = mid + 1
            else:
                high = mid - 1

        return result