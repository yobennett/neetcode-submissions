class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        
        # recursive search 
        def dfs(j, node):
            curr = node

            # iterate through each char in the word starting from j
            for i in range(j, len(word)):
                char = word[i]

                # wildcard char
                if char == ".":

                    # iterate through each child
                    for child in curr.children.values():
                        # next char
                        if dfs(i + 1, child):
                            return True
                    return False

                # exact match char
                else:
                    # current char not in truee
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]

            # true all prefix in true AND leaf node is a word
            return curr.word

        return dfs(0, self.root)     
