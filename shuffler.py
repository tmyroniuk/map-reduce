from itertools import groupby
from operator import itemgetter
import sys

file_name = "file"


def read_mapper_output(files_number, separator='\t'):
    for file_numer in range(1, files_number + 1):
        with open(f'{file_name}{file_numer}', 'r') as file:
            for line in file:
                yield line.rstrip().split(separator, 1)


def main(separator='\t'):
    # Read number of files
    files_number = int(next(sys.stdin))
    data = read_mapper_output(files_number)
    print(data)
    # groupby groups multiple word-count pairs by word,
    # and creates an iterator that returns consecutive keys and their group:
    #   current_word - string containing a word (the key)
    #   group - iterator yielding all ["<current_word>", "<count>"] items
    for [word, count] in sorted(data, key=itemgetter(0)):
        print('%s%s%s' % (word, separator, count))


if __name__ == "__main__":
    main()
