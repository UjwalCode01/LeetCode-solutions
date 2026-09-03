class MagicDictionary:

    def __init__(self):
        self.words = []

    def buildDict(self, dictionary):
        self.words = dictionary

    def search(self, searchWord):
        for word in self.words:
            if len(word) != len(searchWord):
                continue

            diff = 0

            for i in range(len(word)):
                if word[i] != searchWord[i]:
                    diff += 1

            if diff == 1:
                return True

        return False