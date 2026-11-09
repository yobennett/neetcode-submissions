class UnionFind:
    
    def __init__(self, n: int):
        self.parent = {}
        self.rank = {}
        self.num_components = n

        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0

    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y) # same parent

    def union(self, x: int, y: int) -> bool:
        xRoot, yRoot = self.find(x), self.find(y)
        xRank, yRank = self.rank[xRoot], self.rank[yRoot]

        # same root, nothing to do
        if xRoot == yRoot:
            return False

        if xRank > yRank:
            # x rank greater, set y's root to x
            self.parent[yRoot] = xRoot
        elif xRank < yRank:
            # y rank greater, set x's root to y
            self.parent[xRoot] = yRoot
        else:
            # same rank, set y parent to x parent
            self.parent[yRoot] = xRoot
            # increment x parent rank
            self.rank[xRoot] += 1

        # decrement number of components upon each successful union
        self.num_components -= 1

        return True

    def getNumComponents(self) -> int:
        return self.num_components

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Union Find with a node per account
        uf = UnionFind(len(accounts))

        # map for email -> account index
        emailToAccountIndex = {}

        for i, account in enumerate(accounts):
            for email in account[1:]:
                # email already mapped to account index
                if email in emailToAccountIndex:
                    uf.union(i, emailToAccountIndex[email])
                # email is unmapped to account index
                else:
                    emailToAccountIndex[email] = i

        # index of account -> emails
        emailGroup = defaultdict(list)

        # iterate through emails and group it by root (account index i)
        for email, i in emailToAccountIndex.items():
            root = uf.find(i)
            emailGroup[root].append(email)

        results = []
        for i, emails in emailGroup.items():
            name = accounts[i][0]
            result = [name] + sorted(emailGroup[i])
            results.append(result)

        return results