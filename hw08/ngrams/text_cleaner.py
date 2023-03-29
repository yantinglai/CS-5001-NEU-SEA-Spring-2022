"""A text cleaner"""


class TextCleaner:
    """A text cleaner class"""

    def __init__(self, file_name):  # pass the file_name
        """Initialize the text cleaner"""
        self.file_name = file_name

    def open_file(self, file_name):  # pass the file_name
        """Open the file"""
        try:
            f = open(file_name)
        except FileNotFoundError as e:
            print(f"Unable to open {file_name}")
            return
        f = f.read().lower()
        a = self.read_file(f)

        return a

    def read_file(self, text):
        """Read file"""
        text = text.replace('mr.', 'mr')
        text = text.replace(',', ' COMMA')
        text = text.replace('-', " ")  # 算两个单词
        text = text.replace('\"', "")  # 把 " 删除
        text = text.replace('(', "")
        text = text.replace(')', "")
        text = text.replace('\n', ".")  # 把换行改成句号
        text = text.split(".")
        text = [x for x in text if len(x) > 0]  # 把 text里的空element去掉了

        return text
