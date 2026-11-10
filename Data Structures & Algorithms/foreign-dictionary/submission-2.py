class Solution:
    # DFS
    def foreignDictionary(self, words: List[str]) -> str:
        # setup
        # adjacency list with entry per character in words
        adj = {c:set() for w in words for c in w}

        # compare words pair-wise
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            # if w1 not lexicographically smaller than w2
            # then claim is incorrect
            minLength = min(len(w1), len(w2))
            # w1 is longer and shared prefix are equa.
            if len(w1) > len(w2) and w1[:minLength] == w2[:minLength]:
                return ""

            # iterate through characters after shared prefix
            # insert neighbors in topologicial sort
            for j in range(minLength):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        # False -> already visited
        # True -> visiting currently
        # n/a -> not yet visited
        visit = {}

        result = []

        # dfs with post-order traversal
        def dfs(char):
            # prepare
            if char in visit:
                # True already visited means cycle
                return visit[char]

            visit[char] = True

            # run dfs on neighbors first
            for neighbor in adj[char]:
                if dfs(neighbor):
                    return True

            # clean up
            visit[char] = False
            result.append(char)

        # check each char
        # True then cycle or not possible
        for char in adj:
            if dfs(char):
                return ""

        # reverse output since post-order and dfs visited children first
        result.reverse()
        return "".join(result)