# 208. Implement Trie - Prefix Tree

# 定义一个trie树节点，包含当前的children和isWord布尔值。
# children是一个字典，key为一个字符，value为这个字符对应的后缀所组成的TrieNode。
# isWord表示是否有一个word到此node结束。
class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}
        self.isWord = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    # 即遍历单词的每个字符，逐层查找，有则继续，没有就创建一个新的TrieNode，最后一位IsWord = True
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for letter in word:
            child = node.children.get(letter)
            if not child:
                child = TrieNode()
                node.children[letter] = child
            node = child
        node.isWord = True

    # 遍历单词每个字符，逐层查找，没有立即返回False，找到最后一个TrieNode，则返回 TrieNode.isWord
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for letter in word:
            node = node.children.get(letter)
            if not node:
                return False
        return node.isWord

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for letter in prefix:
            node = node.children.get(letter)
            if not node:
                return False
        return True