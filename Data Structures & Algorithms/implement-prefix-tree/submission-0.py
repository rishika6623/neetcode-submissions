class PrefixTree:

    def __init__(self):
        self.root = {}
        
    def insert(self, word: str) -> None:
        curr = self.root
        for letter in word:
            if letter in curr:
                curr =  curr[letter]
            else:
                curr[letter] = {}
                curr = curr[letter]
        curr["end"] = 0

    def search(self, word: str) -> bool:
        curr = self.root
        for letter in word:
            if letter not in curr:
                return False
            curr = curr[letter]
        if "end" not in curr:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for letter in prefix:
            if letter not in curr:
                return False
            curr = curr[letter]
        return True
        