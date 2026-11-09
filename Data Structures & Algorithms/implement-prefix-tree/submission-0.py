class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        # iterate through each char in the word
        for char in word:
            # initialize child for char if not already exist
            if char not in curr.children:
                curr.children[char] = TrieNode()
            # advance 
            curr = curr.children[char]

        # last char (after iterating through prefix chars is a word)
        curr.word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.word        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True
        