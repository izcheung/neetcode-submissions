class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Solution:

    def makeTrie(self, words):
        # Insert all words in a Trie
        for word in words:
            cur = self.root
            for char in word:
                if char not in cur.children:
                    cur.children[char] = TrieNode()
                cur = cur.children[char]
            cur.word = True

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.root = TrieNode()
        self.makeTrie(words)

        res = []
        word = []

        def dfs(r, c, seen, cur):
            rowInBounds = 0 <= r < len(board)
            colInBounds = 0 <= c < len(board[0])
            
            if not rowInBounds or not colInBounds:
                return False

            if (r,c) in seen:
                return False
            
            char = board[r][c]
            if char not in cur.children:
                return False

            word.append(char)
            cur = cur.children[char]

            if cur.word:
                copy = word.copy()
                cur.word = False
                res.append("".join(copy))

            
            seen.add((r,c))

            dfs(r+1, c, seen, cur)
            dfs(r-1, c, seen, cur)
            dfs(r, c+1, seen, cur)
            dfs(r, c-1, seen, cur)

            seen.remove((r,c))
            word.pop()

        seen = set()
        cur = self.root

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] not in cur.children:
                    continue
                dfs(r, c, seen, cur)
        return res




        
