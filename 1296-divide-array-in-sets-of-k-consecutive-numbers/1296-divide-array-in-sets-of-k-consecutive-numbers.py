from collections import Counter

class Solution(object):
    def isPossibleDivide(self, nums, k):
        if len(nums) % k != 0:
            return False
        
        count = Counter(nums)
        for num in sorted(count):
            while count[num] > 0:
                for i in range(k):
                    if count[num + i] <= 0:
                        return False
                    count[num + i] -= 1
        return True