import collections

class UF:
    def __init__(self, N):
        self.parents = list(range(N))

    def union(self, child, parent):
        self.parents[self.find(child)] = self.find(parent)

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])  # Path compression
        return self.parents[x]

class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        uf = UF(len(accounts))
        ownership = {}

        # Step 1: Union accounts that share an email
        for i, account in enumerate(accounts):
            name = account[0]
            for email in account[1:]:
                if email in ownership:
                    uf.union(i, ownership[email])
                ownership[email] = i

        # Step 2: Group emails by their root account index
        merged = collections.defaultdict(list)
        for email, idx in ownership.items():
            root = uf.find(idx)
            merged[root].append(email)

        # Step 3: Prepare final merged output
        result = []
        for idx, emails in merged.items():
            name = accounts[idx][0]
            result.append([name] + sorted(emails))

        return result