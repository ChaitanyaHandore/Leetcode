class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        c = 0
        d = 0
        n1 = set(nums1)
        n2 = set(nums2)

        for num in nums1:
            if num in n2:
                c += 1

        for num in nums2:
            if num in n1:
                d += 1

        return [c, d]