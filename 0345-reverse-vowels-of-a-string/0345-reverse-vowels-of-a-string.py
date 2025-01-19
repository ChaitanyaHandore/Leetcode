class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        v = "aeiouAEIOU"
        a = []
        
        # Collect all vowels in the string
        for i in range(len(s)):
            if s[i] in v:
                a.append(s[i])
        
        # Reverse the list of vowels
        a.reverse()
        
        r = []
        k = 0
        
        # Build the final string with reversed vowels
        for i in range(len(s)):
            if s[i] in v:
                r.append(a[k])
                k += 1
            else:
                r.append(s[i])
        
        # Join the characters to form the result string
        r = "".join(r)
        return r