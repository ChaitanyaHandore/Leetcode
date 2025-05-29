class Solution(object):
    def countConsistentStrings(self, allowed, words):
        c = 0
        for word in words:
            if all(ch in allowed for ch in word):
                c += 1
        return c