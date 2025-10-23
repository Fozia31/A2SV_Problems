# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        cur = self.root
        for c in word:
            cur = cur.children[c]
        cur.isEnd = True

    def findRoot(self , word):
        cur = self.root
        prefix = ""

        for c in word:
            if c not in cur.children:
                return word
            cur = cur.children[c]
            prefix += c
            if cur.isEnd:
                return prefix
        return word


class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        tries = Trie()
        for root in dictionary:
            tries.insert(root)
        
        words = sentence.split()
        replaced = [tries.findRoot(word) for word in words]
        return " ".join(replaced)
        