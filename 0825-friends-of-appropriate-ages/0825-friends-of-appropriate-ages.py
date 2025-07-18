class Solution(object):
    def numFriendRequests(self, ages):
        count = [0] * 121                           # counter: count frequency of each age
        for age in ages:
            count[age] += 1
        ans = 0
        for ageA, countA in enumerate(count):       # nested loop, pretty straightforward
            for ageB, countB in enumerate(count):
                if ageA * 0.5 + 7 >= ageB: continue
                if ageA < ageB: continue
                if ageA < 100 < ageB: continue
                ans += countA * countB
                if ageA == ageB: ans -= countA
        return ans    