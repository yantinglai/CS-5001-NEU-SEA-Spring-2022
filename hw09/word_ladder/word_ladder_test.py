from word_ladder import WordLadder


def test_make_ladder():
    """Testing the make ladder function"""
    word_list = {"love", "bove", "bare",
                 "bore", "barf", "baff", "buff", "bull"}
    test = WordLadder("love", "buff", word_list)
    new_word = test.make_ladder()
    stack_repr = new_word.__repr__()

    assert stack_repr == 'love\tbove\tbore\tbare\tbarf\tbaff\tbuff\t'
