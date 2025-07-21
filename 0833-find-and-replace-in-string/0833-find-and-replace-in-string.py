class Solution(object):
    def findReplaceString(self, S, indices, sources, targets):
        """
        :type S: str
        :type indices: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        # Prepare a list of valid replacements
        replace_map = []
        for i, src, tgt in zip(indices, sources, targets):
            if S[i:i+len(src)] == src:
                replace_map.append((i, src, tgt))
        
        # Sort replacements in reverse order of indices
        # to avoid messing up string positions during replacement
        replace_map.sort(reverse=True)
        
        # Apply replacements
        for i, src, tgt in replace_map:
            S = S[:i] + tgt + S[i+len(src):]
        
        return S