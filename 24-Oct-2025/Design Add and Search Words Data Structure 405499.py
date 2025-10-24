# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isEnd = False

class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur = self.root
        for c in word:
            cur = cur.children[c]
        cur.isEnd = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cur = self.root

        def dfs(node, i):
            if i == len(word):
                return node.isEnd

            c = word[i]
            if c == ".":
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            else:
                if c not in node.children:
                    return False
            return dfs(node.children[c], i + 1)
        return dfs(self.root, 0)
        if cur.isEnd:
            return True
        return False

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)