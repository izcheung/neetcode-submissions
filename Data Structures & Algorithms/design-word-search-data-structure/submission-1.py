class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.word = True
        

    def search(self, word: str) -> bool:

        def dfs(i, cur):
            if i == len(word):
                return cur.word
            char = word[i]

            if char == ".":
                for child in cur.children.values():
                    if dfs(i+1, child):
                        return True
                return False

            if char not in cur.children:
                return False
            
            return dfs(i+1, cur.children[char])
        return dfs(0, self.root)



            
        
