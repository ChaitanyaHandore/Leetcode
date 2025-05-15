class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        sorted_arr = sorted(arr, key=lambda x: (bin(x).count('1'), x))
        return sorted_arr