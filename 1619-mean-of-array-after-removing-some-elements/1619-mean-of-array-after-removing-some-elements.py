class Solution(object):
    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """
        cLen = len(arr)
        cTrim = int(cLen * 0.05)
        cSortedArr = sorted(arr)
        
        # Remove smallest and largest 5%
        cTrimmedArr = cSortedArr[cTrim : cLen - cTrim]
        
        # Calculate and return the mean
        return float(sum(cTrimmedArr)) / len(cTrimmedArr)