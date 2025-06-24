from bisect import bisect_right

class Solution(object):
    def answerQueries(self, nums, queries):
        nums.sort()
        
        # Custom accumulate for Python 2
        def accumulate(arr):
            total = 0
            result = []
            for num in arr:
                total += num
                result.append(total)
            return result
        
        prefix_sums = accumulate(nums)
        return [bisect_right(prefix_sums, q) for q in queries]