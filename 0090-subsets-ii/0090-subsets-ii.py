class Solution:
    def subsetsWithDup(self, n: List[int]) -> List[List[int]]:
        res = []
        subset = []
        n.sort()  # Step 1: Sort to handle duplicates

        def dfs(i):
            if i >= len(n):
                res.append(subset.copy())
                return

            # Include n[i]
            subset.append(n[i])
            dfs(i + 1)

            # Step 2: Skip duplicates
            while i + 1 < len(n) and n[i] == n[i + 1]:
                i += 1

            # Exclude n[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res