class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        if desiredTotal <= 0:
            return True
        if sum(range(1, maxChoosableInteger + 1)) < desiredTotal:
            return False

        memo = {}

        def can_win(choices, total):
            state = tuple(choices)
            if state in memo:
                return memo[state]
            if choices[-1] >= total:
                memo[state] = True
                return True
            for i in range(len(choices)):
                if not can_win(choices[:i] + choices[i+1:], total - choices[i]):
                    memo[state] = True
                    return True
            memo[state] = False
            return False

        return can_win(list(range(1, maxChoosableInteger + 1)), desiredTotal)