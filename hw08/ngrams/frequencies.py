"""Calculate top n counts, top n frequencies, and frequency of N-gram"""


class NgramFrequencies:
    """A class of NgramFrequencies"""

    def __init__(self):
        """Initialize the NgramFrequencies"""
        self.map = {}  # 创建每个 ngram 对应的 map
        self.value = 0   # 每个 ngram 对应 的 total value

    def add_item(self, word):
        """Takes an n-gram and increments its count in the dictionary"""
        self.value += 1  # 总数每次都自增1
        if word in self.map:
            self.map[word] += 1
        else:
            self.map[word] = 1

    @property
    def top_n_counts(self):
        """Returns a list of items sorted on the count"""
        return sorted(
            self.map.items(), key=lambda x: x[1], reverse=True
        )

    @property
    def top_n_freqs(self):
        """Returns a list of items sorted on the frequencies"""
        ROUND = 3
        d = {x: round(self.map[x] / self.value, ROUND)
             for x in self.map.keys()}  # dic comprehension
        # dic 转成 list
        return sorted(
            d.items(), key=lambda x: x[1], reverse=True  # sort the list
        )

    def frequency(self, word):
        """calculate the frequency"""
        return round(self.map[word] / self.value, 3)
