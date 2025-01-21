class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        # Convert lists to sets
        set1 = set(nums1)
        set2 = set(nums2)
        
        # Find the difference for each set
        only_in_nums1 = list(set1 - set2)
        only_in_nums2 = list(set2 - set1)
        
        # Return the result as a list of two lists
        return [only_in_nums1, only_in_nums2]
