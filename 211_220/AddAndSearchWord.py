# 211. Add and Search Word - Data Structure Design
# 与208题类似，创建一个TrieNode对象。

class TrieNode:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}
        self.isWord = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    # addWord的过程与208中的insert过程完全一样
    def addWord(self, word):
        """
        Adds a word into the data structure.
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

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        node = self.root
        return self.searchNode(node, word)

    # 当字母为"."时，采用回溯算法，将当前node的dict中所有的value拿来当作child，只要其中一个返回的是True，那么整个方法返回True。
    # 注意的是，我们在TrieNode中设置Boolean值isWord，表示是否有一个word到此node结束。
    def searchNode(self, node, word):
        if not word:
            return node.isWord

        letter = word[0]
        if letter != ".":
            child = node.children.get(letter)
            if not child:
                return False
            node = child
            return self.searchNode(node, word[1:])
        else:
            for k, v in node.children.items():
                if self.searchNode(v, word[1:]):
                    return True
            return False


if __name__ == "__main__":
    w = WordDictionary()
    w.addWord("ab")
    w.addWord("...")
    print(w.search("a"))
    print(w.search("ab"))