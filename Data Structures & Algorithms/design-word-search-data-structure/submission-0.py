class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False

class WordDictionary:

    def __init__(self):
        # root = TrieNode
        self.store = []

    def addWord(self, word: str) -> None:
        self.store.append(word)

    def search(self, word: str) -> bool:
        for w in self.store:
            if len(w) != len(word):
                continue

            i = 0
            while i < len(w):
                if w[i] == word[i] or word[i] == '.':
                    i +=1
                else:
                    break
                if len(w) == i:
                    return True

        return False
                
