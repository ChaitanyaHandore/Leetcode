from collections import Counter

class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = Counter(s)
        
        # Unique identifiers for numbers
        num_count = {}
        num_count[0] = count['z']  # zero
        num_count[2] = count['w']  # two
        num_count[4] = count['u']  # four
        num_count[6] = count['x']  # six
        num_count[8] = count['g']  # eight
        
        # Digits that depend on previous counts
        num_count[3] = count['h'] - num_count[8]  # three (h appears in "three" and "eight")
        num_count[5] = count['f'] - num_count[4]  # five (f appears in "five" and "four")
        num_count[7] = count['s'] - num_count[6]  # seven (s appears in "seven" and "six")
        num_count[1] = count['o'] - num_count[0] - num_count[2] - num_count[4]  # one
        num_count[9] = count['i'] - num_count[5] - num_count[6] - num_count[8]  # nine

        # Construct the output
        result = []
        for num in range(10):
            result.append(str(num) * num_count.get(num, 0))
        
        return "".join(result)

# Test cases
sol = Solution()
print(sol.originalDigits("owoztneoer"))  # Output: "012"
print(sol.originalDigits("fviefuro"))    # Output: "45"