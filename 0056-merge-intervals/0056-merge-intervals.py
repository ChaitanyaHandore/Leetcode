from typing import List

class Solution:
    def merge(self, cintervals: List[List[int]]) -> List[List[int]]:
        if not cintervals:
            return []

        # 1) Sort by start time
        cintervals.sort(key=lambda cx: cx[0])

        # 2) Merge in one pass
        cmerged = []
        ccur_start, ccur_end = cintervals[0]

        for cstart, cend in cintervals[1:]:
            if cstart <= ccur_end:          # overlap (touching counts as overlap)
                ccur_end = max(ccur_end, cend)
            else:
                cmerged.append([ccur_start, ccur_end])
                ccur_start, ccur_end = cstart, cend

        cmerged.append([ccur_start, ccur_end])
        return cmerged