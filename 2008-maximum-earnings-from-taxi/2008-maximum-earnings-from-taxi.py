class Solution(object):
    def maxTaxiEarnings(self, n, rides):
        """
        :type n: int
        :type rides: List[List[int]]
        :rtype: int
        """
        import collections
        hashmap = collections.defaultdict(list)
        for start, end, tip in rides:
            hashmap[end].append((start, tip))

        dp = [0]*(n+1)
        for location in range(1, n+1):
            # taxi driver has the fare from the previous location, let's see if he/she can make more money by dropping someone at the current location
            # we check that by checking if the current location is an end point, among the ones gathered as hashmap keys
            dp[location] = dp[location-1] 
            if location in hashmap:
                profitDroppingPassengersHere = 0
                # for each ending trip at the current 'location'
                for start, tip in hashmap[location]:
                    profitDroppingPassengersHere = max(profitDroppingPassengersHere, location - start + tip + dp[start])
                # update the dp
                dp[location] = max(dp[location], profitDroppingPassengersHere)

        return dp[n]
