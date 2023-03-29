"""Data analysis class"""
import re


class DataAnalysis:
    """A data analysis class"""

    def __init__(self, file_name):
        """Initialize the constructor"""
        self.name = file_name
        self.count = 0
        self.language_list = []
        self.dic = {}  # dictionary object

    def read_data(self, file_name):
        """read the data and get the counts"""
        try:
            file = open(file_name)

        except FileNotFoundError as _:
            print(f"Unable to open {file_name}")
            return

        lines = file.readlines()

        for line in lines:
            line = line.strip('\n').split(',')
            self.language_list.append(line[6])  # append language to list
            self.count += 1

        for language in self.language_list:
            if language not in self.dic:
                self.dic[language] = 1   # calculate the language frequency
            else:
                self.dic[language] += 1

    def top_n_lang_freqs(self, N):
        """Calculate the top n languages"""

        DIGIT = 3
        d = {
            x: round(self.dic[x] / self.count, DIGIT) for x in self.dic.keys()
        }
        a = sorted(d.items(), key=lambda x: x[1], reverse=True)

        return a[0:N]

    def top_n_country_tlds_freqs(self, N, file):  # pass file_name
        """Calculate the top n countries"""
        domain = []
        maps = {}
        count = 0

        try:
            file = open(file)

        except FileNotFoundError as _:
            print(f"Unable to open {file}")
            return

        self.lines = file.readlines()
        for line in self.lines:

            line = line.split(',')
            xyz = line[3]
            xyz = re.findall('[.]\\w+$', xyz)
            for item in xyz:
                count += 1
                item = item[1:]
                if len(item) == 2:
                    domain.append(item)

        for key in domain:
            if key in maps:  # key error 'vu' due to input error
                maps[key] += 1
            else:
                maps[key] = 1

        DIGIT = 3
        dic = {x: round(maps[x] / count, DIGIT) for x in maps.keys()}
        b = sorted(dic.items(), key=lambda x: x[1], reverse=True)

        return b[0:N]

# How to imporve this code?
# 1. write a read_data and add_item function for top_n_country_tlds_freqs
