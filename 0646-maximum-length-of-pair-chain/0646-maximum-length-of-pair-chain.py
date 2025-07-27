class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(key=lambda x: x[1])
        
        prev = 0
        res = 1
        
        for i in range(1, len(pairs)):
            if pairs[prev][1] < pairs[i][0]:
                prev = i
                res += 1
        
        return res