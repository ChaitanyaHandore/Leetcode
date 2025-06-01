class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        from collections import Counter
        if Counter(target)!=Counter(arr):
            return False
        for i in range(len(target)):
            if target[i] in arr:
                continue
            else:
                return False
        return True