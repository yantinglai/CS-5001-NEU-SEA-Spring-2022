import math
import random
from list_searcher import ListSearcher

N = 1000
K = 11000
STEP = 1000


def main():

    # Linear search with unsorted list
    for i in range(N, K, STEP):
        test_linear_search(i, 2000, ordered=False)

    # Linear search with sorted list
    for i in range(N, K, STEP):
        test_linear_search(i, 2000, ordered=True)

    # Binary search with unsorted list
    for i in range(N, K, STEP):
        test_binary_search(i, 1000)

    # Find median from 100 to 1000
    for i in range(100, 1100, 100):
        test_median(i, 140)


def test_linear_search(N, num_trials, ordered):
    """
    Run a linear search experiment with the given configurations:
    N:          list size
    num_trials: the number of times linear_search is called
    ordered:    whether ordered or un-ordered lists are used
    """
    min_comps = math.inf  # Initialize min as infinity
    max_comps = -math.inf  # Initialize max as -infinity
    total_comps = 0
    # Create a ListSearcher and generate (un)ordered data
    s = ListSearcher(N)
    s.generate_data(ordered)

    # Run the trials
    for _trial in range(num_trials):
        s.reset_comparisons()  # reset_comparison count
        key = random.randrange(N)  # generate a random key from 0 to N-1
        s.linear_search(key)  # call linear search
        num_comps = s.comparisons()  # retrieve number of comparisons

        # update max, min, and total number of comparisons
        if (num_comps > max_comps):
            max_comps = num_comps
        if (num_comps < min_comps):
            min_comps = num_comps
        total_comps += num_comps

    print("N=" + str(N) + ",",
          "best=" + str(min_comps), "(expected 1),",
          "worst=" + str(max_comps), "(expected", str(N)+"),",
          "avg=" + str(total_comps/num_trials),
          "(expected", str(math.ceil(N/2))+")")


def test_binary_search(N, num_trials):
    """
    Run a binary search experiment with the given configurations:
    N:          list size
    num_trials: the number of times binary_search is called
    """
    min_comps = math.inf  # Initialize min as infinity
    max_comps = -math.inf  # Initialize max as -infinity
    total_comps = 0
    # Creates a ListSearcher and generates ordered data
    s = ListSearcher(N)
    s.generate_data()

    # Run the trials
    for _trial in range(num_trials):
        s.reset_comparisons()
        key = random.randrange(N)
        s.binary_search(key)
        num_comps = s.comparisons()

        # update max, min, and total number of comparisons
        if (num_comps > max_comps):
            max_comps = num_comps
        if (num_comps < min_comps):
            min_comps = num_comps
        total_comps += num_comps

    print("N=" + str(N) + ",",
          "best=" + str(min_comps), "(expected 1),",
          "worst=" + str(max_comps), "(expected",
          str(math.ceil(math.log(N)/math.log(2.0)))+"),",
          "avg=" + str(total_comps/num_trials), "(expected ???)")


def test_median(N, num_trials):
    min_comps = math.inf  # Initialize min as infinity
    max_comps = -math.inf  # Initialize max as -infinity
    total_comps = 0
    s = ListSearcher(N)

    # Run the trials
    for _trial in range(num_trials):
        s.generate_data(ordered=False)

        s.reset_comparisons()
        s.find_median()
        num_comps = s.comparisons()

        # update max, min, and total number of comparisons
        if (num_comps > max_comps):
            max_comps = num_comps
        if (num_comps < min_comps):
            min_comps = num_comps
        total_comps += num_comps

    print("N=" + str(N) + ",",
          "best=" + str(min_comps) + ",",
          "worst=" + str(max_comps) + ",",
          "avg=" + str(total_comps/num_trials))


main()
