"""Data Analysis: Counting Frequencies"""
import sys
from data_analysis import DataAnalysis


def main(file_name):
    """start the data analysis"""
    data = DataAnalysis(file_name)
    data.read_data(file_name)

    # Report top ten languages by frequency
    print("Languages:")
    print_output(data.top_n_lang_freqs(10))

    # Report top ten country (2 letter) domains by frequency
    print("Top level country domains:")
    print_output(data.top_n_country_tlds_freqs(10, file_name))


def print_output(collection):
    """Format the print out"""
    for item in collection:
        print(item[0]+":  \t", round(item[1], 3))


main(sys.argv[1])
