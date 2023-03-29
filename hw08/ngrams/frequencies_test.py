"""A test doc for frequencies"""
from frequencies import NgramFrequencies


def test_constructor():  # pass 不传值就过了
    """test the constructor"""
    nf = NgramFrequencies()
    assert nf.value == 0
    assert nf.map == {}


def test_add_item():
    """test the add_item function"""
    nf = NgramFrequencies()
    nf.add_item("the")
    assert nf.value == 1
    assert nf.map["the"] == 1


def test_top_n_counts():  # list object is not callable mistake
    """test the top n counts property"""
    nf = NgramFrequencies()
    for _ in range(1):
        nf.add_item("one")
    for _ in range(3):
        nf.add_item("five")
    for _ in range(6):
        nf.add_item("ten")
    # print(nf.top_n_counts[0])  # 错误：写成了nf.top_n_counts()[0]
    # 当function变成property之后，就不能够再加()了
    assert nf.top_n_counts[0] == ("ten", 6)
    assert nf.top_n_counts[1] == ("five", 3)
    assert nf.top_n_counts[2] == ("one", 1)


def test_top_n_freqs():  # list object is not callable
    """test the top n freqs property"""
    nf = NgramFrequencies()
    for _ in range(1):
        nf.add_item("one")
    for _ in range(3):
        nf.add_item("five")
    for _ in range(6):
        nf.add_item("ten")
    assert nf.top_n_freqs[0][1] == 0.6
    assert nf.top_n_freqs[1][1] == 0.3
    assert nf.top_n_freqs[2][1] == 0.1


def test_frequency():
    """thest the frequency function"""
    nf = NgramFrequencies()
    for _ in range(1):
        nf.add_item("one")
    for _ in range(3):
        nf.add_item("five")
    for _ in range(6):
        nf.add_item("ten")
    assert nf.frequency("one") == 0.1
    assert nf.frequency("five") == 0.3
    assert nf.frequency("ten") == 0.6

# list object is not callable
# 把@property 去掉之后，test case就能够通过
