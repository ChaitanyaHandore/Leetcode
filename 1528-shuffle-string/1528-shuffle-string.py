class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        s1 = [""] * len(s)  # Create a list with empty strings of the same length as s
        for i in range(len(indices)):
            s1[indices[i]] = s[i]  # Place each character at its correct position
        return "".join(s1)  # Convert list to string and return