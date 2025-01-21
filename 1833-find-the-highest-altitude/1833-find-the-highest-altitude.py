class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        altitude = 0  
        a = [0] 
        
        for i in range(len(gain)):
            altitude += gain[i]  
            a.append(altitude)  
        
        return max(a)  
