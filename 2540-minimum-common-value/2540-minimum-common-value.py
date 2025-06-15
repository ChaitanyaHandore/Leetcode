class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        set2 = set(nums2)
        common = [num for num in nums1 if num in set2]
        return min(common) if common else -1